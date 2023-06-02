from instagrapi import Client

class InstagramController:
    def __init__(self, username, password, verification_code=""):
        self.bot = Client()
        self.bot.login(
            username=username,
            password=password,
            verification_code=verification_code
        )    

    def make_post(self, file_paths,  caption):
            return self.bot.album_upload(
                file_paths, 
                caption=caption
            )