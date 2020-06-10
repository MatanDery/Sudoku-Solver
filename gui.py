from tkinter import *
from tkinter.messagebox import showinfo
from Sudoku_solver import rec_brute


class Ui():
    def __init__(self, main_window):
        self.entry_list = []
        self.var_list = []
        main_window.wm_title("Users Locker")
        for y in range(9):
            for x in range(9):
                self.var = StringVar()
                self.entry_list.append( Entry(textvariable=self.var, width = 2))
                self.entry_list[-1].grid(row=y+y//3, column=x+x//3)
                self.var_list.append(self.var)

        for i in range(3, 9, 4):
            for j in range(11):
                self.sep = Label(text='---', )
                self.sep2 = Label(text='|', )
                self.sep.grid(row = i, column = j)
                self.sep2.grid(row = j, column = i)

        solve_button = Button(main_window, text='SOLVE', command=self.solve,)
        solve_button.grid(row=15, column=15)

    def popup_error(self):
        showinfo('err', 'only enter 0-9')

    def unsolve_error(self):
        showinfo('err', 'unsolveable_error')

    def init_bord(self):
        bord = []
        for i in range(9):
            bord.append([])
            for j in range(9):
                bord[i].append(0)
        return bord

    def input_bord(self):
        bord = self.init_bord()

        for val in range(len(self.var_list)):
            row = val // 9
            if self.var_list[val].get() != '':
                try:
                    bord[row][val % 9] = int(self.var_list[val].get())
                    if not 0 < bord[row][val % 9] < 10:
                        raise ValueError
                except ValueError :
                    self.popup_error()
        return bord

    def output_bord(self,bord):
        for val in range(len(self.var_list)):
            row = val // 9
            self.var_list[val].set(bord[row][val % 9])


    def solve(self):
        bord = self.input_bord()
        fin, bord = rec_brute(bord)
        if fin == False:
            self.unsolve_error()
        self.output_bord(bord)


main_window = Tk()
Ui(main_window)
main_window.mainloop()
