import random as rnd 

def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    favorite = input("Please enter one of your hobbies: ")

    # Generating user name
    first_letter = first_name[0]
    first_seven = (last_name + 'append')[0:7] # Add character and select the seven-character piece
    random_number1 = rnd.randint(0,99) # Generate random number between 0 and 99
    user_name = (first_letter + first_seven + str(random_number1)).lower() # Get the user name in its lower case

    # Generating password1
    random_number2 = rnd.randint(0,99)
    password1 = (first_name + str(random_number2) + last_name).lower() # Concatenate first name, random number and last name
    for i in range(len(password1)): # Replacing special character
        if password1[i] == 'a':
            password1 = password1.replace(password1[i],'@')
        elif password1[i] == 'o':
            password1 = password1.replace(password1[i],'0')
        elif password1[i] == 'l':
            password1 = password1.replace(password1[i],'1')
        elif password1[i] == 's':
            password1 = password1.replace(password1[i],'$')

    # Generating password2
    # Get first character of first name, last name and favorite word, in its lower case,
    # and their last character, in its upper case
    password2 = first_name[0].lower() + first_name[len(first_name) - 1].upper() + \
                last_name[0].lower() + last_name[len(last_name) - 1].upper() + \
                favorite[0].lower() + favorite[len(favorite) - 1].upper()

    # Generating password3
    # Get random-length portion of first name, last name and favorite word. Then 
    # concatenate them together
    random_length1 = rnd.randint(1,len(first_name) - 1) 
    random_length2 = rnd.randint(1,len(last_name) - 1)
    random_length3 = rnd.randint(1,len(favorite) - 1)
    password3 = first_name[0:random_length1] + favorite[0:random_length3] + \
                last_name[0:random_length2]

    # Print the result
    print("Thanks",first_name,"your user name is",user_name)
    print("Here are three suggested passwords for you to consider:")
    print("Password 1:",password1)
    print("Password 2:",password2)
    print("Password 3:",password3)

main()