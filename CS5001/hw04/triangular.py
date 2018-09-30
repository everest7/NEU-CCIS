import sys

def main():
    tri_num = int(sys.argv[1])
    sum = 0
    for i in range (1, tri_num + 1):
        sum += i # Triangular number is the sum of values between 1 and the input number
    print("Current file name:",sys.argv[0])
    print("The triangular number of the input number is",sum)
main()