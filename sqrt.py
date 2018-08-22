# Caution: Code written in python 3
'''This is a program which calculates the square root of a number by using
Newton's method. This program accepts floating point inputs as well.'''
import math

class sqrt:
    def __init__(self,x):
        self.x = x
    def nearest_sqrt(self):
        self.perfect_square = False
        for i in range(math.floor(self.x)):
            if i**2 > self.x:
                y_1 = i
                x_1_1 = i**2
                break
            elif i**2<self.x:
                y_2 = i
                x_1_2 = i**2

            elif float(i**2) == self.x:
                 self.perfect_square = True

        if self.perfect_square == False:
            if self.x-x_1_2 < x_1_1-self.x:
                self.x_1 = x_1_2
                self.y = y_2
            elif self.x-x_1_2 > x_1_2-self.x:
                self.x_1 = x_1_1
                self.y = y_1
        else:
            self.sqrt = i-1

    def sqrt(self):
        square_root.nearest_sqrt()
        if self.perfect_square == False:
            del_x = self.x - self.x_1
            del_y = del_x / (2*self.y)
            return self.y+del_y
        else:
            return self.sqrt

print("This programs gets a number as an input and outpus its square root as the output. Decimals are allowed")
x = float(input("Enter the number"))
square_root = sqrt(x)
result = square_root.sqrt()
print("The square root of %.3f is %.2f using Newton's method." % (x,result))
