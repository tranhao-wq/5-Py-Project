import qrcode

data = "https://www.clcoding.com/"
img = qrcode.make(data)
img.save("qr.png") 