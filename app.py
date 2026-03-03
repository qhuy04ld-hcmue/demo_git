def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))
