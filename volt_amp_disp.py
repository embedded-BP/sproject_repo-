
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("STM32 USB Monitor")
root.geometry("1250x760")

# Menu
menubar=tk.Menu(root)
for name in ("File","Connection","View","Settings","Tools","Help"):
    m=tk.Menu(menubar,tearoff=0)
    if name=="Connection":
        m.add_command(label="Refresh Ports")
        m.add_command(label="Connect")
        m.add_command(label="Disconnect")
    menubar.add_cascade(label=name,menu=m)
root.config(menu=menubar)

top=ttk.Frame(root,padding=8)
top.pack(fill="x")

ttk.Label(top,text="COM Port").grid(row=0,column=0,padx=4)
ports=ttk.Combobox(top,values=["COM1","COM2","COM3","COM4","COM5"],width=10,state="readonly")
ports.current(4)
ports.grid(row=0,column=1)

ttk.Label(top,text="Baud").grid(row=0,column=2,padx=4)
baud=ttk.Combobox(top,values=["9600","19200","57600","115200"],width=10,state="readonly")
baud.current(3)
baud.grid(row=0,column=3)

ttk.Button(top,text="Refresh").grid(row=0,column=4,padx=5)
ttk.Button(top,text="Connect").grid(row=0,column=5,padx=5)
ttk.Button(top,text="Disconnect").grid(row=0,column=6,padx=5)

status=tk.StringVar(value="Disconnected")
runtime=tk.StringVar(value="Runtime : 00:00:00")
ttk.Label(top,textvariable=status).grid(row=0,column=7,padx=20)
ttk.Label(top,textvariable=runtime).grid(row=0,column=8,padx=10)

cards=ttk.Frame(root,padding=10);cards.pack()
for i,(t,v) in enumerate([("Voltage","0.00 V"),("Current","0.00 A"),("Power","0.00 W")]):
    f=tk.LabelFrame(cards,text=t,width=350,height=150)
    f.grid(row=0,column=i,padx=10)
    f.grid_propagate(False)
    ttk.Label(f,text=v,font=("Consolas",28,"bold")).place(relx=.5,rely=.5,anchor="center")

graphs=ttk.Frame(root,padding=10);graphs.pack()
for i,n in enumerate(["Voltage","Current","Power"]):
    lf=tk.LabelFrame(graphs,text=n+" Graph")
    lf.grid(row=0,column=i,padx=10)
    c=tk.Canvas(lf,width=250,height=250,bg="white")
    c.pack()
    for x in range(0,251,25): c.create_line(x,0,x,250,fill="#ddd")
    for y in range(0,251,25): c.create_line(0,y,250,y,fill="#ddd")

bottom=ttk.Frame(root,padding=8);bottom.pack(fill="x",side="bottom")
raw=tk.StringVar(value="Raw Data : Waiting...")
ttk.Label(bottom,textvariable=raw).pack(anchor="w")
ttk.Label(bottom,text="Device Status").pack(anchor="w")
root.mainloop()
