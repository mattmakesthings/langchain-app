from flask import Flask, request
from dotenv import load_dotenv
from flask_pydantic import validate

from serializers.query import QueryModel, QueryResponseModel
from serializers.market_research import MarketResearchModel
from serializers.social_media_assistant import SocialMediaPromptModel, SocialMediaCaptionResponse, SocialMediaImageResponse
from serializers.instagram_post import InstagramPostModel
from serializers.image_upload import ImageUpload

from controllers.model_query import ModelQueryController
from controllers.image_variation import ImageGenerationController
from controllers.post_to_instagram import InstagramController
from controllers.utils import download_photos, delete_photos, convert_to_jpgs


load_dotenv()
app = Flask(__name__)

mqc = ModelQueryController()
ivc = ImageGenerationController()


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

@app.route("/social_media/caption", methods=["GET"])
@validate()
def generate_caption(query: SocialMediaPromptModel):
    result = mqc.social_media_post(query.product_description)
    return SocialMediaCaptionResponse(
        response=result,
    ).json()

@app.route("/social_media/image", methods=["GET"])
@validate()
def generate_image(query: SocialMediaPromptModel):
    images = ivc.generate(query.product_description)
    return SocialMediaImageResponse(
        images = images,
    ).json()

@app.route("/social_media/image_variations", methods=["POST"])
def generate_variations():
    png = ImageUpload(file=request.data)
    images = ivc.generate_variations(png.file)
    return SocialMediaImageResponse(
        images = images,
    ).json()


@app.route("/social_media/instagram", methods=["POST"])
@validate()
def instagram_post(body: InstagramPostModel):
    ig_controller = InstagramController(
        username=body.username,
        password=body.password,
        verification_code=body.verification_code
    )

    png_temp_files = download_photos(body.image_urls)
    jpg_temp_files = convert_to_jpgs(png_temp_files)
    file_paths = [tempfile.name for tempfile in jpg_temp_files ]
    
    instagram_response = ig_controller.make_post(
        file_paths=file_paths,
        caption=body.caption,
    )

    delete_photos(
        tempfiles=jpg_temp_files
    )

    return instagram_response 

    

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)

    