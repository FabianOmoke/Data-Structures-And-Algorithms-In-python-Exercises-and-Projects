
def is_multiple(n,m):
    if m%n == 0:
        print(f"{m} is a multiple of {n}")
    else:
        print("They are not multiples")

print("SOLVING SIMPLE PROBLEMS")

firstNum = int(input("Enter the number whose multiple You'd like to Know: "))
secondNum = int(input("Enter the alleged Multiple: "))

is_multiple(secondNum,firstNum)

def isEven(m):
    if int(m) & 1 == 0:  #binary format 2 ** 0 =  1
        print("It is Even")
    else:
        print("Your number is odd")

number = int(input("Enter the number you wish to investigate: "))

isEven(number)

def minmax(data):
    max = 0
    min = 0
    for i in data:
        if i >= max:
            max = i
        else:
            min = i
    return (min, max)

print("\n The min-max ratings stand at: ", minmax([1]))

def sum_of_squares(data):
    list = []
    sum = 0
    for i in range(data+1):
        list.append(i)
    for k in list:
        sum += k**2
    return sum

def sum_of_squares_advanced(data):
    return sum([pow(x,2) for x in range (data+1)])

print("The sum of the squares", sum_of_squares_advanced(5))
