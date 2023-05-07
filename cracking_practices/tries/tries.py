import os


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
            if self.children[letter] is None:
                return

            return self.children[letter]

        def add_child(self, letter):
            # in order to create an instance within the same class, I need to referece the superclass (trie)
            self.children[letter] = Trie.Node(letter)

        def get_children(self):
            return self.children.values()

        def has_children(self):
            return len(self.children.keys()) > 0

        def delete(self):
            self = None

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
                # if child.is_end_of_word:
                #     print("\n")

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

            if not self._is_root(current):
                print(current.value)

        traverse(self.root)

    def _is_empty_word(self, word):
        return len(word) == 0

    def _is_one_letter(self, word):
        return len(word) == 1

    # post order traversal
    def delete(self, word):
        if not self.contains(word):
            raise Exception("The word does no exist.")

        def traverse(current, word):
            if current is None:
                return

            if self._is_empty_word(word):
                current.is_end_of_word = False

                if not current.has_children():
                    current.delete()

                return

            current = current.get_child(word[0])
            cropped_word = word[1:]
            traverse(current, cropped_word)

        root_letter = self.root.get_child(word[0])
        traverse(root_letter, word[1:])

    def auto_complete(self, prefix):
        prefix = self._groom_word(prefix)
        if prefix is None:
            return

        # get the prefix children
        current = self.root.get_child(prefix[0])

        if not current:
            return

        def traverse(current, word, found_words):
            # base case
            word = word + current.value

            if not current.has_children():
                if current.is_end_of_word:
                    found_words.append(word)
                    print(found_words)
                return

            if current.is_end_of_word:
                found_words.append(word)

            for child in current.get_children():
                traverse(child, word, found_words)

        traverse(current, "", [])


if __name__ == "__main__":
    os.system("clear")
    trie = Trie()

    trie.insert("car")
    trie.insert("care")
    trie.insert("card")
    trie.insert("egg")
    trie.insert("nada")
    trie.insert("careful")

    print("contains car", trie.contains("car"))
    print("contains care", trie.contains("care"))
    # print("contains care", trie.contains("care"))
    # print("contains card", trie.contains("card"))
    # print("contains egg", trie.contains("egg"))
    # print("contains careful", trie.contains("careful"))
    # print("contains careful", trie.contains("iris"))
    # todo validate when there is no child letter
    # trie.auto_complete("s")
    trie.auto_complete("c")
    trie.auto_complete("e")
