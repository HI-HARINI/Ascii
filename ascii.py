name="Harini"
for letter in name:
    print(ord(letter))
    

from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("Ascii Convertor")

inputbox=Entry(root)
inputbox.place(relx=0.5, rely=0.1,anchor=CENTER)
label1=Label(root,text="The Ascii # is: " )
label1.place(relx=0.5, rely=0.3,anchor=CENTER)
label2=Label(root,text="Encrypted Value " )
label2.place(relx=0.5, rely=0.5,anchor=CENTER)
label3=Label(root,text="Encrypted Text " )
label3.place(relx=0.5, rely=0.6,anchor=CENTER)
def asciicon():
    inputvalue=inputbox.get()
    for letter in inputvalue:
        label1["text"]+=str(ord(letter))+" "
        ascii=int(ord(letter))
        encrypted=ascii-1
        label3["text"]+=str(chr(encrypted))
button1=Button(root,text="Generate Ascii",command=asciicon)
button1.place(relx=0.5, rely=0.4,anchor=CENTER)

root.mainloop()