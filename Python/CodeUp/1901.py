n = int(input())

def print_num(n):
    if n != 1:
        print_num(n-1)
    print(n)
    

print_num(n)