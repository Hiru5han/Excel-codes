for idx in range(1, 2001):
    x='=INDIRECT('
    y='"Form1!"'
    eq = f',&ADDRESS(ROW(${idx}:${idx}),COLUMN($C:$C)))'
    print(x+y+eq)