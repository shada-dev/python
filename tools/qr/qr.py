import pyqrcode
content = str(input("Enter the message you want: "))
qr = pyqrcode.create(content)
qr.save("qr.jpg")
print("=> image saved ✓ ")
