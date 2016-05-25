import datetime


def years(age):
    today = str(datetime.date.today())[:4]
    return int(today) + 100 - int(age)


def main():
    name = input("name?")
    age = input("how old R U?")
    print ("%s, you'll be 100 in %i" % (name, years(age)))



if __name__ == '__main__':
    main()
