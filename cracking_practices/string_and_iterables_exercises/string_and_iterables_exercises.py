import re
from select import select


class StringsExersices:
    def __init__(self):
        self.smalll_sentence = "This is a small sentence"


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
        return self.small_list_a[7-1]

    def remove_sixth_element(self):
        del self.small_list_a[6-1]
        return self.small_list_a

    def upd_first_element(self):
        self.small_list_a[1-1] = 'A'
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




if __name__ == "__main__":
    lst = ListExersices()
    lst.test_list_exercises()


# sdf
