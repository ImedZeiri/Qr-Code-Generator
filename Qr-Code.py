import qrcode
import json

JsonFile = open("data.json", "r")
jsonContent = JsonFile.read()
resJson = json.loads(jsonContent)

qr = qrcode.QRCode(
        box_size=10,
        version=1,
        border=5)
qr.add_data(resJson)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

img.save('qrcode001.png')