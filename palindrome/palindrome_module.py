def palindrome(str):
    is_palindrome = str.replace(" ", "")
    if is_palindrome == is_palindrome[::-1]:
        return "It's a palindrome"
    else:
        return "It's not"


def main():
    str = input("type your str!")
    print (palindrome(str))



if __name__ == '__main__':
    main()
