import qrcode

get_url_input = str(input("Enter the URL:- "))

img = qrcode.make(get_url_input)

save_name = str(input("Enter the saving name:- "))

img.save(save_name + ".jpg")

print("QR Code Generated")
