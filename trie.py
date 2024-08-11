"""
Implementation + test case based off this blog: 
https://medium.com/codefight-on/codefights-solves-it-findsubstrings-5d6284d314e0

Note -- the original test case has bugs which I fixed! 
"""


class TrieNode:
    def __init__(self, letter=None, terminal=False):
        self.children = dict()
        self.letter = letter
        self.terminal = terminal


def add_word(root, word):
    changed = False
    curr = root
    for letter in word:
        if letter not in curr.children:
            curr.children[letter] = TrieNode(letter)
            changed = True
        curr = curr.children[letter]
    if not curr.terminal:
        curr.terminal = True
        changed = True
    return not changed


def trie_equal(t1, t2):
    if t1.letter != t2.letter:
        return False
    if t1.terminal != t2.terminal:
        return False
    if len(t1.children) != len(t2.children):
        return False
    for c1, c2 in zip(t1.children.values(), t2.children.values()):
        if not trie_equal(c1, c2):
            return False
    return True


def main():

    root1 = TrieNode()
    c = TrieNode("c")
    root1.children["c"] = c
    a1 = TrieNode("a")
    c.children["a"] = a1
    h = TrieNode("h")
    c.children["h"] = h
    t1 = TrieNode("t")
    m = TrieNode("m")
    a2 = TrieNode("a")
    t1.terminal = True
    m.terminal = True
    a2.terminal = True
    a1.children["t"] = t1
    a1.children["m"] = m
    h.children["a"] = a2
    t2 = TrieNode("t")
    t2.terminal = True
    a2.children["t"] = t2

    root2 = TrieNode()
    for word in ["cat", "cam", "cha", "chat"]:
        print(f"Adding {word}, was it there? {add_word(root2, word)}")
        print(f"Searching {word}, was it there? {add_word(root2, word)}")

    print(
        f"Manually constructed trie = add_word( ) construction? {trie_equal(root1, root2)}"
    )


if __name__ == "__main__":
    main()
