from tkinter import *
from tkinter import filedialog
import qrcode

root = Tk()
root.geometry("1000x500")
root.title("QR Code Generator")
QR_Code_Generator = Label(root, text="QR Code Generator", font="Ariel").pack(side=TOP)
Enter_URL = Label(text="Enter URL").pack()

get_url = Entry(root, width=50)
get_url.pack()

def save():
    global generated_successfully
    file = filedialog.asksaveasfilename(filetypes=[('JPEG files','*.jpeg')],defaultextension='.png')
    a=str(get_url.get())
    img = qrcode.make(a)
    img.save(file)
    generated_successfully = Label(text="QR Code Generated Successfully")
    generated_successfully.pack()


def delete():
    get_url.delete(0, END)
    generated_successfully.destroy()

button = Button(text="Generate QR Code", command=save).pack()
button_clear = Button(text="Clear", command=delete)
button_clear.pack()
root.mainloop()
