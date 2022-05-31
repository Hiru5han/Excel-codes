for idx in range(1, 16381):
    eq = f'=INDIRECT("Form1!",&ADDRESS(ROW(${idx}:${idx}),COLUMN($C:$C)))'
    print(eq)
