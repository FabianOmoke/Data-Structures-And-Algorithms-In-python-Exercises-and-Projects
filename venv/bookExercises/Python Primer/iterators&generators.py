# Generator Example

def fibonacci( ):
    a = 0
    b = 1
    while b<1000:          # keep going...
        yield a          # report value, a, during this pass # Automatically creates an iterator that can be fed to list
        future = a + b
        a = b            # this will be next value reported
        b = future       # and subsequently this


data = fibonacci()        # Our iterable automaticaly takes the values

for i in data:
    print(i)