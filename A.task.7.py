# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task7 problem A

import copy
import string
class Polynomial:
    def __init__(self, coeffs):
        for i in range(len(coeffs)):
            if not(isinstance(coeffs[i], int)):
                coeffs[i] = int(coeffs[i])
        self.coeffs = coeffs[::-1]
    def __str__(self):
        res = ""
        list1 = copy.copy(self.coeffs)
        for i in range(len(list1)):
            if i == 0:
                list1[i] = str(abs(list1[i]))
            elif i == 1:
                list1[i] = "%dx" % (abs(list1[i]))
            else:
                list1[i] = "%dx^%d" %(abs(list1[i]), i)
##        return str(list1)
        first = 0
        for i in range(len(self.coeffs[::-1])):
            if i == 0 and self.coeffs[::-1][i] > 0:
                res += list1[::-1][i]
            elif i == 0 and self.coeffs[::-1][i] < 0:
                res += '-'+str(list1[::-1][i])
            else:
                if self.coeffs[::-1][i] > 0:
                    res += ' + '+ list1[::-1][i]
                elif self.coeffs[::-1][i] < 0:
                    res += ' - '+ list1[::-1][i]
        return res
    def __add__(self, poly):
        init_self = copy.copy(self.coeffs)
        init_poly = copy.copy(poly.coeffs)
        maxi = max(len(self.coeffs), len(poly.coeffs))
        for i in range(len(self.coeffs), 9):
            self.coeffs += [0]
        for i in range(len(poly.coeffs), 9):
            poly.coeffs += [0]
        l_n = []
        l = []
        for i in range(len(self.coeffs)):
            l.append(self.coeffs[i] + poly.coeffs[i])
        for i in range(maxi):
            l_n.append(l[i])
        self.coeffs = copy.copy(init_self)
        poly.coeffs = copy.copy(init_poly)
        return Polynomial(l_n[::-1])
    def __sub__(self, poly):
        init_self = copy.copy(self.coeffs)
        init_poly = copy.copy(poly.coeffs)
        maxi = max(len(self.coeffs), len(poly.coeffs))
        for i in range(len(self.coeffs), 9):
            self.coeffs += [0]
        for i in range(len(poly.coeffs), 9):
            poly.coeffs += [0]
        l_n = []
        l = []
        for i in range(len(self.coeffs)):
            l.append(self.coeffs[i] - poly.coeffs[i])
        for i in range(maxi):
            l_n.append(l[i])
        self.coeffs = copy.copy(init_self)
        poly.coeffs = copy.copy(init_poly)
        return Polynomial(l_n[::-1])
    def calculate(self, x):
        res = 0
        for i in range(len(self.coeffs)):
            res += self.coeffs[i]*(x**i)
        return res
    def __mul__(self, poly):
        new_list = []
        voc = {}
        maxi = (len(self.coeffs)+len(poly.coeffs))-1
        for i in range(maxi):
            voc[i] = 0
        for i in range(len(self.coeffs)):
            for j in range(len(poly.coeffs)):
                temp = self.coeffs[i] * poly.coeffs[j]
                voc[i+j] += temp
        for i in range(maxi):
            new_list.append(voc[i])
        return Polynomial(new_list[::-1])
##a = Polynomial([2, 1])
##b = Polynomial([1, 1])
##print a
##print a+b
##print a-b
##print b
##print b.calculate(2)
##print a*b

print "Polynimial A"
sizeA = input("Enter size: ")
coeffsA = raw_input("Enter coefficients: ")
print "Polynomial A is: "
A = Polynomial(string.split(coeffsA))
print A

print "Polynimial B"
sizeB = input("Enter size: ")
coeffsB = raw_input("Enter coefficients: ")
print "Polynomial B is: "
B = Polynomial(string.split(coeffsB))
print B

print "Sum of A and B is (A+B): "
print A+B

print "A subtract B is (A-B): "
print A-B

print "Multiplication of A and B is (A*B):"
print A*B

c = input("Enter number: ")
print "Equation B with x=2: "
print B.calculate(c)

