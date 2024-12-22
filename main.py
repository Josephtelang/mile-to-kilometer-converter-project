from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=80,height=80)
window.config(padx=20,pady=20)

def calculate():
    km = round(float(input.get())*1.60)
    new_text = km 
    my_label.config(text=new_text)
    

my_label = Label(text= 0)   
my_label.grid(row=1,column=1)

new_label = Label(text="Miles")
new_label.grid(row=0,column=2)

label2 = Label(text="Km")
label2.grid(row=1,column=2)

label3 = Label(text="is equal to")
label3.grid(row=1,column=0)

button = Button(text="Calculate",command=calculate)  
button.grid(row=2,column=1)
 
input = Entry(width= 10)
input.grid(row=0,column=1)

window.mainloop()