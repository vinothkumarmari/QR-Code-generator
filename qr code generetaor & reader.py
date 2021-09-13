import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Name = input("Enter your name : ")
phone = int(input("Enter your ph.no : "))
# li = [Name, age]

qr = pyqrcode.create(phone)
qr.png("Vi.png", scale=8)

d = decode(Image.open("Vinoth.png"))
print(d[0].data.decode("Ascii"))