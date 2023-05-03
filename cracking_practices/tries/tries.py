import os


class Node:
    def __init__(self, value):
        self.value = value
        # self.children = [None] * 26  # for each letter in the alphabet
        self.children = {}
        self.is_end_of_word = False

    def __str__(self):
        return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'

    def __repr__(self):
        return f'Value: {self.value}, Is_end_of_word: {self.is_end_of_word}'


class Trie(Node):
    def __init__(self):
        self.root = Node("root")
        # self.root = Node(None)

    def __str__(self):
        return f'Root: {self.root}'

    def __repr__(self):
        return f'Root: {self.root}'

        
    def insert(self, word):
        word = word.lower()
        print("inserting ", word)
        # set current to root
        current = self.root
        # traverse all the word
        for i in range(len(word)):
            letter = word[i]
            print(letter)
            if self._letter_exist_in_dict(current, letter):
                current = current.children[letter]
            else:
                new_node = Node(letter)
                current.children[letter] = new_node
                current = new_node

        current.is_end_of_word = True

        print("done")

    def _letter_exist_in_dict(self, current, letter):
        return letter in current.children

    # # rerturn the letter's possition on the array. which is the same -1 possition on the alphabet
    # def _get_ch_index(self, ch):
    #     return ord(ch.lower()) - ord("a")


if __name__ == "__main__":
    os.system("clear")
    trie = Trie()
    # trie.insert("@")
    trie.insert("BOY")
    trie.insert("BOl")

    # test uppercase
    # test non alphabet characters

#
