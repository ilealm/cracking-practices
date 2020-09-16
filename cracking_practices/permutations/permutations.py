def permutations0(array, intercalate_array=[], permuts=[]):

    if len(array) == 1:
        perm = []
        # do the permutations for this array. I needd +1 BC i whant to permutate at the end also,
        for p in range(0, len(intercalate_array) + 1):
            this_perm = intercalate_array[0:p] + array + intercalate_array[p:]
            perm.append(this_perm)
            print(this_perm)
            # clear intercalate_array for the next cycle
        intercalate_array.clear()
        if len(perm) == 3:
            permuts.append(perm)
            print("-----next round....")
        return

    for i in range(0, len(array)):
        print(i, "the intecalate array is", intercalate_array)
        # intercalate_array=[]
        # this is the one that moves the pointer into the main array. If the array is a sub array, i'n not really goint to need id
        intercalate_array.append(array[i])
        sub_array = array[0:i] + array[i + 1 :]  # is array minus array[i]

        # if len(sub_array) > 1:
        permutations(sub_array, intercalate_array, permuts)
        # if len(intercal
        # ate) > 0 :
        # intercalate_array the value of reduced (which is only 1 element) on each position of intercalate_array, and append to permuts
        # perm = []
        # for p in range(0, len(intercalate_array)+1):
        #     perm = intercalate_array[0:p] + sub_array + intercalate_array[p:]
        #     permuts.append(perm)

        #     print(perm)

    intercalate_array.clear()

    # clear intercalate_array for the next cycle
    # intercalate_array.clear()
    # print("--------------------- end ", i)

    # print(permuts)
    return permuts


# nop, only works with 3 elements
def permutations2(array):
    return_list = []
    for i in range(0, len(array)):
        x = []
        base = array[i]
        sub_array = array[0:i] + array[i + 1 :]

        sub_array.insert(0, base)
        return_list.append(sub_array)

        sub_array = array[0:i] + array[i + 1 :]
        sub_array.reverse()
        sub_array.insert(0, base)
        return_list.append(sub_array)

        # print(x)
        # print(base+sub_array.sort())
        # x.append(sub_array.sort())

    return return_list


# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1 :]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
# data = list('123')
# data = [1,2,3]
# for p in permutation(data):
#     print(p)

# based on the explanation of
# https://www.youtube.com/watch?v=KukNnoN-SoY


def permutations(array, permutation=[], perms=[]):
    if array == []:
        print(permutation)
        perms.append(permutation.copy())
        # permutation.clear()
        return

    for i in range(0, len(array)):
        permutation.append(array[i])
        sub_array = array[:i] + array[i + 1 :]
        permutations(sub_array, permutation,  perms)
        permutation.pop()  # I was missing this!!!
        
    return perms


if __name__ == "__main__":
    array = [1, 2, 3]
    print(permutations(array))
