# put your python code here
num1,num2,num3 = abs(int(input())),\
                 abs(int(input())),\
                 abs(int(input()))

num1,num2, num3 = (num1//2) + (num1 % 2 > 0),\
                  (num2//2) + (num2 % 2 > 0),\
                  (num3//2) + (num3 % 2 > 0)
s = num1 + num2 + num3

print(s)