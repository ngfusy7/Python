def main():
    number = get_number()
    mew(3)

def get_number():
    while True:
        n = int(input("What's n: "))
        if n > 0:
            break
    return n       
def mew(n):
    for _ in range(n):
        print("meow")


main()