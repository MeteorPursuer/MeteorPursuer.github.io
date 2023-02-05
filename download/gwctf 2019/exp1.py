from z3 import *
x = [0] * 6
for i in range(6):
    x[i] = Int('x[' + str(i) + ']')

s = Solver()
s.add(x[0]==0xDF48EF7E)
s.add(x[5]==0x84F30420)
s.add(x[1]==0x20CAACF4)
s.add(x[2]-x[3]==0x84A236FF)
s.add(x[3]+x[4]==0xFA6CB703)
s.add(x[2]-x[4]==0x42D731A8)

s.check()
print(s.model())