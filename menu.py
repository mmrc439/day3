print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Exit')
print('Enter your selection:',end='')
x=input()

if x=='1':
    print('you have selected addition')
elif x=='2':
    print('you have selected subtraction')
elif x=='3':
    print('you have selected multiplication')
elif x=='4':
    print('you have selected division')
elif x=='5':
    print('exit')
else:
    print('invalid selection')