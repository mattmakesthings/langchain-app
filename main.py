from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_pydantic import validate

from serializers.query import QueryModel, QueryResponseModel
from serializers.market_research import MarketResearchModel
from serializers.social_media_assistant import SocialMediaAssistantModel, SocialMediaAssistantResponse

from controllers.model_query import ModelQueryController
from controllers.image_variation import ImageVariationController


load_dotenv()
app = Flask(__name__)

mqc = ModelQueryController()
ivc = ImageVariationController()


@app.route("/query", methods=["GET"])
@validate()
def query(query: QueryModel):
    result = mqc.query(query.prompt)
    return QueryResponseModel(
        response=result
    ).json()

@app.route("/compare", methods=["GET"])
@validate()
def market_research(query: MarketResearchModel):
    result = mqc.market_research_query(query.companies)
    return QueryResponseModel(
        response=result
    ).json()

@app.route("/social_media", methods=["GET"])
@validate()
def social_media(query: SocialMediaAssistantModel):
    result = mqc.social_media_post(query.product_description)
    images = ivc.generate(query.product_description)
    return SocialMediaAssistantResponse(
        response=result,
        images = images,
    ).json()

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)

    