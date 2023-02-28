from Bruteforce import compute_bruteforce
from DnC import compute_DnC
from Randomizer import xyz_random_points
from Util import *
import tkinter
import tkinter.ttk
import time

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


class GUI3D:
    def __init__(self, root):
        self.root = root
        self.frame = tkinter.ttk.Frame(self.root)
        # init mpl figure
        self.figure = Figure(figsize=(4, 4), facecolor='white')
        self.axis = self.figure.add_subplot(projection="3d")
        self.points = []
        self.points_xyz = [[], [], []]

        # setup button
        self.make_button()
        self.position_button()

        # prepare canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.toolbar = NavigationToolbar2Tk(
            self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(y=423)
        self.canvas.get_tk_widget().place(x=0, y=0)
        self.canvas.draw()

        # for positioning debug
        self.debug_cursor()

    def make_button(self):
        # make generate button
        self.amountLabel = tkinter.Label(
            text="Points", font=("Poppins"), master=self.frame)
        self.amountForm = tkinter.Entry(
            background='#FAFAFA', font=("Poppins"), master=self.frame)
        self.limitLabel = tkinter.Label(
            text="Limit", font=("Poppins"), master=self.frame)
        self.limitForm = tkinter.Entry(
            background='#FAFAFA', font=("Poppins"), master=self.frame)
        self.generateButton = tkinter.Button(text="Generate", font=(
            "Poppins"), bg="#495464", fg="#FAFAFA", command=self.update_points, master=self.frame)

        # points
        self.pointsLabel = tkinter.Label(
            text="Points", font=("Poppins"), master=self.frame)
        self.pointsFrame = tkinter.Frame(self.root)
        self.pointsScrollbarY = tkinter.Scrollbar(self.pointsFrame)
        self.pointsScrollbarX = tkinter.Scrollbar(
            self.pointsFrame, orient="horizontal")
        self.pointsText = tkinter.Text(self.pointsFrame, height=30, width=30, wrap="none",
                                       yscrollcommand=self.pointsScrollbarY.set,
                                       xscrollcommand=self.pointsScrollbarX.set, font=(
                                           "Poppins"),
                                       background='#E8E8E8')
        self.pointsText.configure(state="disabled")
        self.pointsScrollbarY.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.pointsScrollbarX.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.pointsScrollbarY.config(command=self.pointsText.yview)
        self.pointsScrollbarX.config(command=self.pointsText.xview)
        self.pointsText.pack(side="left")

        # solve button
        self.bruteButton = tkinter.Button(text="BruteForce", font=(
            "Poppins"), bg="#495464", fg="#FAFAFA", command=self.start_bruteforce, master=self.frame)
        self.bruteCompare = tkinter.Label(text="Compare", master=self.frame)
        self.bruteTime = tkinter.Label(text="Time", master=self.frame)
        self.bruteCompareAnswer = tkinter.Label(self.frame)
        self.bruteTimeAnswer = tkinter.Label(self.frame)
        self.DnCButton = tkinter.Button(text="DnC", font=(
            "Poppins"), bg="#495464", fg="#FAFAFA", command=self.start_DnC, master=self.frame)
        self.DnCCompare = tkinter.Label(text="Compare", master=self.frame)
        self.DnCTime = tkinter.Label(text="Time", master=self.frame)
        self.DnCCompareAnswer = tkinter.Label(self.frame)
        self.DnCTimeAnswer = tkinter.Label(self.frame)
        self.closestAnswer = tkinter.Label(
            text="Closest Pair", master=self.frame)
        self.distLabel = tkinter.Label(text="Distance", master=self.frame)
        self.distLabelAnswer = tkinter.Label(self.frame)
        self.point1Label = tkinter.Label(text="Point 1", master=self.frame)
        self.point1LabelAnswer = tkinter.Label(self.frame)
        self.point2Label = tkinter.Label(text="Point 2", master=self.frame)
        self.point2LabelAnswer = tkinter.Label(self.frame)

        # error
        self.amountError = tkinter.Label(
            font=("Arial", 8), fg='red', master=self.frame)
        self.limitError = tkinter.Label(
            font=("Arial", 8), fg='red', master=self.frame)
        self.solveError = tkinter.Label(
            font=("Arial", 10), fg='red', master=self.frame)

    def position_button(self):
        # constant
        self.label_positionx = 400
        self.first_y = 0
        self.label_gap = 40
        self.form_positionx = 480

        self.solve_positionx = 15
        self.solve_y = 450
        self.solve_gapx = 130
        self.solve_gapy = 30
        self.dist_positionx = 215
        self.dist_gapy = 20
        self.text_gap = 70

        # input
        self.amountLabel.place(x=self.label_positionx, y=self.first_y)
        self.amountForm.place(x=self.form_positionx, y=self.first_y)
        self.limitLabel.place(x=self.label_positionx,
                              y=self.first_y + self.label_gap)
        self.limitForm.place(x=self.form_positionx,
                             y=self.first_y + self.label_gap)
        self.generateButton.place(x=585, y=self.first_y + 2*self.label_gap)

        # points
        self.pointsLabel.place(x=510, y=self.first_y + 3*self.label_gap)
        self.pointsFrame.place(x=self.label_positionx+2,
                               y=self.first_y + 4.5*self.label_gap)

        # solve
        self.bruteButton.place(x=self.solve_positionx, y=self.solve_y)
        self.bruteCompare.place(x=self.solve_positionx,
                                y=self.solve_y + 3*self.solve_gapy)
        self.bruteTime.place(x=self.solve_positionx,
                             y=self.solve_y + 4*self.solve_gapy)
        self.DnCButton.place(x=self.solve_positionx +
                             self.solve_gapx, y=self.solve_y)
        self.DnCCompare.place(
            x=self.solve_positionx + self.solve_gapx, y=self.solve_y + 3*self.solve_gapy)
        self.DnCTime.place(x=self.solve_positionx +
                           self.solve_gapx, y=self.solve_y + 4*self.solve_gapy)
        self.closestAnswer.place(x=self.dist_positionx, y=self.solve_y)
        self.distLabel.place(x=self.dist_positionx,
                             y=self.solve_y + self.dist_gapy)
        self.point1Label.place(x=self.dist_positionx,
                               y=self.solve_y + 2*self.dist_gapy)
        self.point2Label.place(x=self.dist_positionx,
                               y=self.solve_y + 3*self.dist_gapy)

    def update_points_text(self):
        self.reset_error()
        self.pointsText.configure(state="normal")
        self.pointsText.delete(1.0, tkinter.END)
        for point in self.points:
            self.pointsText.insert(tkinter.END, point_to_string(point) + "\n")
        self.pointsText.configure(state="disabled")

    def show_error(self, n_error="", limit_error="", solve_error=""):
        if n_error != "" or limit_error != "":
            self.amountError.config(text=n_error)
            self.limitError.config(text=limit_error)
        if solve_error != "":
            self.solveError.config(text=solve_error)

        self.amountError.place(x=self.label_positionx,
                               y=self.first_y + (self.label_gap)//2)
        self.limitError.place(x=self.label_positionx,
                              y=self.first_y + 3 * (self.label_gap)//2)
        self.solveError.place(x=self.solve_positionx + 7,
                              y=self.solve_y + self.solve_gapy+15)

    def reset_error(self):
        self.amountError.place_forget()
        self.limitError.place_forget()
        self.solveError.place_forget()

    def update_points(self):
        # get input
        n = self.amountForm.get()
        limit = self.limitForm.get()

        # validate
        n = validate_n(n)
        n_error = type(n) == str

        limit = validate_limit(limit)
        limit_error = type(limit) == str

        if n_error or limit_error:
            if not n_error:
                n = ""
            if not limit_error:
                limit = ""
            self.show_error(n_error=n, limit_error=limit)
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
        self.axis.scatter3D(
            self.points_xyz[0], self.points_xyz[1], self.points_xyz[2], color="red")
        self.canvas.draw()

    def update_answer(self, method, answer, execTime):
        if method == "Bruteforce":
            self.bruteCompareAnswer.place(
                x=self.solve_positionx + self.text_gap, y=self.solve_y + 3*self.solve_gapy)
            self.bruteCompareAnswer.config(text=answer[0])
            self.bruteTimeAnswer.place(
                x=self.solve_positionx + self.text_gap, y=self.solve_y + 4*self.solve_gapy)
            self.bruteTimeAnswer.config(text=f"{execTime*1000:0.2f} ms")
        else:
            self.DnCCompareAnswer.place(
                x=self.solve_positionx + self.solve_gapx + self.text_gap, y=self.solve_y + 3*self.solve_gapy)
            self.DnCCompareAnswer.config(text=answer[0])
            self.DnCTimeAnswer.place(
                x=self.solve_positionx + self.solve_gapx + self.text_gap, y=self.solve_y + 4*self.solve_gapy)
            self.DnCTimeAnswer.config(text=f"{execTime*1000:0.2f} ms")

        self.distLabelAnswer.place(
            x=self.dist_positionx + self.text_gap, y=self.solve_y + self.dist_gapy)
        self.distLabelAnswer.config(text=f"{answer[1]:0.2f}")
        self.point1LabelAnswer.place(
            x=self.dist_positionx + self.text_gap, y=self.solve_y + 2*self.dist_gapy)
        self.point1LabelAnswer.config(
            text=point_to_string(answer[2][0]))
        self.point2LabelAnswer.place(
            x=self.dist_positionx + self.text_gap, y=self.solve_y + 3*self.dist_gapy)
        self.point2LabelAnswer.config(
            text=point_to_string(answer[2][1]))
        self.update_plot_answer(answer[2][0], answer[2][1])
        
    def update_plot_answer(self, p1, p2):
        x = [p1[0], p2[0]]
        y = [p1[1], p2[1]]
        z = [p1[2], p2[2]]

        self.axis.remove()
        self.axis = self.figure.add_subplot(projection="3d")
        self.axis.scatter3D(
            self.points_xyz[0], self.points_xyz[1], self.points_xyz[2], color="red")
        self.axis.scatter3D(
            x, y, z, color="blue")
        self.axis.plot(x, y, z)
        self.canvas.draw()

    def flatten_xyz(self):
        x, y, z = self.points_xyz
        self.points = []
        for point in zip(x, y, z):
            self.points.append(point)

    def start_bruteforce(self):
        if len(self.points) == 0:
            self.show_error(solve_error="generate points before start")
            return
        start = time.time()
        answer = compute_bruteforce(self.points)
        print(answer)
        end = time.time()
        self.update_answer("Bruteforce", answer, end - start)

    def start_DnC(self):
        if len(self.points) == 0:
            self.show_error(solve_error="generate points before start")
            return
        start = time.time()
        answer = compute_DnC(self.points)
        print(answer)
        end = time.time()
        self.update_answer("DnC", answer, end - start)

    def debug_cursor(self):
        self.cursor_pos = tkinter.Label(self.frame)
        self.cursor_pos.place(x=650, y=700)
        self.frame.bind("<Motion>", lambda event: self.cursor_pos.configure(
            text=f"{event.x}, {event.y}"))

    def start(self):
        # run tkinter
        self.debug_cursor()
        tkinter.mainloop()


def make_root():
    # init tkinter
    frame = tkinter.Tk()
    frame.wm_title("Closest Pair Visualizer")
    frame.geometry("690x720")
    frame.resizable(False, False)
    return frame


if __name__ == "__main__":
    root = make_root()
    program = GUI3D(root)
    program.start()
