from datetime import datetime
from sys import exit


def main():
    s = input("Enter a date in the format MM/DD/YYYY: ")
    s = s.strip()
    try:
        date_c = datetime.strptime(s, '%m/%d/%Y')
        print(date_c.strftime('%A, %B %d, %Y'))
    except:
        print("Incorrect format!")
    exit()


if __name__ == "__main__":
    main()