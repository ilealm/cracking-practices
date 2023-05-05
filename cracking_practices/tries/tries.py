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
class Trie:
    def __init__(self):
        self.root = self.Node("root")
        # self.root = Node(None)

    def __str__(self):
        return f"Root: {self.root}"

    def __repr__(self):
        return f"Root: {self.root}"

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = {}
            self.is_end_of_word = False

        def __str__(self):
            return f"Value: {self.value} "

        def __repr__(self):
            return f"Value: {self.value}"

        def has_child(self, letter):
            return letter in self.children

        def get_child(self, letter):
            return self.children[letter]

        def add_child(self, letter):
            # in order to create an instance within the same class, I need to referece the superclass (trie)
            self.children[letter] = Trie.Node(letter)

        def get_children(self):
            return self.children.values()



    def _groom_word(self, word):
        if word is None:
            raise Exception("There is no word.")

        return word.lower().strip()

    def insert(self, word):
        word = self._groom_word(word)
        current = self.root

        for letter in word:
            if not current.has_child(letter):
                current.add_child(letter)

            current = current.get_child(letter)

        current.is_end_of_word = True



    def contains(self, word):
        if word is None : return False

        word = self._groom_word(word)
        current = self.root

        for letter in word:
            if not current.has_child(letter):
                return False

            current = current.get_child(letter)

        return current.is_end_of_word


    # Preorder: root first
    def traverse_preorder(self):
        def traverse(current):
            if not current : return

            print(current.value)
            for child in current.get_children():
                traverse(child)

        traverse(self.root)


if __name__ == "__main__":
    os.system("clear")
    trie = Trie()
    # trie.insert("@")
    # trie.insert("BOY ")
    # trie.insert("  BOly")
    trie.insert("care")
    trie.insert("job")
    trie.insert("iris")
    trie.traverse_preorder()
    # print(trie.contains(None))

    # test uppercase
    # test non alphabet characters

#
