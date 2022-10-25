# PROBLEM DOMAIN
# Having a string, return the first non reperting character. Uppercase and lower cases are the same
# "A green apple"
# a:2; g:1; r:1; e:3; n:1; p:2; l:1
# return: g

# from curses import erasechar


# BLANK = object()


# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = size * [BLANK]

#     def __len__(self):
#         return len(self.table)

#     def __get_index__(self, key):
#         list_key = [ord(i.lower()) for i in key]
#         list_sum = sum(list_key)

#         index = (list_sum * 41) % self.size

#         return index

#     def add(self, key, value):
#         index = self.__get_index__(key)
#         # TODO manage collitions
#         self.table[index] = value

#     def is_key_in_table(self, key):
#         index = self.__get_index__(key)

#         return self.table[index] is not BLANK


#     def get_value(self, key):
#         index = self.__get_index__(key)
#         # if (self.table[index]) is BLANK:
#         #     raise KeyError(key)

#         return self.table[index]


#     def delete(self, key):
#         # TODO manage collitions
#         index = self.__get_index__(key)
#         self.table[index] = BLANK


from re import S


class TextChecking:
    def __init__(self):
        self.hash_table = {}

    def __find_first_non_repeted__(self, text):
        for ch in text:
            if self.hash_table.get(ch) == 1:
                return ch

        if len(text) > 1:
            return text[0]


        return None

    def __increase_key_counter__(self, key):
        key = key.lower()
        # if self.hash_table[key] is None:
        if self.hash_table.get(key) is None:
            self.hash_table[key] = 1
        else:
            self.hash_table[key] += 1

    def __fill_hash_table__(self, text):
        for ch in text:
            self.__increase_key_counter__(ch)

    def return_first_non_repeted(self, text):
        self.__fill_hash_table__(text)

        return self.__find_first_non_repeted__(text)
