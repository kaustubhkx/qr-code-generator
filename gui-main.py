from tkinter import *
from tkinter.filedialog import askopenfile
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
    generated_successfully = Label(text="QR Code Generated Successfully")
get_url = Entry(root)
get_url.pack()
enter_url = Label(text="Enter Name of the file").pack()
save_url = Entry(root)
save_url.pack()
def delete():
    get_url.delete(0, END)
    save_url.delete(0, END)
button = Button(text="Generate QR Code", command=save).pack()
button_clear = Button(text="Clear", command=delete)
button_clear.pack()
root.mainloop()
