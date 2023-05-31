from instabot import Bot
import urllib.request
import tempfile

class InstagramController:
    def __init__(self, username, password):
        self.bot = Bot()
        self.bot.login(
            username=username,
            password=password
        )

    def download_photo(self, image_url) -> tempfile:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        try:
            # Download the image from the URL
            urllib.request.urlretrieve(image_url, temp_file.name)
            print("Image downloaded successfully to:", temp_file.name)
        except Exception as e:
            print("Error occurred while downloading the image:", str(e))

        return temp_file
    

    def make_post(self, url,  caption):
            temp_file = self.download_photo(url)
            return self.bot.upload_photo(
                temp_file.name, 
                caption=caption
            )