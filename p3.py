from sys import exit
import re


def main():
    p1 = input("Enter the first part of the string: ")
    p2 = input("Enter the second part of the string: ")
    p1 = p1.lstrip()
    p2 = p2.rstrip()
    if (re.match(r"^(\')([^\'\\]*((\\)(.){1})*)*(\\)$",p1) and re.match(r"^([^\'\\]*((\\)(.){1})*)*\'$",p2)) or (re.match(r"^(\")([^\"\\]*((\\)(.){1})*)*(\\)$",p1) and re.match(r"^([^\"\\]*((\\)(.){1})*)*\"$",p2)):
        print("True")
    else:
        print("False")
    exit()


if __name__ == "__main__":
    main()