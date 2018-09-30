import sys

def main():
    num = int(sys.argv[1])
    counter = 0
    f1 = 0 # The first item of fabonacci sequence is 0
    f2 = 1 # The second item of fabonacci sequence is 1
    if num == 1:
        print(f1)
    elif num == 2:
        print(f1,f2)
    else:
        while counter < num:
            print(f1,end=" ")
            n = f1 + f2
            f1 = f2
            f2 = n
            counter += 1
main()