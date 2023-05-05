import os

# class Trie(Node):
class Trie:
    def __init__(self):
        self.root = self.Node("root")

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

        def has_children(self):
            return len(self.children.keys()) > 0

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
        if word is None:
            return False

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
            if not current:
                return

            if not self._is_root(current):
                print(current.value)
            # print(current.value)
            for child in current.get_children():
                traverse(child)
                if child.is_end_of_word:
                    print("\n")

        traverse(self.root)

    def _is_root(self, current):
        return current.value == "root"

    # Postorder: leaf first. The word will be backwards
    def traverse_postorder(self):
        def traverse(current):
            if not current:
                return

            for child in current.get_children():
                traverse(child)
                # if child.is_end_of_word:
                #     print("\n")

            if not self._is_root(current):
                print(current.value)

        traverse(self.root)

    def _is_empty_word(self, word):
        return len(word) == 0

    def _is_one_letter(self, word):
        return len(word) == 1

    def delete(self, word):
        def traverse(current, word):
            if current is None:
                return

            print(current.value, "   word:", word)

            # if I reached the end of the word
            if self._is_empty_word(word):
                print(current.is_end_of_word)
                current.is_end_of_word = False
                print(current.is_end_of_word)
                # todo if there is no child, delete the word upwards
                if current.has_children():
                    print("I CANT delete this word, IT HAS CHILDREN")
                else:
                    print("I can delete this word")
                return

            current = current.get_child(word[0])
            cropped_word = word[1:]
            traverse(current, cropped_word)

        root_letter = self.root.get_child(word[0])
        traverse(root_letter, word[1:])
        print("done")


if __name__ == "__main__":
    os.system("clear")
    trie = Trie()
    # trie.insert("@")
    # trie.insert("BOY ")
    # trie.insert("  BOly")
    trie.insert("care")
    trie.insert("other")
    trie.insert("nada")
    print("\n\n")
    # trie.delete("care")
    trie.delete("car")
    # trie.traverse_postorder()
    # print(trie.contains(None))

    # test uppercase
    # test non alphabet characters

#
