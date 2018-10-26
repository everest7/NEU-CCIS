def main():
    file_name = input("Enter the file name: ")
    try:  # Exception handling
        file1 = open(file_name, "r")  # open file in read mode
        word_count, char_count, letter_number = 0, 0, 0
        for line in file1.readlines():
            line = line.rstrip('\n')  # strip the new line character
            word_list = line.split(' ')  # return a list
            for word in word_list:
                char_count += len(word)  # count the character in a word
                for char in word:
                    # determine if the character is letter or number
                    if (char.isalpha() or char.isnumeric()):
                        letter_number += 1  # count the letters and numbers
            word_count += len(word_list)  # count the words in every line
        # Print result
        print("Words:", word_count)
        print("Characters:", char_count)
        print("Letters and number:", letter_number)
    except FileNotFoundError:
        print("Unable to open", file_name)
    return


main()
