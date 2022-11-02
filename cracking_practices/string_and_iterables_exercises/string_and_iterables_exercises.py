# class StringsExersices:
#     def __init__(self):
#         self.smalll_sentence = "This is a small sentence"


from ast import Delete


class ListExersices:
    def __init__(self) -> None:
        self.small_list_a = ["10", "20", "30", "40", "50"]
        self.small_list_b = ["60", "70", "80", "90", "100"]

    def get_all_items_one_list(self):
        return self.small_list_a[:]

    def get_first_item_list(self):
        # ! the LAST position is NOT returned
        return self.small_list_a[0:1]

    def get_last_item_list(self):
        return self.small_list_a[-1:]

    def get_first_3_items(self):
        #! Last item is NOT in the list
        result = self.small_list_a[:3]
        return result

    def get_middle_items(self):
        # ! -1 BC the last item DOESN'T APPEAR!
        return self.small_list_a[1:-1]

    def get_all_but_last(self):
        return self.small_list_a[:-1]

    def get_both_lists_in_new_one(self):
        # small_list_a and small_list_b remain the same
        new_list = self.small_list_a + self.small_list_b
        return new_list

    def add_list_b_to_a(self):
        self.small_list_a += self.small_list_b
        return self.small_list_a

    def get_last_half(self):
        return self.small_list_a[5:]

    def get_odd_items(self):
        return self.small_list_a[::2]

    def get_odd_items_from_end(self):
        return self.small_list_a[::-2]

    def get_reversed_list_a(self):
        # this doesn't affect the list
        return self.small_list_a[::-1]

    def get_num_items(self):
        return len(self.small_list_a)

    def get_sixth_item(self):
        return self.small_list_a[7 - 1]

    def remove_sixth_element(self):
        del self.small_list_a[6 - 1]
        return self.small_list_a

    def upd_first_element(self):
        self.small_list_a[1 - 1] = "A"
        return self.small_list_a

    def add_item_at_end(self):
        new_item = "B"
        self.small_list_a.append(new_item)
        return self.small_list_a

    def add_new_sequence(self):
        new_sequence = ["C", "D", "E", "F"]
        self.small_list_a.extend(new_sequence)
        return self.small_list_a

    def insert_at_sixth_position(self):
        self.small_list_a.insert(5, "60")
        return self.small_list_a

    #! this one, removes the first item with the indicared VALUE
    def remove_value_one_hundred(self):
        value_to_remove = "100"
        self.small_list_a.remove(value_to_remove)
        return self.small_list_a

    def remove_last_item(self):
        self.small_list_a.pop()
        return self.small_list_a

    def sort_in_place(self):
        self.small_list_a.extend(["-1", "-2", "-3"])
        self.small_list_a.sort()
        return self.small_list_a

    def reverse_in_place(self):
        self.small_list_a.reverse()
        return self.small_list_a

    def remove_range_items(self):
        self.small_list_a[4:13] = []
        return self.small_list_a

    def remove_list_duplicates(self):
        # ! convert to a set, BC set doesn't allow diplicates
        thisList = ["apple", "banana", "banana", "banana", "cherry"]
        thisSet = set(thisList)

        return thisSet

    def clear_all_items(self):
        # the list still exists, it's just NONE
        return self.small_list_a.clear()

    def test_list_exercises(self):
        print("get_all_items_one_list \n", self.get_all_items_one_list())
        print("get_first_item_list \n", self.get_first_item_list())
        print("get_last_item_list \n", self.get_last_item_list())
        print("get_first_3_items \n", self.get_first_3_items())
        print("get_middle_items \n", self.get_middle_items())
        print("get_both_lists_in_new_one \n", self.get_both_lists_in_new_one())
        print("get_all_but_last \n", self.get_all_but_last())
        print("add_list_b_to_a \n", self.add_list_b_to_a())
        print("get_last_half \n", self.get_last_half())
        print("get_odd_items \n", self.get_odd_items())
        print("get_reversed_list_a \n", self.get_reversed_list_a())
        print("get_num_items \n", self.get_num_items())
        print("self.get_sixth_item \n", self.get_sixth_item())
        print("self.remove_sixth_element \n", self.remove_sixth_element())
        print("self.upd_first_element \n", self.upd_first_element())
        print("self.add_item_at_end \n", self.add_item_at_end())
        print("self.add_new_sequence \n", self.add_new_sequence())
        print("self.insert_at_sixth_position \n", self.insert_at_sixth_position())
        print("self.remove_value_one_hundred \n", self.remove_value_one_hundred())
        print("self.remove_last_item \n", self.remove_last_item())
        print("self.sort_in_place \n", self.sort_in_place())
        print("self.reverse_in_place \n", self.reverse_in_place())
        print("self.remove_range_items \n", self.remove_range_items())
        print("self.remove_list_duplicates \n", self.remove_list_duplicates())
        print("self.clear_all_items \n", self.clear_all_items())


class DictExersices:
    def __init__(self):
        self.my_dict = None

    def create_dict_with_values(self):
        self.my_dict = {1: "one", 2: "two", 3: "three"}
        return self.my_dict

    def get_value(self):
        return self.my_dict[2]

    def add_new_key_value(self):
        self.my_dict[4] = "four"
        return self.my_dict

    def update_value(self):
        self.my_dict[1] = "uno"
        return self.my_dict

    def get_keys(self):
        # rerurns an ITERABLE
        return self.my_dict.keys()

    def get_values(self):
        # rerurns an ITERABLE
        return self.my_dict.values()

    def dict_contains_value_four(self):
        return True if "four" in self.my_dict.values() else False

    def remove_key_two(self):
        self.my_dict.pop(2)
        return self.my_dict

    def remove_non_exitant_key(self):
        return self.my_dict.pop(2, "The key does not exist")

    def remove_last_added(self):
        self.my_dict.popitem()
        return self.my_dict

    def get_value_of_a_key(self):
        return self.my_dict[1]

    def add_key_value_if_key_doesnt_exist(self):
        #  returns the value of the item with the specified key.
        # If the key does not exist, insert the key, with the specified value
        res = self.my_dict.setdefault(5, "five")
        return self.my_dict

    def create_new_dic_from_two_dicts(self):
        dict_one = {"A": "a", "B": "b", "C": "c", "D": "d"}
        dict_two = {
            "E": "e",
            "F": "f",
            "A": "aa",
            "B": "bb",
            "G": "g",
            "H": "h",
            "I": "i",
        }
        # !this also removes duplicates
        new_dict = {**dict_one, **dict_two}
        return new_dict

    def create_new_dic_from_other_two_opt_two(self):
        dict_one = {"A": "a", "B": "b"}
        dict_two = {
            "E": "e",
            "F": "f",
            "A": "aa",
            "B": "bb",
            "G": "g",

        }
        # !this also removes duplicates
        new_dict = dict_one.copy()
        new_dict.update(dict_two)

        return new_dict

    def create_new_dic_from_two_dicts_and_other_keys(self):
        dict_one = {"A": "a", "B": "b"}
        dict_two = {
            "E": "e",
            "F": "f",
            "A": "aa",
            "B": "bb",
            "G": "g",

        }
        # !this also removes duplicates
        new_dict = {**dict_one, 'key1':'value1', **dict_two, 'key2':'value2', 'key3':'value3'}

        return new_dict


    def merge_two_dicts(self):
        dict_one = {"A": "a", "B": "b"}
        dict_two = {
            "E": "e",
            "F": "f",
            "A": "aa",
            "B": "bb",
            "G": "g",

        }
        # !this also removes duplicates
        # I don't know why 2nd arg HAS TO HAVE **
        dict_one = dict(dict_one, **dict_two)

        return dict_one




    def test_dict_exercises(self):
        print("Dict exercises ")
        print("create_dict_with_values \n", self.create_dict_with_values())
        print("get_value \n", self.get_value())
        print("add_new_key_value \n", self.add_new_key_value())
        print("update_value \n", self.update_value())
        print("get_keys \n", self.get_keys())
        print("get_values \n", self.get_values())
        print("dict_contains_value_four \n", self.dict_contains_value_four())
        print("remove_key_two \n", self.remove_key_two())
        print("remove_non_exitant_key \n", self.remove_non_exitant_key())
        print("remove_last_added \n", self.remove_last_added())
        print("get_value_of_a_key \n", self.get_value_of_a_key())
        print("add_key_value_if_key_doesnt_exist \n", self.add_key_value_if_key_doesnt_exist())
        print("create_new_dic_from_two_dicts \n", self.create_new_dic_from_two_dicts())
        print("create_new_dic_from_two_dicts_and_other_keys \n", self.create_new_dic_from_two_dicts_and_other_keys())
        print("merge_two_dicts \n", self.merge_two_dicts())
        print("create_new_dic_from_other_two_opt_two \n", self.create_new_dic_from_other_two_opt_two())

class SetExercises():
    def __init__(self) -> None:
        pass

    def create_set(self):
        #! has to have double (())
        mySet = set(('apple', 'banana', 'cherry'))
        return mySet

    def get_set_len(self):
        mySet = {'apple', 'banana', 'cherry'}
        return len(mySet)

    def loop_set(self):
        mySet = {'apple', 'banana', 'cherry'}
        for item in mySet:
            print(item)

    def is_item_in_set(self):
        mySet = {'apple', 'banana', 'cherry'}
        return True if 'banana' in mySet else False


    def add_item_to_set(self):
        mySet = {'apple', 'banana', 'cherry'}
        mySet.add('straberry')
        return mySet

    def add_iterable_to_set(self):
        # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
        mySet = {'apple', 'banana', 'cherry'}
        myList =['chicken','eggs']
        mySet.update(myList)

        return mySet

    def merge_two_sets_in_one(self):
        # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
        mySet = {'apple', 'banana', 'cherry'}
        my_newSet = {'chicken','eggs'}
        mySet.update(my_newSet)

        return mySet


    def remove_list_item(self):
        # To remove an item in a set, use the remove(), or the discard() method.
        #  If the item to remove does not exist, remove() will raise an error.
        # If the item to remove does not exist, discard() will NOT raise an error.
        mySet = {'apple', 'banana', 'cherry'}
        mySet.discard('banana')

        return mySet


    def remove_last_item(self):
        # ! this method will always RETURN DIFFERENT VALUES
        # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
        mySet = {'apple', 'banana', 'cherry'}
        last_item = mySet.pop()
        return last_item


    def clear_set(self):
        mySet = {'apple', 'banana', 'cherry'}
        # this will create a None object
        mySet.clear()
        return mySet

    def delete_set(self):
        mySet = {'apple', 'banana', 'cherry'}
        # this will DELETE COMPLETLY THE OBJECT
        del mySet
        return "the object doesnt exist"

    def print_all_set_items(self):
        mySet = {'apple', 'banana', 'cherry'}
        for item in mySet:
            print(item)

        return "all the sets"

    def create_new_set_from_two_sets(self):
        mySet_one = {'apple', 'banana', 'cherry'}
        mySet_two ={'chicken','eggs'}
        # You can use the union() method that returns a new set containing all items from both sets
        # Both union() and update() will exclude any duplicate items.
        new_set = mySet_one.union(mySet_two)

        return new_set

    def add_set_to_existing_set(self):
        mySet_one = {'apple', 'banana', 'cherry'}
        mySet_two ={'chicken','eggs'}
        # update() method that inserts all the items from one set into another.
        # Both union() and update() will exclude any duplicate items.
        mySet_one.update(mySet_two)

        return mySet_one


    def get_items_in_both_sets(self):
        mySet_one = {'apple', 'banana', 'cherry', 'eggs'}
        mySet_two ={'chicken','eggs', 'banana'}
        duplicated_sets = mySet_one.intersection(mySet_two)
        # intersection() method will return a new set, that only contains the items that are present in both sets.
        return duplicated_sets

    def leave_just_duplicated_items_in_sets(self):
        mySet_one = {'apple', 'banana', 'cherry', 'eggs'}
        mySet_two ={'chicken','eggs', 'banana'}
        mySet_one.intersection_update(mySet_two)

        return mySet_one

    def get_new_set_with_non_duplicated_items_in_sets(self):
        mySet_one = {'apple', 'banana', 'cherry', 'eggs'}
        mySet_two ={'chicken','eggs', 'banana'}

        non_duplicated = mySet_one.symmetric_difference(mySet_two)

        return non_duplicated

    def remove_duplicates_from_sets(self):
        mySet_one = {'apple', 'banana', 'cherry', 'eggs'}
        mySet_two ={'chicken','eggs', 'banana'}
        mySet_one.symmetric_difference_update(mySet_two)
        # symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
        return mySet_one

    def are_set_item_into_other_set(self):
        mySet_one = {'apple', 'banana', 'cherry', 'eggs'}
        mySet_two ={'chicken','eggs', 'banana'}
        # sdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
        return not mySet_one.isdisjoint(mySet_two)

    def are_all_setA_items_in_setB(self):
        # the order of the sets doesnt matter
        mySet_one = {"a", "b", "c"}
        mySet_two ={"f", "e", "d", "c", "b", "a"}
        #! Returns whether another set contains this set or not
        # issubset True if all items in set mySet_one are present in set mySet_two:
        is_one_in_two =  mySet_one.issubset(mySet_two)

        return is_one_in_two


    def are_all_setB_items_in_setA(self):
        # the order of the sets doesnt matter
        mySet_one ={"f", "e", "d", "c", "b", "a"}
        mySet_two = {"a", "b", "c"}
        # Returns whether another set contains this set or not
        #! issubset True if all items in set mySet_two are present in set mySet_one:
        is_one_in_two =  mySet_one.issuperset(mySet_two)

        return is_one_in_two



    def test_set_exercises(self):
        print("Set exercises")
        print("create_set \n", self.create_set())
        print("get_set_len \n", self.get_set_len())
        self.loop_set()
        print("is_item_in_set \n", self.is_item_in_set())
        print("add_item_to_set \n", self.add_item_to_set())
        print("merge_two_sets_in_one \n", self.merge_two_sets_in_one())
        print("add_iterable_to_set \n", self.add_iterable_to_set())
        print("remove_list_item \n", self.remove_list_item())
        print("remove_last_item \n", self.remove_last_item())
        print("clear_set \n", self.clear_set())
        print("delete_set \n", self.delete_set())
        print("print_all_set_items \n", self.print_all_set_items())
        print("create_new_set_from_two_sets \n", self.create_new_set_from_two_sets())
        print("add_set_to_existing_set \n", self.add_set_to_existing_set())
        print("get_items_in_both_sets \n", self.get_items_in_both_sets())
        print("leave_just_duplicated_items_in_sets \n", self.leave_just_duplicated_items_in_sets())
        print("remove_duplicates_from_sets \n", self.remove_duplicates_from_sets())
        print("are_set_item_into_other_set \n", self.are_set_item_into_other_set())
        print("are_all_setA_items_in_setB \n", self.are_all_setA_items_in_setB())
        print("are_all_setB_items_in_setA \n", self.are_all_setB_items_in_setA())
        print("get_new_set_with_non_duplicated_items_in_sets \n", self.get_new_set_with_non_duplicated_items_in_sets())


if __name__ == "__main__":
    # lst = ListExersices()
    # lst.test_list_exercises()
    # hh = DictExersices()
    # hh.test_dict_exercises()
    thisSet =SetExercises()
    thisSet.test_set_exercises()




