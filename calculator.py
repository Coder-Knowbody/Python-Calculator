num1 = input('First Number')
fltnum1 = float(num1)
arith = input('Arithmetic Sign')
num2 = input('Second Number')
fltnum2 = float(num2)
if arith == '+':
    print(fltnum1 + fltnum2)
elif arith == '-':
    print(fltnum1 - fltnum2)
elif arith == '*':
    print(fltnum1 * fltnum2)
elif arith == '/':
    print(fltnum1 / fltnum2)
else:
    print('Syntax error')