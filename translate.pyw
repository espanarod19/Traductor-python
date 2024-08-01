from tkinter import *
from googletrans import Translator
import tkinter.messagebox
from tkinter import ttk


def translate_to_english(spanish_text): 
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(spanish_text, src='es', dest='en')    
    return translated_text.text

 
def checkInput():
    trans = buscador_entry.get()
    if not trans:
        tkinter.messagebox.showinfo("DUMB!!", "No Escribiste nada PERRUUUU!!!")
    else:
        #button.config(command=lambda: buscador_entry.delete(0, END))
        translated_text = translate_to_english(trans)
        tkinter.messagebox.showinfo("You Entered", translated_text)
        #label.configure(text=translated_text)
        #button.config(command=lambda: buscador_entry.delete(0, END))
        
        

master = Tk()
master.title("TRADUCTOR")
master.geometry("350x50+400+300")
master.config(bg="#6FAFE7")
button = Button(master, text="Ingles", command=checkInput, height=1, width=10)
button.pack(side='right')
text = Label(master, text="Que tradusco:").pack(side='left', padx=5)
buscador_entry = Entry(master, bd=3)
buscador_entry.pack(side='left', padx=4)

        
   





master.mainloop()
