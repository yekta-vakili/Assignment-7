print("Please select the desired operation:")
print("1-sum\n2-Submission\n3-Multiplication")
select = int(input())


class Calculations:
    def __init__(self, x):
        self.complex_number = x

    def su_m(self, B):
        output = self.complex_number + B.complex_number
        print(output)

    def sub(self, B):
        output = self.complex_number - B.complex_number
        print(output)

    def multi(self, B):
        output = self.complex_number * B.complex_number
        print(output)


"""
real = int(input("!!Please enter the real section!!\n"))
unreal = int(input("!!Please enter an imaginary section!!\n"))
comp = complex(real,unreal)
print(comp)
real2 = int(input("!!Please enter the real section!!\n"))
unreal2 = int(input("!!Please enter an imaginary section!!\n"))
comp2 = complex(real2,unreal2)
print(comp2)
t1 = Calculations(comp)
t2=Calculations(comp2)
"""
i = 0
q = ['-', '-']
while i <= 1:
    real = int(input("!!Please enter the real section!!\n"))
    unreal = int(input("!!Please enter an imaginary section!!\n"))
    comp = complex(real, unreal)
    q[i] = comp
    i += 1

t1 = Calculations(q[0])
t2 = Calculations(q[1])


if select == 1:
    out = t1.su_m(t2)
if select == 2:
    out = t1.sub(t2)
if select == 3:
    out = t1.multi(t2)
