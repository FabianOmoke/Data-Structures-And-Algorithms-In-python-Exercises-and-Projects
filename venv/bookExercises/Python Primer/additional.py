## Conditional Expressions

n = int(input("Enter the number: "))

sign = "negative" if n<0 else "positive"

print(sign)

##List Comprehensions
squares = [k*k for k in range(100)]

liste= []

print(liste)

"""multiply all entries of numeric data list by a given factor"""
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
        print(data[j], end=",")





