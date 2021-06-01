import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=15,
    border=5
)

data = "https://linktr.ee/X_vamp"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="grey")
img.save("test.png")
