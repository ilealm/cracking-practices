
import re


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
        print("get_count_of_one_item \n", self.get_count_of_one_item())
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
        new_dict = {
            **dict_one,
            "key1": "value1",
            **dict_two,
            "key2": "value2",
            "key3": "value3",
        }

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
        print(
            "add_key_value_if_key_doesnt_exist \n",
            self.add_key_value_if_key_doesnt_exist(),
        )
        print("create_new_dic_from_two_dicts \n", self.create_new_dic_from_two_dicts())
        print(
            "create_new_dic_from_two_dicts_and_other_keys \n",
            self.create_new_dic_from_two_dicts_and_other_keys(),
        )
        print("merge_two_dicts \n", self.merge_two_dicts())
        print(
            "create_new_dic_from_other_two_opt_two \n",
            self.create_new_dic_from_other_two_opt_two(),
        )


class SetExercises:
    def __init__(self) -> None:
        pass

    def create_set(self):
        #! has to have double (())
        mySet = set(("apple", "banana", "cherry"))
        return mySet

    def get_set_len(self):
        mySet = {"apple", "banana", "cherry"}
        return len(mySet)

    def loop_set(self):
        mySet = {"apple", "banana", "cherry"}
        for item in mySet:
            print(item)

    def is_item_in_set(self):
        mySet = {"apple", "banana", "cherry"}
        return True if "banana" in mySet else False

    def add_item_to_set(self):
        mySet = {"apple", "banana", "cherry"}
        mySet.add("straberry")
        return mySet

    def add_iterable_to_set(self):
        # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
        mySet = {"apple", "banana", "cherry"}
        myList = ["chicken", "eggs"]
        mySet.update(myList)

        return mySet

    def merge_two_sets_in_one(self):
        # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
        mySet = {"apple", "banana", "cherry"}
        my_newSet = {"chicken", "eggs"}
        mySet.update(my_newSet)

        return mySet

    def remove_set_item(self):
        # To remove an item in a set, use the remove(), or the discard() method.
        #  If the item to remove does not exist, remove() will raise an error.
        # If the item to remove does not exist, discard() will NOT raise an error.
        mySet = {"apple", "banana", "cherry"}
        mySet.discard("banana")

        return mySet

    def remove_random_item(self):
        # ! this method will always RETURN DIFFERENT VALUES
        # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
        mySet = {"apple", "banana", "cherry"}
        last_item = mySet.pop()
        return last_item

    def clear_set(self):
        mySet = {"apple", "banana", "cherry"}
        # this will create a None object
        mySet.clear()
        return mySet

    def delete_set(self):
        mySet = {"apple", "banana", "cherry"}
        # this will DELETE COMPLETLY THE OBJECT
        del mySet
        return "the object doesnt exist"

    def print_all_set_items(self):
        mySet = {"apple", "banana", "cherry"}
        for item in mySet:
            print(item)

        return "all the sets"

    def create_new_set_from_two_sets(self):
        mySet_one = {"apple", "banana", "cherry"}
        mySet_two = {"chicken", "eggs"}
        # You can use the union() method that returns a new set containing all items from both sets
        # Both union() and update() will exclude any duplicate items.
        new_set = mySet_one.union(mySet_two)

        return new_set

    def add_set_to_existing_set(self):
        mySet_one = {"apple", "banana", "cherry"}
        mySet_two = {"chicken", "eggs"}
        # update() method that inserts all the items from one set into another.
        # Both union() and update() will exclude any duplicate items.
        mySet_one.update(mySet_two)

        return mySet_one

    def get_items_in_both_sets(self):
        mySet_one = {"apple", "banana", "cherry", "eggs"}
        mySet_two = {"chicken", "eggs", "banana"}
        duplicated_sets = mySet_one.intersection(mySet_two)
        # intersection() method will return a new set, that only contains the items that are present in both sets.
        return duplicated_sets

    def leave_just_duplicated_items_in_sets(self):
        mySet_one = {"apple", "banana", "cherry", "eggs"}
        mySet_two = {"chicken", "eggs", "banana"}
        mySet_one.intersection_update(mySet_two)

        return mySet_one

    def get_new_set_with_non_duplicated_items_in_sets(self):
        mySet_one = {"apple", "banana", "cherry", "eggs"}
        mySet_two = {"chicken", "eggs", "banana"}

        non_duplicated = mySet_one.symmetric_difference(mySet_two)

        return non_duplicated

    def remove_duplicates_from_sets(self):
        mySet_one = {"apple", "banana", "cherry", "eggs"}
        mySet_two = {"chicken", "eggs", "banana"}
        mySet_one.symmetric_difference_update(mySet_two)
        # symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
        return mySet_one

    def are_set_item_into_other_set(self):
        mySet_one = {"apple", "banana", "cherry", "eggs"}
        mySet_two = {"chicken", "eggs", "banana"}
        # sdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
        return not mySet_one.isdisjoint(mySet_two)

    def are_all_setA_items_in_setB(self):
        # the order of the sets doesnt matter
        mySet_one = {"a", "b", "c"}
        mySet_two = {"f", "e", "d", "c", "b", "a"}
        #! Returns whether another set contains this set or not
        # issubset True if all items in set mySet_one are present in set mySet_two:
        is_one_in_two = mySet_one.issubset(mySet_two)

        return is_one_in_two

    def are_all_setB_items_in_setA(self):
        # the order of the sets doesnt matter
        mySet_one = {"f", "e", "d", "c", "b", "a"}
        mySet_two = {"a", "b", "c"}
        # Returns whether another set contains this set or not
        #! issubset True if all items in set mySet_two are present in set mySet_one:
        is_one_in_two = mySet_one.issuperset(mySet_two)

        return is_one_in_two


    def add_three_lists_to_a_set(self):
        set1 = {11, 12, 13, 14}
        # 3 lists of numbers
        list1 = [15, 16, 17]
        list2 = [18, 19]
        list3 = [30, 31, 19, 17]
        set1.update(list1, list2, list3)

        return set1


    def add_list_to_set_with_pipe(self):
        #original set
        set1 = {1, 2, 3, 4, 5}
        #list ofnumbers to add
        list1 = [6, 7]
        # convert list to set and get union of both the sets using |
        set1 |= set(list1)

        return set1

    def add_tuple_to_a_set(self):
        #input set
        set1 = {1, 2, 4, 5}
        # tuple to add
        tuple1 = (6, 7)
        #add tuple to the set
        set1.add(tuple1)

        return set1
        # {1, 2, 4, 5, (6, 7)}

    def test_set_exercises(self):
        print("Set exercises")
        print("create_set \n", self.create_set())
        print("get_set_len \n", self.get_set_len())
        self.loop_set()
        print("is_item_in_set \n", self.is_item_in_set())
        print("add_item_to_set \n", self.add_item_to_set())
        print("merge_two_sets_in_one \n", self.merge_two_sets_in_one())
        print("add_iterable_to_set \n", self.add_iterable_to_set())
        print("remove_set_item \n", self.remove_set_item())
        print("remove_random_item \n", self.remove_random_item())
        print("clear_set \n", self.clear_set())
        print("delete_set \n", self.delete_set())
        print("print_all_set_items \n", self.print_all_set_items())
        print("create_new_set_from_two_sets \n", self.create_new_set_from_two_sets())
        print("add_set_to_existing_set \n", self.add_set_to_existing_set())
        print("get_items_in_both_sets \n", self.get_items_in_both_sets())
        print(
            "leave_just_duplicated_items_in_sets \n",
            self.leave_just_duplicated_items_in_sets(),
        )
        print("remove_duplicates_from_sets \n", self.remove_duplicates_from_sets())
        print("are_set_item_into_other_set \n", self.are_set_item_into_other_set())
        print("are_all_setA_items_in_setB \n", self.are_all_setA_items_in_setB())
        print("are_all_setB_items_in_setA \n", self.are_all_setB_items_in_setA())
        print(
            "get_new_set_with_non_duplicated_items_in_sets \n",
            self.get_new_set_with_non_duplicated_items_in_sets(),
        )
        print("add_three_lists_to_a_set \n", self.add_three_lists_to_a_set())
        print("add_list_to_set_with_pipe \n", self.add_list_to_set_with_pipe())
        print("add_tuple_to_a_set \n", self.add_tuple_to_a_set())


class TuplesExercises:
    def create_tuple(self):
        #! it's better to add always a "," at the end of the list, so Python can ID as a tuple
        # When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
        my_tupple = (
            "apple",
            "banana",
            "cherry",
            "banana",
        )
        return my_tupple

    def create_tuple_with_constructor(self):
        #! note the double round-brackets
        my_tuple = tuple(("apple", "banana", "cherry", "banana"))
        return my_tuple

    def create_tuple_with_one_item(self):
        # ! To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
        my_tuple = ("apple",)
        return my_tuple

    def create_tuple_dif_data_types(self):
        my_tupple = (
            "apple",
            548,
            True,
        )
        return my_tupple

    def get_tuple_len(self):
        my_tupple = (
            "apple",
            "banana",
            "cherry",
            "banana",
        )
        return len(my_tupple)

    def get_item_with_index(self):
        # BC tuples are ordered, I will alwasys have them ordered
        my_tupple = (
            "apple",
            "cherry",
            "banana",
            "cherry",
            "banana",
        )
        return my_tupple[1]

    def get_last_item(self):
        # tuples accept negative index, like list
        my_tupple = (
            "apple",
            "banana",
            "cherry",
            "banana",
        )
        return my_tupple[-1]

    def get_second_to_last_item(self):
        # tuples accept negative index, like list
        my_tupple = (
            "apple",
            "banana",
            "cherry",
            "orange",
            "banana",
        )
        return my_tupple[-2]

    def get_range_in_tuple(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        # The search will start at index 2 (included) and end at index 5 (not included)
        return my_tuple[2:5]

    def get_items_until_nth_position(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        return my_tuple[:4]

    def get_items_from_nth_to_end(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        return my_tuple[2:]

    def get_last_three_items(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        # returns the items from index -4 (included) to index -1 (excluded)
        return my_tuple[-4:-1]

    def item_exist(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        return True if "orange" in my_tuple else False

    def workaround_to_edit_item(self):
        my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        # Tuples are unchangeable, or immutable as it also is called.
        # But there is a workaround.
        # You can convert the tuple into a list, change the list, and convert the list back into a tuple.
        my_list = list(my_tuple)
        my_list[1] = "BANANA"
        my_tuple = tuple(my_list)
        return my_tuple

    def add_item(self):
        my_tuple = ("apple", "banana", "cherry")
        # Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
        # Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
        my_list = list(my_tuple)
        my_list.append("MANGO")
        my_tuple = tuple(my_list)
        return my_tuple

    def add_tuple_to_tuple(self):
        my_tuple = (
            "apple",
            "banana",
            "cherry",
        )
        # ! When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
        my_new_tuple = ("EGGS",)
        my_tuple += my_new_tuple
        return my_tuple

    def remove_item(self):
        # ! Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
        my_tuple = (
            "apple",
            "banana",
            "cherry",
        )
        # ! When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
        my_list = list(my_tuple)
        my_list.remove("banana")
        my_tuple = tuple(my_list)
        return my_tuple

    def delete_tuple(self):
        # del keyword can delete the tuple completely:
        my_tuple = (
            "apple",
            "banana",
            "cherry",
        )
        del my_tuple
        return "Deleted"

    def set_items_into_variables(self):
        # When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
        # But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
        fruits = ("apple", "banana", "cherry")
        #! The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
        (green, yellow, red) = fruits

        return (green, yellow, red)

    def set_some_items_to_list_variable(self):
        fruits = (
            "apple",
            "banana",
            "cherry",
            "strawberry",
            "raspberry",
        )
        # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
        (first, second, *my_list_variable) = fruits

        return first, second, my_list_variable
        # -->  ('apple', 'banana', ['cherry', 'strawberry', 'raspberry'])

    # If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
    def set_middle_items_to_list_variable(self):
        fruits = (
            "apple",
            "banana",
            "cherry",
            "strawberry",
            "raspberry",
        )
        (first, *middle_items,last) = fruits

        return (first, middle_items,last)
        # --> ('apple', ['banana', 'cherry', 'strawberry'], 'raspberry')


    def loop_tuple(self):
        my_tuple = ("apple", "banana","cherry")
        items = ""
        for item in my_tuple:
            items += item + ", "

        return items

    def loop_tuple_with_range_and_index(self):
        my_tuple = ("apple", "banana", "cherry", "lime")
        items = ""
        for i in range(len(my_tuple)):
            items += my_tuple[i] + ", "

        return items

    def join_two_tuples(self):
        tuple_one = ("eggs", "milk",)
        tuple_two = ("bananas", "milk", "berries")
        all_tuple = tuple_one + tuple_two

        return all_tuple
        # -->  ('eggs', 'milk', 'bananas', 'milk', 'berries')

    def multiply_tuple(self):
        base_tuple = ("one", "two", "three",)
        multiplied_base = base_tuple * 3

        return multiplied_base
        #  -->  ('one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three')


    def get_count_of_one_item(self):
        my_tuple = ("milk", "eggs", "milk", "bread", "milk")
        return my_tuple.count("milk")
        # -->  3

    def get_index_of_item(self):
        my_tuple = ("milk", "eggs", "milk", "bread", "milk")
        return my_tuple.index("eggs")
        # -->  1

    def test_tuples_exercises(self):
        print("create_tuple --> ", self.create_tuple())
        print("create_tuple_with_one_item --> ", self.create_tuple_with_one_item())
        print("get_tuple_len --> ", self.get_tuple_len())
        print("create_tuple_dif_data_types --> ", self.create_tuple_dif_data_types())
        print(
            "create_tuple_with_constructor --> ", self.create_tuple_with_constructor()
        )
        print("get_item_with_index --> ", self.get_item_with_index())
        print("get_last_item --> ", self.get_last_item())
        print("get_second_to_last_item --> ", self.get_second_to_last_item())
        print("get_range_in_tuple --> ", self.get_range_in_tuple())
        print("get_items_until_nth_position --> ", self.get_items_until_nth_position())
        print("get_items_from_nth_to_end --> ", self.get_items_from_nth_to_end())
        print("get_last_three_items --> ", self.get_last_three_items())
        print("item_exist --> ", self.item_exist())
        print("workaround_to_edit_item --> ", self.workaround_to_edit_item())
        print("add_item --> ", self.add_item())
        print("add_tuple_to_tuple --> ", self.add_tuple_to_tuple())
        print("remove_item --> ", self.remove_item())
        print("delete_tuple --> ", self.delete_tuple())
        print("set_items_into_variables --> ", self.set_items_into_variables())
        print("set_some_items_to_list_variable --> ", self.set_some_items_to_list_variable())
        print("set_middle_items_to_list_variable --> ", self.set_middle_items_to_list_variable())
        print("loop_tuple --> ", self.loop_tuple())
        print("loop_tuple_with_range_and_index --> ", self.loop_tuple_with_range_and_index())
        print("join_two_tuples --> ", self.join_two_tuples())
        print("join_two_tuples --> ", self.join_two_tuples())
        print("multiply_tuple --> ", self.multiply_tuple())
        print("get_count_of_one_item --> ", self.get_count_of_one_item())
        print("get_index_of_item --> ", self.get_index_of_item())


class MatchExercises:
    def find_first_name_with_seven_letters(self):
        names = ["Linda", "Tiffany", "Florina", "Jovann"]
        length_of_names = [len(name) for name in names]
        # --> [5, 7, 7, 6]
        idx = length_of_names.index(7)
        return names[idx]

    def find_index_first_match(self):
        names = ["Linda", "Tiffany", "Florina", "Jovann"]
        idx = names.index("Florina")
        return idx

    def test_match_exercises(self):
        print("find_first_name_with_seven_letters  --> ", self.find_first_name_with_seven_letters())
        print("find_index_first_match  --> ", self.find_index_first_match())

# if __name__ == "__main__":
    # lst = ListExersices()
    # lst.test_list_exercises()
    # hh = DictExersices()
    # hh.test_dict_exercises()
    # thisSet =SetExercises()
    # thisSet.test_set_exercises()
    # tpl = TuplesExercises()
    # tpl.test_tuples_exercises()
    # matchs = MatchExercises()
    # matchs.test_match_exercises()

