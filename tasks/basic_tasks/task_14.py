def multiple():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    product = num1 + num2
    #Check
    if(product <= 1000):
        return product
    else:
        return num1 + num2
        
def main():
    multiple()
    print("The value is", multiple())
    
    