
# Professional STM32 USB Monitor UI (template)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("STM32 USB Power Monitor")
root.geometry("1100x700")
root.configure(bg="#20242b")

style = ttk.Style()
style.theme_use("clam")

top = tk.Frame(root,bg="#2c313c",height=60)
top.pack(fill="x")
tk.Label(top,text="STM32 USB POWER MONITOR",bg="#2c313c",fg="white",
         font=("Segoe UI",22,"bold")).pack(pady=10)

ctrl = tk.Frame(root,bg="#20242b")
ctrl.pack(fill="x",padx=10,pady=10)
ttk.Label(ctrl,text="COM Port").grid(row=0,column=0,padx=5)
port=ttk.Combobox(ctrl,values=["COM1","COM2","COM3","COM4","COM5"],width=10)
port.grid(row=0,column=1)
ttk.Button(ctrl,text="Refresh").grid(row=0,column=2,padx=5)
ttk.Button(ctrl,text="Connect").grid(row=0,column=3,padx=5)
ttk.Button(ctrl,text="Disconnect").grid(row=0,column=4,padx=5)

cards=tk.Frame(root,bg="#20242b")
cards.pack(fill="x",padx=20,pady=10)

def card(parent,title,value):
    f=tk.Frame(parent,bg="#313743",bd=2,relief="groove",width=450,height=180)
    f.pack(side="left",expand=True,fill="both",padx=10)
    f.pack_propagate(False)
    tk.Label(f,text=title,font=("Segoe UI",18,"bold"),bg="#313743",fg="white").pack(pady=15)
    lbl=tk.Label(f,text=value,font=("Consolas",40,"bold"),bg="#313743",fg="#00ff99")
    lbl.pack(expand=True)
    return lbl

vlabel=card(cards,"Voltage","0.00 V")
ilabel=card(cards,"Current","0.00 A")

graphs=tk.Frame(root,bg="#20242b")
graphs.pack(fill="both",expand=True,padx=20,pady=10)
for title in ("Voltage Trend","Current Trend"):
    f=tk.LabelFrame(graphs,text=title,bg="#313743",fg="white")
    f.pack(fill="both",expand=True,pady=8)
    c=tk.Canvas(f,bg="black",height=180)
    c.pack(fill="both",expand=True,padx=5,pady=5)
    c.create_text(250,90,text="Live Graph Area",fill="lime",font=("Segoe UI",16))

bottom=tk.Frame(root,bg="#2c313c")
bottom.pack(fill="x",side="bottom")
raw=tk.StringVar(value="Waiting for USB data...")
status=tk.StringVar(value="Disconnected")
tk.Label(bottom,text="Raw Data:",bg="#2c313c",fg="white").pack(anchor="w",padx=10)
tk.Label(bottom,textvariable=raw,bg="#2c313c",fg="cyan").pack(anchor="w",padx=10)
tk.Label(bottom,textvariable=status,bg="#2c313c",fg="orange").pack(anchor="e",padx=10)

root.mainloop()
