import tkinter
from PIL import ImageTk, Image
from tkinter import LEFT, filedialog
from tkinter import messagebox
import cv2

def insert_img():
    print("Image")
    filename = filedialog.askopenfilename(title="open")
    img_show = Image.open(filename)
    img_show_tk = ImageTk.PhotoImage(img_show)
    panel = tkinter.Label(window, image=img_show_tk)
    panel.image = img_show_tk
    panel.pack(side= tkinter.RIGHT)
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    rows, cols , _ = img.shape
    #img = cv2.inread
    print(filename)
    print(rows)
    print(cols)
    print(img)

def insert_text():
    print("Text")
    filename = filedialog.askopenfilename(title="open")
    text = open(filename, "r")
    lines = text.read()
    text_box.insert(tkinter.END,lines)
    text_box.pack(side=tkinter.LEFT)

    print(lines)
   
def hide_text():
    print("ocultar mensaje");

def contact():
    messagebox.showinfo("How contact me", "liahutaislinn@ciencias.unam.mx")
    print("liahutaislinn@ciencias.unam.mx");

def about():
    messagebox.showinfo("About Program", "This program is a test")
    print("About")

def ocultar_procesar():
    result=textExample.get("1.0","end")
    result=result.rstrip()
    print(result)
    #print("liahutaislinn@ciencias.unam.mx");

def get():
    print("About");

def hide():
    print("Hide")

window = tkinter.Tk()
window.title('Esteganografía por el método LSB')
window.geometry("850x500")
#window.config(width=850, height=500)
window.resizable(width= True, height= True)
menubar = tkinter.Menu(window, background = "#000000", foreground="black" )
mode = tkinter.Menu(menubar)
# label1 = tkinter.Label(window, text="¡Otra etiqueta!")
# label1.config(fg="blue")

mode.add_command(label= "Hide", command=hide)
mode.add_command(label= "Get", command=get)
menubar.add_cascade(label="Mode", menu=mode)

help = tkinter.Menu(menubar)
# label1 = tkinter.Label(window, text="¡Otra etiqueta!")
# label1.config(fg="blue")

help.add_command(label= "About", command=about)
help.add_command(label= "Contact", command=contact)

# help.config(bg='#D9D8D7')
menubar.add_cascade(label="Help", menu=help)
window.config(menu=menubar)




btn_image = tkinter.Button(window, text="Abrir imagen",command=insert_img)
btn_image.pack(side=tkinter.RIGHT)
btn_image = tkinter.Button(window, text="Abrir texto",command=insert_text)
btn_image.pack(side=tkinter.LEFT)
# textExample=tkinter.Text(window, height=2, width=27)
# textExample.pack(side=tkinter.BOTTOM)
btn_image = tkinter.Button(window, text="Ocultar mensaje",command=ocultar_procesar)
btn_image.pack(side=tkinter.BOTTOM)
#input
textExample=tkinter.Text(window, height=1.5, width=29)
textExample.pack(side=tkinter.BOTTOM)
#---------------------
text_box =tkinter.Text(window, height=50, width=50)
# # textos y titulos
# titulo = tkinter.Label(window,text="Login de Usuario con Python",font=("Arial",24))
# titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
window.mainloop()