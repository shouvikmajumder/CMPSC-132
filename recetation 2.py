class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i**2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        if self._imag<0:
           return f"{self._real} - {abs(self._imag)}i"

    def conjugate(self):
        return Complex(self._real,-1*self._imag)

    def __mul__(self,other):
        if isinstance(other, Complex):
            real_part = (self._real*other._real) - (self._imag*other._imag)
            imag_part = (self._real*other._imag) + (self._imag*other._real)
            return Complex(real_part,imag_part)
        else:
            return Complex(self._real*other,self._imag*other)
            
    def __rmul__(self,other):
        return Complex(self._real*other,self._imag*other)



    __repr__ = __str__
