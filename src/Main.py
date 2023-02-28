from GUI3D import GUI3D
from GUInD import GUInD
import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.title("Closest Pair Visualizer")
tabControl = tkinter.ttk.Notebook(root)

gui1 = GUI3D(tabControl)
tab1 = gui1.frame

gui2 = GUInD(tabControl)
tab2 = gui2.frame

root.geometry("750x750")
root.resizable(False, False)

tabControl.add(tab1, text ='3D')
tabControl.add(tab2, text ='n-D')
tabControl.pack(expand = 1, fill ="both")

root.mainloop()