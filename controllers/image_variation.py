import openai
import os

class ImageVariationController:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def generate(self, prompt, n=3):
        response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return [image_url]