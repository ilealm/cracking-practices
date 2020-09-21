# Given two ordered lists, return a list with all the elements sorted.


def join_two_lists(lst1, lst2):
    lst_result = []
    if not lst1 or not lst2 :
        return lst_result

    pointer_lst1 = 0
    pointer_lst2 = 0

    while pointer_lst1 < len(lst1) and pointer_lst2 < len(lst2):
        if lst1[pointer_lst1] < lst2[pointer_lst2]:
            lst_result.append(lst1[pointer_lst1])
            pointer_lst1 +=1
        else:
            lst_result.append(lst2[pointer_lst2])
            pointer_lst2 +=1

    while pointer_lst1 < len(lst1):
        lst_result.append(lst1[pointer_lst1])
        pointer_lst1 +=1

    while pointer_lst2 < len(lst2):
        lst_result.append(lst2[pointer_lst2])
        pointer_lst2 +=1

    return lst_result

if __name__ == "__main__":
    lst1 = [10,15, 20,25,30]
    lst2 = [1,3,5]
    print(join_two_lists(lst1, lst2))
