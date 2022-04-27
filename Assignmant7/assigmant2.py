print("Please select the desired operation:")
print("1-sum\n2-Submission\n3-Multiplication")
select = int(input())


class Calculations:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def su_m(self, A):
        out1 = self.real+A.real
        out2 = (self.imag+A.imag)*1j
        print(out1, "+", out2)

    def sub(self, B):
        out1 = self.real-B.real
        out2 = self.imag-B.imag
        out3 = out2*1j
        if out2 >= 0:
            print(out1, "+", out3)
        else:
            print(out1, out3)

    def multi(self, C):
        out1 = self.real*C.real
        out2 = self.real*(C.imag*1j)
        out3 = (self.imag*1j)*C.real
        out4 = (self.imag)*(C.imag)*-1
        out5 = out2 + out3
        out6 = out4 + out1
        print(out6, "+", out5)


i = 0
q = ['-', '-']
p = ['-', '-']
while i <= 1:
    real = int(input("!!Please enter the real section!!\n"))
    unreal = int(input("!!Please enter an imaginary section!!\n"))
    q[i] = real
    p[i] = unreal
    i += 1
print(q)
print(p)

t1 = Calculations(q[0], p[0])
t2 = Calculations(q[1], p[1])

if select == 1:
    out = t1.su_m(t2)
if select == 2:
    out = t1.sub(t2)
if select == 3:
    out = t1.multi(t2)
