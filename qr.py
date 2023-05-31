"""do pip install qrcode"""
import qrcode


def whatsapp_qr_code ():
    print("Okay then, input the number..."
    "Don't forget the country code!")
    data = input(': ').replace("+", "").replace(" ","")
    qr_code = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2,)
    qr_code.add_data('https://wa.me/'+data)
    qr_code.make(fit=True)
    image = qr_code.make_image(fill_color="white", back_color="black")
    print("your qr code has been made, give it a name")
    qr_name = str(input()) + '.png'
    image.save(qr_name)
    print('your qr code has been made')


def make_qr_code ():
    print("type what you want to convert to a qr code")
    usr_txt = input(": ")
    qr_code = qrcode.QRCode(
        version=1,
        box_size=8,
        border=2)
    qr_code.add_data(usr_txt)
    qr_code.make(fit=True)
    image = qr_code.make_image(fill_color="white", back_color="black")
    print("one qr code coming right up!")
    print("...")
    print("...")
    print("All done, you can now give it a name:")
    qr_name = str(input(" ")) + '.png'
    print('\ncomplete!')
    image.save(qr_name)





print("What would you like to do?\n"
"1. Generate qr code for a whatsapp number\n"
"2. store data in a qr code")
print("")

usr_choice = int(input("choose a number from above: "))
if usr_choice == 1:
    whatsapp_qr_code()
else:
    make_qr_code()
