import openai
import os

class ImageGenerationController:
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
    
    def generate_variations(self, file, n=3):
        response = openai.Image.create_variation(
            image=file,
            n=n,
        )
        image_urls = []
        for obj in response.data:
            image_urls.append(
                obj.url
            )
        return image_urls