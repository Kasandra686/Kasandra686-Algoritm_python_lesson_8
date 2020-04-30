# 2) Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'value={self.value},left={self.left},right={self.right}...'


def huffman_algorithm(string):
    def huffman_tree(string):
        leaf_nodes = Counter()
        leaf = Counter(string)

        for i, value in leaf.items():
            leaf_nodes[Node(i)] = value

        while len(leaf_nodes) > 1:
            most_common = leaf_nodes.most_common()
            intermediate_node = Node(False, left=most_common[-2][0], right=most_common[-1][0])
            leaf_nodes[intermediate_node] = leaf_nodes.pop(most_common[-1][0]) + leaf_nodes.pop(most_common[-2][0])

        return list(leaf_nodes.keys())[0]

    def create_char_codes(bin_tree, char_codes, path=''):
        if bin_tree.value:
            char_codes[bin_tree.value] = path

        if bin_tree.left is not None:
            create_char_codes(bin_tree.left, char_codes, path=f'{path}0')

        if bin_tree.right is not None:
            create_char_codes(bin_tree.right, char_codes, path=f'{path}1')

    char_codes = dict()
    bin_tree = huffman_tree(string)
    create_char_codes(bin_tree, char_codes)
    return ' '.join([char_codes[char] for char in string])


if __name__ == "__main__":
    # s = input("Введите строку: ")
    s = 'beep boop beer!'
    print(s)
    print(huffman_algorithm(s))
    s2 = 'hiit hyyt hrro.'
    print(s2)
    print(huffman_algorithm(s2))

