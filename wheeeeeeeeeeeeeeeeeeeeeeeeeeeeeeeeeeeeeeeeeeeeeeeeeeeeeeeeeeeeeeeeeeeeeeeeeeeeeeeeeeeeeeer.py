from tkinter import*
from PIL import ImageTk,Image
import os 
from tkinter import filedialog
root = Tk()
root.geometry("1000x1000")
lab = Label(root)


def fun():
    global pointy
    global img2
    pointy =  filedialog.askopenfilename(title = "Open Image File",filetypes = [("Image Files","*.jpg *.png *.jpeg *.gif")])
    img = Image.open(pointy)
    img2 = ImageTk.PhotoImage(img)
    lab['image'] = img2
    img2.close()
    
    
def r():
    global pointy
    im = Image.open(pointy)
    img2.ImageTk.PhotoImage(im.rotate(180))
    lab['image'] = img2
    img2.close()

B2 = Button(root,text = "Work",command = fun)

w2 =  Button(root,text = "Worek",command = r)

B2.pack()
lab.pack()
w2.pack()
w2.place(relx = 0.1, rely = 0.1)
root.mainloop()