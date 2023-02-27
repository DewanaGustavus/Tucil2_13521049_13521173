from Bruteforce import compute_bruteforce
from DnC import compute_DnC
from Randomizer import xyz_random_points
from Validator import *
import tkinter
import numpy as np
import time

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from mpl_toolkits import mplot3d  

class GUI3D:
    def __init__(self):
        # init tkinter
        self.frame = tkinter.Tk()
        self.frame.wm_title("Closest Pair Visualizer")
        self.frame.geometry("720x720")
        self.frame.resizable(False, False)

        # init mpl figure 
        self.figure = Figure(figsize = (5, 5), facecolor='yellow')
        self.axis = self.figure.add_subplot(projection="3d")
        self.points = []
        self.points_xyz = [[], [], []]
        
        # setup button
        self.make_button()    
        self.position_button()
        
        # prepare canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.draw()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=20, y=450)
        self.canvas.get_tk_widget().place(x=0, y=0)
        
    def make_button(self):
        # make generate button
        self.amountLabel = tkinter.Label(text="Points")
        self.amountForm = tkinter.Entry(background='red')
        self.limitLabel = tkinter.Label(text="Limit")
        self.limitForm = tkinter.Entry(background='red')
        self.generateButton = tkinter.Button(text="Generate", command=self.update_points)
        
        # points
        self.pointsLabel = tkinter.Label(text="Points")
        self.pointsFrame = tkinter.Frame(self.frame)
        self.pointsScrollbarY = tkinter.Scrollbar(self.pointsFrame)
        self.pointsScrollbarX = tkinter.Scrollbar(self.pointsFrame, orient="horizontal")
        self.pointsText = tkinter.Text(self.pointsFrame, height=30, width=20, wrap="none",
                                       yscrollcommand=self.pointsScrollbarY.set, 
                                       xscrollcommand=self.pointsScrollbarX.set, 
                                       background='green')
        self.pointsText.configure(state="disabled")
        self.pointsScrollbarY.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.pointsScrollbarX.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.pointsScrollbarY.config(command=self.pointsText.yview)
        self.pointsScrollbarX.config(command=self.pointsText.xview)
        self.pointsText.pack(side="left")
        
        # solve button
        self.bruteButton = tkinter.Button(text="Bruteforce", command=self.start_bruteforce)
        self.bruteCompare = tkinter.Label(text="Compare")
        self.bruteTime = tkinter.Label(text="Time")
        self.bruteCompareAnswer = tkinter.Label()
        self.bruteTimeAnswer = tkinter.Label()
        self.DnCButton = tkinter.Button(text="DnC", command=self.start_DnC)
        self.DnCCompare = tkinter.Label(text="Compare")
        self.DnCTime = tkinter.Label(text="Time")
        self.DnCCompareAnswer = tkinter.Label()
        self.DnCTimeAnswer = tkinter.Label()
        self.closestAnswer = tkinter.Label(text="Closest Pair")
        self.distLabel = tkinter.Label(text="Distance")
        self.distLabelAnswer = tkinter.Label()
        self.point1Label = tkinter.Label(text="Point 1")
        self.point1LabelAnswer = tkinter.Label()
        self.point2Label = tkinter.Label(text="Point 2")
        self.point2LabelAnswer = tkinter.Label()

    def position_button(self):
        # constant
        self.label_positionx = 520
        self.first_y = 10
        self.label_gap = 40
        self.form_positionx = 560
        
        self.solve_positionx = 50
        self.solve_y = 510
        self.solve_gapx = 130
        self.solve_gapy = 30
        self.dist_positionx = 300
        self.dist_gapy = 20
        self.text_gap = 70
        
        # input
        self.amountLabel.place(x=self.label_positionx, y=self.first_y)
        self.amountForm.place(x=self.form_positionx, y=self.first_y)
        
        self.limitLabel.place(x=self.label_positionx, y=self.first_y + self.label_gap)
        self.limitForm.place(x=self.form_positionx, y=self.first_y + self.label_gap)
        
        self.generateButton.place(x=self.form_positionx, y=self.first_y + 2*self.label_gap)

        # points
        self.pointsLabel.place(x=self.form_positionx, y=self.first_y + 3*self.label_gap)
        self.pointsFrame.place(x=self.label_positionx, y=self.first_y + 4*self.label_gap)

        # solve
        self.bruteButton.place(x=self.solve_positionx, y=self.solve_y)
        self.bruteCompare.place(x=self.solve_positionx, y=self.solve_y + 2*self.solve_gapy)
        self.bruteTime.place(x=self.solve_positionx, y=self.solve_y + 3*self.solve_gapy)
        self.DnCButton.place(x=self.solve_positionx + self.solve_gapx, y=self.solve_y)
        self.DnCCompare.place(x=self.solve_positionx + self.solve_gapx, y=self.solve_y + 2*self.solve_gapy)
        self.DnCTime.place(x=self.solve_positionx + self.solve_gapx, y=self.solve_y + 3*self.solve_gapy)
        self.closestAnswer.place(x=self.dist_positionx, y=self.solve_y)
        self.distLabel.place(x=self.dist_positionx, y=self.solve_y + self.dist_gapy)
        self.point1Label.place(x=self.dist_positionx, y=self.solve_y + 2*self.dist_gapy)
        self.point2Label.place(x=self.dist_positionx, y=self.solve_y + 3*self.dist_gapy)

    def update_points_text(self):
        self.pointsText.configure(state="normal")
        self.pointsText.delete(1.0, tkinter.END)
        for point in self.points:
            self.pointsText.insert(tkinter.END, self.point_to_string(point) + "\n")
        self.pointsText.configure(state="disabled")

    def update_points(self):
        # get input
        n = self.amountForm.get()
        limit = self.limitForm.get()

        # validate
        n = validate_n(n)
        n_error = type(n) == str
        if n_error:
            print("n")

        limit = validate_limit(limit)
        limit_error = type(limit) == str
        if limit_error:
            print("limit")
            
        if n_error or limit_error:
            return
            
        # process
        self.points_xyz = xyz_random_points(n, limit)
        self.flatten_xyz()
        self.update_plot()
        self.forget_answer()
        self.update_points_text()
    
    def forget_answer(self):
        self.bruteCompareAnswer.place_forget()
        self.bruteTimeAnswer.place_forget()
        self.DnCCompareAnswer.place_forget()
        self.DnCTimeAnswer.place_forget()
        self.distLabelAnswer.place_forget()
        self.point1LabelAnswer.place_forget()
        self.point2LabelAnswer.place_forget()
    
    def update_plot(self):
        # points visualization
        self.axis.remove()
        self.axis = self.figure.add_subplot(projection="3d")
        self.axis.scatter3D(self.points_xyz[0], self.points_xyz[1], self.points_xyz[2], color="red")
        self.canvas.draw()

    def update_answer(self, method, answer, execTime):
        if method == "Bruteforce":
            self.bruteCompareAnswer.place(x=self.solve_positionx + self.text_gap, y=self.solve_y + 2*self.solve_gapy)
            self.bruteCompareAnswer.config(text=answer[0])
            self.bruteTimeAnswer.place(x=self.solve_positionx + self.text_gap, y=self.solve_y + 3*self.solve_gapy)
            self.bruteTimeAnswer.config(text=f"{execTime*1000:0.2f} ms")
        else:
            self.DnCCompareAnswer.place(x=self.solve_positionx + self.solve_gapx + self.text_gap, y=self.solve_y + 2*self.solve_gapy)
            self.DnCCompareAnswer.config(text=answer[0])
            self.DnCTimeAnswer.place(x=self.solve_positionx + self.solve_gapx + self.text_gap, y=self.solve_y + 3*self.solve_gapy)
            self.DnCTimeAnswer.config(text=f"{execTime*1000:0.2f} ms")

        self.distLabelAnswer.place(x=self.dist_positionx + self.text_gap, y=self.solve_y + self.dist_gapy)
        self.distLabelAnswer.config(text=f"{answer[1]:0.2f}")
        self.point1LabelAnswer.place(x=self.dist_positionx + self.text_gap, y=self.solve_y + 2*self.dist_gapy)
        self.point1LabelAnswer.config(text=self.point_to_string(self.points[answer[2][0]]))
        self.point2LabelAnswer.place(x=self.dist_positionx + self.text_gap, y=self.solve_y + 3*self.dist_gapy)
        self.point2LabelAnswer.config(text=self.point_to_string(self.points[answer[2][1]]))

    def point_to_string(self, point):
        string = "("
        for xyz in point:
            string += f"{xyz:0.2f}, "
        string = string[:-2] + ")"
        return string       

    def flatten_xyz(self):
        x, y, z = self.points_xyz
        self.points = []
        for point in zip(x, y, z):
            self.points.append(point)

    def start_bruteforce(self):
        if len(self.points) == 0:
            print("generate points before start")
            return
        start = time.time()
        answer = compute_bruteforce(self.points)
        end = time.time()
        self.update_answer("Bruteforce", answer, end - start)
            
    def start_DnC(self):
        if len(self.points) == 0:
            print("generate points before start")
            return
        start = time.time()
        answer = compute_DnC(self.points)
        end = time.time()
        self.update_answer("DnC", answer, end - start)

    def debug_cursor(self):
        self.cursor_pos = tkinter.Label(self.frame)
        self.cursor_pos.place(x=650,y=700)
        self.frame.bind("<Motion>", lambda event: self.cursor_pos.configure(text=f"{event.x}, {event.y}"))

    def start(self):
        # run tkinter
        self.debug_cursor()
        tkinter.mainloop()

if __name__ == "__main__":
    program = GUI3D()
    program.start()