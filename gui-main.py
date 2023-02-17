from tkinter import *
from tkinter import filedialog
import qrcode
from tkinter import messagebox 

root = Tk()
root.geometry("1000x500")
root.title("QR Code Generator")
QR_Code_Generator = Label(root, text="QR Code Generator", font="Ariel").pack(side=TOP)
Enter_URL = Label(text="Enter URL").pack()

get_url = Entry(root, width=50)
get_url.pack()

 
def save():
    if not get_url.get():
        messagebox.showerror("Empty field", "This field cannot be left blank")
    else:
        try:
            global generated_successfully   
            file = filedialog.asksaveasfilename(filetypes=[('JPEG files','*.jpeg')],defaultextension='.png')   
            a=str(get_url.get())   
            img = qrcode.make(a)   
            img.save(file) 
            generated_successfully = Label(text="QR Code Generated Successfully")    
            generated_successfully.pack()
        except:
            messagebox.showerror("Invalid URL","Enter a valid URL")


def delete():
    try:
        get_url.delete(0, END)
        generated_successfully.destroy()
    except:
        pass

button = Button(text="Generate QR Code", command=save).pack()
button_clear = Button(text="Clear", command=delete)
button_clear.pack()
root.mainloop()
