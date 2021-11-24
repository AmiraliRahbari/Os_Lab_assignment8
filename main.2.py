class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))


r = int(input("Enter real num 1 : "))
e = int(input("Enter imag num 1 : "))
num1 = Complex(r, e)
print("num 1 : ", num1.real, ' + ', num1.imag, 'j', end='')
r = int(input("\nEnter real num 2 : "))
e = int(input("Enter imag num 2 : "))
num2 = Complex(r, e)
print("num 2 : ", num2.real, ' + ', num2.imag, 'j', end='')
print('\nSum : ', (num1 + num2).real, ' + ', (num1 + num2).imag, 'j', end='')
print('\nSub : ', (num1 - num2).real, ' + ', (num1 - num2).imag, 'j', end='')
print('\nMul : ', (num1 * num2).real, ' + ', (num1 * num2).imag, 'j', end='')
