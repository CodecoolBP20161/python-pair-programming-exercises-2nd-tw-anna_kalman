from random import randint

def random_list():
    list_name = []
    for i in range(1, randint(2, 10)):
        list_name.append(randint(1, 100))
    return list_name

def listoverlap(list1, list2):
    result_list = (sorted(list(set(a) | set(b))))
    return result_list

def main():
    print (listoverlap(a,b))
    return

a = random_list()
b = random_list()
if __name__ == '__main__':
    print (a)
    print (b)
    main()
