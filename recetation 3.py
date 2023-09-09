class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i**2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i


    def conjugate(self):
        return Complex(self._real,-1*(self._imag))

    def __mul__(self,other):
        if isinstance(other, Complex):
            real_part = (self._real*other._real) - (self._imag*other._imag)
            imag_part = (self._real*other._imag) + (self._imag*other._real)
            ans = Complex(real_part,imag_part)
            return ans
        else:
            ans = Complex(self._real*other,self._imag*other)
            return ans
    def __rmul__(self,other):
        ans = Complex(self._real*other,self._imag*other)
        return ans

    
    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        else:
           return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__



class Real(Complex):
    def init(self,value):
        super().init(value,0)

    def mul(self,other):
        if isinstance(self,Real) and isinstance(other,Real):
            real_part = (self._realother._real)
            ans = Real(real_part)
            return ans
        elif isinstance(other,Complex):
            return other.mul(self)
        else:
            ans = Real(self._real*other)
            return ans

    def eq(self,other):
        if isinstance(self,Real) and isinstance(other,Real):
            return True
        else:
            return False

    def int(self):
        return int(self._real)

    def float(self):
        return float(self._real)