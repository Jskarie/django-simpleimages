import StringIO

import PIL
import pytest

from django.core.files.base import ContentFile


class Image:
    def __init__(self):
        self.dimensions = (10, 10)
        self.color = 'blue'
        self.name = 'image.jpg'

    @property
    def django_file(self):
        return ContentFile(self.image_file.getvalue())

    @property
    def image_file(self):
        # Create a file-like object to write thumb data (thumb data previously created
        # using PIL, and stored in variable 'thumb')
        image_io = StringIO.StringIO()
        self.pil_image.save(image_io, format='JPEG')
        image_io.seek(0)
        return image_io

    @property
    def pil_image(self):
        return PIL.Image.new('RGB', self.dimensions, self.color)


@pytest.fixture()
def image():
    return Image()
