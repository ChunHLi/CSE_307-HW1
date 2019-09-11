from sys import exit
import re


def main():
    s = input("Enter a number: ")
    s = s.strip()
    if re.match(r"^([-+]*)?[0-9]*\.([0-9]+)$",s) or re.match(r"^([-+]*)?[0-9]*(\.([0-9]+))?[eE][-+]?[0-9]+$",s):
        print("float")
    elif re.match(r"^-?[1-9][0-9]*$",s) or re.match(r"^0(b|B)[0-1]+$",s) or re.match(r"^0(o|O)[0-7]+$",s) or re.match(r"^0(x|X)([0-9]|[abcdefABCDEF])+$",s):
        print("int")
    else:
        print("None")
    exit()


if __name__ == "__main__":
    main()