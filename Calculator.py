from tkinter import *

def shw_scrn(event):
    global scrn
    txt = event.widget.cget("text")
    if txt == "=":
        if scrn.get().isdigit():
            value = int(scrn.get())

        else:
            try:
                value = eval(scrn.get())
            except EXCEPTION as e:
                value = "Error"
                # print(e)

        scrn.set(value)
        scrn_lbl.update()

    elif txt == "C":
        scrn_lbl.update()
        scrn.set("")

    else:
        scrn.set(scrn.get()+str(txt))
        scrn_lbl.update()

root=Tk()
width = 330
height = 618
root.geometry(f"{width}x{height}")
root.maxsize(width,height)
root.minsize(width,height)
root.wm_iconbitmap("calculator.ico")
root.title("Calculator")
root.configure(bg= "dark gray")

scrn = StringVar()
scrn.set("")
scrn_lbl= Entry(root , textvariable = scrn , font = ('lucida 35 bold') , relief = SUNKEN , bg="white" , state = "readonly")
scrn_lbl.pack(padx = 15 , pady = 10 , fill = BOTH)

no_list = [7,8,9]
no_list1 = [4,5,6]
no_list2 = [1,2,3,]
no_list3 = [0,'.',"+"]
no_list4 = ['-','*','/']
no_list5 = ['%','C','=']

f = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f.pack(fill = BOTH)
f1.pack(fill = BOTH)
f2.pack(fill = BOTH)
f3.pack(fill = BOTH)
f4.pack(fill = BOTH)
f5.pack(fill = BOTH)

for no in range(len(no_list)):
    scrn.set("")
    scrn_lbl.update()
    btn= Button(f , text = no_list[no] , font = "lucida 20 bold" , padx =15 )
    btn.pack(side = LEFT , padx =20, pady = 15, fill = BOTH)
    root.bind("<Button-1>" , shw_scrn)

for no in range(len(no_list1)):
    scrn.set("")
    scrn_lbl.update()
    btn= Button(f1 , text = no_list1[no] , font = "lucida 20 bold" , padx =15)
    btn.pack(side = LEFT , padx =20, pady = 15, fill = BOTH)
    root.bind("<Button-1>", shw_scrn)

for no in range(len(no_list2)):
    scrn.set("")
    scrn_lbl.update()
    btn = Button(f2, text=no_list2[no], font="lucida 20 bold", padx=15)
    btn.pack(side=LEFT, padx=20, pady=15, fill = BOTH)
    root.bind("<Button-1>", shw_scrn)

for no in range(len(no_list3)):
    scrn.set("")
    scrn_lbl.update()
    btn = Button(f3, text=no_list3[no], font="lucida 22 bold", padx=15)
    btn.pack(side=LEFT, padx=20, pady=15, fill = BOTH)
    root.bind("<Button-1>", shw_scrn)

for no in range(len(no_list4)):
    scrn.set("")
    scrn_lbl.update()
    btn = Button(f4, text=no_list4[no], font="lucida 25 bold", padx=15)
    btn.pack(side=LEFT, padx=20, pady=15, fill = BOTH)
    root.bind("<Button-1>", shw_scrn)

for no in range(len(no_list5)):
    scrn.set("")
    scrn_lbl.update()
    btn = Button(f5, text=no_list5[no], font="lucida 19 bold", padx=15)
    btn.pack(side=LEFT, padx=20, pady=15, fill = BOTH)
    root.bind("<Button-1>", shw_scrn)

root.mainloop()