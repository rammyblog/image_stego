

import base64
from django.core.files.base import ContentFile


def convert64toImage(image_data, username):
    format, imgstr = image_data.split(';base64,')
    print("format", format)
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr))
    file_name = "{}.".format(username) + ext

    return file_name
