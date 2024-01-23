class BinomialTree:
    def __init__(self, key):
        # Initialize a binomial tree with a key, an order of 0, and an empty list of children.
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        # Add a binomial tree 't' as a child at the end of the current tree's children.
        self.children.append(t)
        self.order = self.order + 1

class BinomialHeap:
    def __init__(self):
        # Initialize a binomial heap with an empty list of trees.
        self.trees = []

    def __iter__(self):
        return iter(self.trees)

    def extract_min(self):
        # Extract the minimum key from the binomial heap.
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node.key

    def get_min(self):
        # Get the minimum key from the binomial heap without removing it.
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least

    def combine_roots(self, h):
        # Combine the root lists of two binomial heaps.
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)

    def merge(self, h):
        # Merge two binomial heaps.
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                    and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1

    def insert(self, key):
        # Insert a key into the binomial heap.
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)

def main():
    # Create a binomial heap.
    bheap = BinomialHeap()

    print('Menu')
    print('insert <data>')
    print('min get')
    print('min extract')
    print('quit')

    while True:
        do = input('What would you like to do? ').split()

        operation = do[0].strip().lower()
        if operation == 'insert':
            data = int(do[1])
            bheap.insert(data)
        elif operation == 'min':
            suboperation = do[1].strip().lower()
            if suboperation == 'get':
                print('Minimum value: {}'.format(bheap.get_min()))
            elif suboperation == 'extract':
                print('Minimum value removed: {}'.format(bheap.extract_min()))
        elif operation == 'quit':
            break

if __name__ == '__main__':
    main()
