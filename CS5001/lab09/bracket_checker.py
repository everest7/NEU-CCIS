from bracket_match import BracketMatch


def main():
    bm = BracketMatch()
    line = input("Input a line:\n")
    if bm.brackets_match(line):
        print("Brackets match")
    else:
        print("Brackets do not match")

main()
