class Complexnumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self, other):
        return Complexnumber(self.real+other.real,self.imag+other.imag)

    def __sub__(self, other):
        return Complexnumber(self.real-other.real,self.imag-other.imag)

    def __mul__(self, other):
        real_part=(self.real*other.real)-(self.imag*other.imag)
        image_part=(self.real*other.imag)+(self.imag*other.real)
        return Complexnumber(real_part,image_part)

    def __str__(self):
        return f"{self.real}:{self.imag}i"

if __name__=="__main__":
    c1=Complexnumber(1,3)
    c2=Complexnumber(2,4)

    result_add=c1+c2
    print(f"Addition{result_add}")

    result_sub=c1-c2
    print(f"Subtraction{result_sub}")

    result_mul=c1*c2
    print(f"multiplication{result_mul}")



