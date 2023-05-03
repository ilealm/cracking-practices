import os


# class Node:
#     def __init__(self, value):
#         self.value = value
#         # self.children = [None] * 26  # for each letter in the alphabet
#         self.children = {}
#         self.is_end_of_word = False

#     def __str__(self):
#         return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'

#     def __repr__(self):
#         return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'


# class Trie(Node):
class Trie():
    def __init__(self):
        self.root = self.Node("root")
        # self.root = Node(None)

    def __str__(self):
        return f'Root: {self.root}'

    def __repr__(self):
        return f'Root: {self.root}'


    class Node():
        def __init__(self, value):
            self.value = value
            self.children = {}
            self.is_end_of_word = False

        def __str__(self):
            return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'

        def __repr__(self):
            return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'

        def has_child(self, letter):
            return letter in self.children




        def add_child(self, letter):
            # x = self.Node(letter)
            self.children[letter] = self.Node(letter)


        def get_child(self, letter):
            return self.children[letter]


    def insert(self, word):
        word = word.lower()
        print("inserting ", word)
        current = self.root

        # TODO ckeck other forms of for in range
        for i in range(len(word)):
            letter = word[i]
            print(letter)
            # if self._letter_exist_in_dict(current, letter):
            if not current.has_child(letter):
                # ! esta linea es la que intentaba cambiar
                # current.add_child(letter)
                current.children[letter] = self.Node(letter)

            current = current.get_child(letter)

        current.is_end_of_word = True

        print("done")




if __name__ == "__main__":
    os.system("clear")
    trie = Trie()
    # trie.insert("@")
    trie.insert("BOY")
    trie.insert("BOly")

    # test uppercase
    # test non alphabet characters

#
