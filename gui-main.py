from tkinter import *
import qrcode
root = Tk()
root.geometry("1000x500")
root.title("QR Code Generator")
QR_Code_Generator = Label(root, text="QR Code Generator", font="Ariel").pack(side=TOP)
Enter_URL = Label(text="Enter URL").pack()
def save():
    a=str(get_url.get())
    img = qrcode.make(a)
    img.save(save_url.get() +".jpg")
    print("QR Code Generated")
get_url = Entry(root)
get_url.pack()
enter_url = Label(text="Enter Name of the file").pack()
save_url = Entry(root)
save_url.pack()
button = Button(text="Generate QR Code", command=save).pack()

root.mainloop()
