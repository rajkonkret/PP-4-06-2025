import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Kurs")

        self.label = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label3 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label4 = tkinter.Label(self.main_window, text="Python")

        self.label.pack(side="left")
        self.label2.pack(side="right")
        self.label3.pack(side="top")
        self.label4.pack(side=tkinter.BOTTOM)

        tkinter.mainloop()


my_gui = MyGui()
