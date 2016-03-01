# STUDENT: Shynggys Sabyrkhan
# GROUP: 1EN04C
# TASK: Task7 problem B

import copy
class ComplexNumber:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def __str__(self):
        a = copy.copy(self.a)
        b = copy.copy(self.b)
        if self.b < 0:
            self.b = abs(self.b)
            if self.a != 0 and self.b != 1:
                return "%d - %di" % (self.a, self.b)
            elif self.a != 0 and self.b == 1:
                return "%d - i" % (self.a)
            elif self.a == 0 and self.b != 1:
                return "%di" % (self.b)
            elif self.a == 0 and self.b == 1:
                return "i"
        elif self.b > 0:
            if self.a != 0 and self.b != 0:
                if self.b != 1:
                    return "%d + %di" % (self.a, abs(self.b))
                else:
                    return "%d + i" % (self.a)
            elif self.a != 0 and self.b == 0:
                return "%d" % (self.a)
            elif self.a == 0 and self.b != 0:
                if self.b != 1:
                    return "%di" % (self.b)
                elif self.b == 1:
                    return "i"
        else:
            if self.a == 0:
                return "0"
            else:
                return str(self.a)
    def __add__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(self.a+other.a, self.b+other.b)
    __radd__ = __add__
    def __sub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(self.a-other.a, self.b-other.b)
    def __rsub__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber(other.a-self.a, other.b-self.b)
    def __mul__(self, other):
        if isinstance(other, int):
            other = ComplexNumber(other)
        return ComplexNumber((self.a*other.a)-(self.b*other.b), (self.a*other.b)+(self.b * other.a))
    __rmul__ = __mul__
    def __neg__(self):
        return ComplexNumber(-self.a, -self.b)

print "Number A"
try:
    a = input("Enter real part: ")
except SyntaxError, m:
    print "No real part"
try:
    b = input("Enter imaginary part: ")
except SyntaxError, m:
    print "No imaginary part"
print "Complex A number is:"
try:
    a
except NameError, m:
    a = 0
try:
    b
except NameError, m:
    b = 0
A = ComplexNumber(a, b)
print A

print "Number B"
try:
    c = input("Enter real part: ")
except SyntaxError, m:
    print "No real part"
try:
    d = input("Enter imaginary part: ")
except SyntaxError, m:
    print "No imaginary part"
print "Complex B number is:"
try:
    c
except NameError, m:
    c = 0
try:
    d
except NameError, m:
    d = 0
B = ComplexNumber(c, d)
print B

print "Number C"
try:
    e = input("Enter real part: ")
except SyntaxError, m:
    print "No real part"
try:
    f = input("Enter imaginary part: ")
except SyntaxError, m:
    print "No imaginary part"
print "Complex C number is:"
try:
    e
except NameError, m:
    e = 0
try:
    f
except NameError, m:
    f = 0
C = ComplexNumber(e, f)
print C

print "Sum of A and B is: "
print A+B
print "Sum of A and C is: "
print A+C
print "A subtract B is: "
print 0-B
print "Multiplication of A and B is: "
print A*B


