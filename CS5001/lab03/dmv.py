import random as rnd

def main():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    name = input("Please enter your first, middle, and last name:")
    dob = input("Enter date of birth (MM/DD/YY):")
    print("-------------------------------------")
    print("Washington Driver License")
    license_number = rnd.randint(1000000,9999999)
    whole_name = name.split(' ')
    LN = whole_name[len(whole_name) - 1]
    FN = name[:len(name) - len(LN)]
    DOB = dob.split("/")
    print("DL",license_number)
    print("LN",LN)
    print("FN",FN)
    print("DOB",dob)
    print("EXP",DOB[0]+'/'+DOB[1]+'/2021')
    print("-------------------------------------")
main()