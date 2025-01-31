#generate pythagoren triplets of lenght <=30

for i in range(1,30):
    for j in range(i,31):
        c=(i**2+j**2)**0.5
        if c.is_integer() and c<=30:
            print('(',i,',',j,',',int(c),',',")")
