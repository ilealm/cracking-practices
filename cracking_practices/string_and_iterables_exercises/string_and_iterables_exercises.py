# class StringsExersices:
#     def __init__(self):
#         self.smalll_sentence = "This is a small sentence"


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
        res = self.my_dict.setdefault(5,"five")
        return self.my_dict


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
        print("add_key_value_if_key_doesnt_exist \n", self.add_key_value_if_key_doesnt_exist() )
        # print(" \n", self.() )


#


if __name__ == "__main__":
    lst = ListExersices()
    # lst.test_list_exercises()
    hh = DictExersices()
    hh.test_dict_exercises()


# sdf
