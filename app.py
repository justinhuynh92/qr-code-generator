#install all the libraries needed
import qrcode

#create a function that collects a text and converts it to a qr code
def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    #save the qr code as an image
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")

#run the function
url = input("Enter the url: ")
generate_qrcode(url)
