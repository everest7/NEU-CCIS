def main():
    strs = input("Enter a string: ") 
    strs = strs.lower()
    i = 0
    while (i < len(strs)):
        if(strs[i] == 'a' or strs[i] == 'e'or strs[i] == 'i'or strs[i] == 'o'or strs[i] == 'u'):
            strs = strs.replace(strs[i],strs[i].upper())
        i += 1
    print(strs)
main()