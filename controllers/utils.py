import tempfile
import urllib
from typing import List
from PIL import Image

def write_bytes_to_tempPNG(png_bytes):
    temp_file = tempfile.NamedTemporaryFile(
        delete=True,
        suffix='.png',
    )
    temp_file.write(png_bytes)
    return temp_file

def download_photo(image_url, suffix=".png") -> tempfile:
        temp_file = tempfile.NamedTemporaryFile(delete=True, suffix=suffix)
        try:
            # Download the image from the URL
            urllib.request.urlretrieve(image_url, temp_file.name)
            print("Image downloaded successfully to:", temp_file.name)
        except Exception as e:
            print("Error occurred while downloading the image:", str(e))

        return temp_file

def delete_photos(tempfiles):
     for file in tempfiles:
          file.close()


def download_photos(image_urls: List[str]) -> List[tempfile.NamedTemporaryFile]:
    photo_tempfiles = []
    for url in image_urls:
        photo_tempfiles.append(
            download_photo(image_url=url)
        )
    return photo_tempfiles

def convert_to_jpgs(files: tempfile.NamedTemporaryFile):
    jpg_files = []
    for file in files:
        png_image = Image.open(file.name)
        jpg_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=True)
        png_image.convert('RGB').save(jpg_file.name, format='JPEG')
        file.close()

        jpg_files.append(jpg_file)

    return jpg_files

          