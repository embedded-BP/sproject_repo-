# File modifie by:
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("STM32 USB Monitor")
root.geometry("1250x760")

# Menu
menubar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New Session",        accelerator="Ctrl+N")
file_menu.add_command(label="Open Log...",         accelerator="Ctrl+O")
file_menu.add_separator()
file_menu.add_command(label="Save Log...",         accelerator="Ctrl+S")
file_menu.add_command(label="Export as CSV...")
file_menu.add_command(label="Export as PDF...")
file_menu.add_separator()
file_menu.add_command(label="Print...",            accelerator="Ctrl+P")
file_menu.add_separator()
file_menu.add_command(label="Exit",                accelerator="Alt+F4")
menubar.add_cascade(label="File", menu=file_menu)

# Connection menu
conn_menu = tk.Menu(menubar, tearoff=0)
conn_menu.add_command(label="Refresh Ports",       accelerator="F5")
conn_menu.add_separator()
conn_menu.add_command(label="Connect",             accelerator="F7")
conn_menu.add_command(label="Disconnect",          accelerator="F8")
conn_menu.add_separator()
conn_menu.add_command(label="Port Settings...")
conn_menu.add_command(label="Auto-Connect on Startup")
menubar.add_cascade(label="Connection", menu=conn_menu)

# View menu
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_checkbutton(label="Show Toolbar")
view_menu.add_checkbutton(label="Show Status Bar")
view_menu.add_checkbutton(label="Show Raw Data Panel")
view_menu.add_separator()
view_menu.add_checkbutton(label="Show Voltage Graph")
view_menu.add_checkbutton(label="Show Current Graph")
view_menu.add_checkbutton(label="Show Power Graph")
view_menu.add_separator()
zoom_menu = tk.Menu(view_menu, tearoff=0)
zoom_menu.add_command(label="Zoom In",             accelerator="Ctrl++")
zoom_menu.add_command(label="Zoom Out",            accelerator="Ctrl+-")
zoom_menu.add_command(label="Reset Zoom",          accelerator="Ctrl+0")
view_menu.add_cascade(label="Zoom", menu=zoom_menu)
view_menu.add_separator()
view_menu.add_command(label="Light Theme")
view_menu.add_command(label="Dark Theme")
menubar.add_cascade(label="View", menu=view_menu)

# Settings menu
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="COM Port Settings...")
settings_menu.add_command(label="Baud Rate Settings...")
settings_menu.add_separator()
settings_menu.add_command(label="Display Settings...")
settings_menu.add_command(label="Graph Settings...")
settings_menu.add_separator()
settings_menu.add_command(label="Calibration Settings...")
settings_menu.add_separator()
settings_menu.add_command(label="Preferences...",  accelerator="Ctrl+,")
menubar.add_cascade(label="Settings", menu=settings_menu)

# Tools menu
tools_menu = tk.Menu(menubar, tearoff=0)
tools_menu.add_command(label="Data Logger")
tools_menu.add_command(label="Serial Monitor...")
tools_menu.add_command(label="Statistics & Analysis...")
tools_menu.add_separator()
tools_menu.add_command(label="Clear All Data",     accelerator="Ctrl+Del")
tools_menu.add_command(label="Reset Graphs")
tools_menu.add_separator()
tools_menu.add_command(label="Run Diagnostics...")
menubar.add_cascade(label="Tools", menu=tools_menu)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Documentation",       accelerator="F1")
help_menu.add_command(label="Keyboard Shortcuts...")
help_menu.add_separator()
help_menu.add_command(label="Check for Updates...")
help_menu.add_command(label="Report a Bug...")
help_menu.add_separator()
help_menu.add_command(label="About STM32 USB Monitor")
menubar.add_cascade(label="Help", menu=help_menu)

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
