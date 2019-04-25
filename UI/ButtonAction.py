import random
from generategrid.generate_grid import Sudo

class ButtonAction:
    def __init__(self):
        self.mat = []
    def insert(self, text):
        s = Sudo()
        s.generate()
        self.mat = s.matrix
        for k in range(9):
            i = random.randint(0, 8)
            l = i
            for m in range(random.randint(1,6)):
                if(m == 0):
                    text[k*9+l].AppendText(str(s.matrix[k][l]))
                    l = random.randint(0, 8)
                    continue
                if(l == i):
                    continue
                else:
                    text[k*9+l].AppendText(str(s.matrix[k][l]))
                    l = random.randint(0, 8)

    def check(self, text, label):
        for m in range(9):
            for n in range(9):
                if(str(self.mat[m][n]) != text[m*9+n].GetValue()):
                    string = "Wrong Answer!!! Row: " + str(m) + "Col: " + str(n)
                    label.SetLabel(string)
                    return
        label.SetLabel("Correct Answer!!!")

    def show(self, text):
        for k in range(len(text)):
            text[k].Remove(0,1)
        for m in range(9):
            for n in range(9):
                text[m*9+n].AppendText(str(self.mat[m][n]))
