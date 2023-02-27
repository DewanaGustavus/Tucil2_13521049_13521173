from GUI3D import GUI3D
import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.title("Tab Widget")
tabControl = tkinter.ttk.Notebook(root)

gui1 = GUI3D(tabControl)
tab1 = gui1.frame
tab2 = tkinter.ttk.Frame(tabControl)
root.geometry("750x750")
root.resizable(False, False)

tabControl.add(tab1, text ='3D')
tabControl.add(tab2, text ='n-D')
tabControl.pack(expand = 1, fill ="both")

root.mainloop()