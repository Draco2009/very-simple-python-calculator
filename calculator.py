# desicion
print("what is the operation? ")
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')
print('give 1 as input for addition, 2 for subtraction and vise versa')
# input
operator = input()
if operator == '1':
    num1 = input('enter the first number: ')
    num2 = input('enter the second number: ')
    print(float(num1) + float(num2))

elif operator == '2':
    num1 = input('enter the first number: ')
    num2 = input('enter the second number: ')
    print(float(num1) - float(num2))
    
elif operator == '3':
    num1 = input('enter the first number: ')
    num2 = input('enter the second number: ')
    print(float(num1) * float(num2))
    
elif operator == '4':
    num1 = input('enter the first number: ')
    num2 = input('enter the second number: ')
    print(float(num1) / float(num2))
    
print('mission completed successfully *dies*')
