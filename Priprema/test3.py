class Node:
    def __init__(self, parent=None, children=None, data=None):
        self.parent = parent
        self.children = children  # DICT -> keys: letter of child nodes; values: refs to child nodes
        self.data = data  # Letter of specific node
        self.last_letter = False  # boolean that indicates if this node is the last letter of some word

    def __str__(self):
        return str(self.data) + " node has children -> " + str(self.children.keys())


class Tree:

    def __init__(self, r=None):
        self.root = r
        self.all_nodes = []  # helper field for printing
        self.leafs = []  # helper field for auto_complete function

    # TASK a) -> 1)
    # does the insertion of nodes
    def form_tree(self, words):
        self.all_nodes = []
        for word in words:
            curr_node = self.root
            for letter in word:
                if letter in curr_node.children.keys():
                    # prepare for next iteration
                    curr_node = curr_node.children[letter]
                    continue
                else:
                    # create node and add it to dict (children) of curr_node
                    node = Node(parent=curr_node, children={}, data=letter)
                    curr_node.children[letter] = node

                    self.all_nodes.append(node)

                    # prepare for next iteration
                    curr_node = node

            curr_node.last_letter = True

        return self.root

    # TASK b) -> a.
    def find_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[letter]

        return curr_node.last_letter

    # TASK b) -> b.
    def auto_complete(self, part):
        def find_leafs(node_):
            if node_.last_letter:
                self.leafs.append(node_)

            if node_.children:
                for letter_ in node_.children.keys():
                    find_leafs(node_.children[letter_])

        curr_node = self.root
        ret_list = []
        for letter in part:
            if letter not in curr_node.children:
                print("Requested pattern is not in dict!")
                return ret_list
            else:
                curr_node = curr_node.children[letter]

        self.leafs = []
        find_leafs(curr_node)

        for node in self.leafs:
            word = ""
            while node.data != "RECNIK":
                word = node.data + word
                node = node.parent
            ret_list.append(word)

        return ret_list

    # TASK b) -> c. -> 1)
    def delete_words(self, letter):
        def del_references(node):
            self.all_nodes.remove(node)
            for child in node.children.values():
                del_references(child)

        if letter not in self.root.children.keys():
            print(f"0 words starting with letter {letter} found")
            return
        else:
            start_node = self.root.children[letter]
            del_references(start_node)
            del self.root.children[letter]

    # Helper function
    def print_tree_data(self):
        print(self.root)
        for node in self.all_nodes:
            print(node)


if __name__ == "__main__":
    root_node = Node(parent=None, children={}, data="RECNIK")
    tree = Tree(r=root_node)

    test = True
    if test:
        word_list = ["panorama", "pasivno", "penkalo", "pecivo", "pero", "portir", "salata"]
        tree.form_tree(word_list)

        print("All nodes with their children fields:")
        tree.print_tree_data()
        print()

        print("FIND_WORD function:")
        print("Return value of find_word fun with existing word as a param:    ", tree.find_word("pecivo"))
        print("Return value of find_word fun with non-existing word as a param:", tree.find_word("papir"))
        print()

        print("AUTO_COMPLETE function:")
        print("Return list for 'pe' pattern (should return 3 words):")
        print(tree.auto_complete("pe"))
        print("Return list for 'pac' pattern (no words with that pattern):")
        print(tree.auto_complete("pac"))
        print()

        print("DELETE_WORDS function:")
        print("Deleting all words starting with 'p'...")
        tree.delete_words("p")
        print("Dict after deletion:")
        tree.print_tree_data()
        print()

    # user interface
    print("Create dict with given words,")
    print("user input should be words separated with spaces, e.g.:")
    print("paprika paradajz pomfrit pekara sladoled slanina")
    words = input("your input: ")
    words = words.split(" ")

    users_root = Node(parent=None, children={}, data="RECNIK")
    users_tree = Tree(r=users_root)
    users_tree.form_tree(words)
    users_tree.print_tree_data()
    print()

    while True:
        print("Choose operation (use corresponding numbers):")
        print("1 -> check if word is in dict")
        print("2 -> find words starting with term")
        print("3 -> delete words starting with letter")
        print("4 -> quit the program")
        menu = input("your input: ")

        if menu == "1":
            print("Check if word exists in dict ->")
            inp = input("input word to search for: ")
            if users_tree.find_word(inp):
                print("Given word was found in dict!")
            else:
                print("Given word was NOT found in dict!")
            print()
        elif menu == "2":
            print("Find words starting with given pattern ->")
            inp = input("input pattern to search for: ")
            print(users_tree.auto_complete(inp))
            print()
        elif menu == "3":
            print("Delete words starting with given letter ->")
            inp = input("input letter: ")
            users_tree.delete_words(inp)
            print("Deleted words starting with letter", inp)
            print("Dict after deletion:")
            users_tree.print_tree_data()
            print()
        elif menu == "4":
            break
        else:
            print("Unknown command! Try again . . .")