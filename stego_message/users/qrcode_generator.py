import pyqrcode
import png
from datetime import date



def barcodeGenerator(uri):
    url = pyqrcode.create(uri)
    image_as_str = url.png_as_base64_str(scale=5)
    image_as_str = "data:image/png;base64,{}".format(image_as_str)
    # url.png('{}.png'.format(order_id), scale=4)
    print("Printing QR code")
    # print(url.terminal(quiet_zone=1))
    return image_as_str
