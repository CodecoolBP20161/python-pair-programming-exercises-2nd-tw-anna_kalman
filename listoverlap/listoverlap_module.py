from random import randint

def random_list():
    list_name = []
    for i in range(1, randint(2, 10)):
        list_name.append(randint(1, 100))
    return list_name


def listoverlap(list1, list2):
    result_list = []
    main_list = list1 + list2
    for i in range(1, max(main_list)):
        if i in main_list:
            result_list.append(i)
    return result_list


def main():
    print (listoverlap(a,b))
    return

a = random_list()
b = random_list()
if __name__ == '__main__':
    main()
