from sys import exit
import re


def main():
    s = input("Enter an identifier: ")
    s = s.strip()
    if s in ["False","def","if","raise","None","del","import","return","True","elif","in","try","and","else","is","while","as","except","lambda","with","assert","finally","nonlocal","yield","break","for","not","class","from","or","continue","global","pass"]:
        print("False")
    if re.match(r"(^[A-Za-z_]+)([A-Za-z_0-9]*$)", s):
        print(True)
    else:
        print(False)
    exit()


if __name__ == "__main__":
    main()