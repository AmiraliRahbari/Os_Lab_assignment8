def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n


class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator must not be zero.")

        self.num = n
        self.denom = d

    def Add(self, other):
        return Fraction.simplify(Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom))

    def Sub(self, other):
        return Fraction.simplify(Fraction(self.num * other.denom - self.denom * other.num, self.denom * other.denom))

    def Mul(self, other):
        return Fraction.simplify(Fraction(self.num * other.num, self.denom * other.denom))

    def Div(self, other):
        return Fraction.simplify(Fraction(self.num * other.denom, self.denom * other.num))

    def __str__(self):
        return f"{self.num} / {self.denom}"

    def simplify(self):
        fact = gcd(self.num, self.denom)
        return Fraction(self.num // fact, self.denom // fact)

def main():
    f1 = Fraction(4, 2)
    f2 = Fraction(2, 2)
    f3 = Fraction.Add(f1,f2)
    f4 = Fraction.Sub(f1,f2)
    f5 = Fraction.Mul(f1,f2)
    f6 = Fraction.Div(f1,f2)
    print(f3.simplify())
    print(f4.simplify())
    print(f5.simplify())
    print(f6.simplify())


if __name__ == '__main__':
    main()