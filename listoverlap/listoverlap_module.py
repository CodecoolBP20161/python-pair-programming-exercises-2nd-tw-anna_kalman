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

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
if __name__ == '__main__':
    main()
