class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = self.Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def top(self):
        if self.empty():
            return False
        return self.head.next.value

    def push(self, value):
        node = self.Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


class AbstractBinaryTree:
    ...


class BinaryTree(AbstractBinaryTree):
    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, string):
        self.root = self.Node(None)
        if (self._check_balance(string)):
            s = string
            temp_s = ""
            while s:
                if self._is_operator(s[0]):
                    s = "" + s[1:]
                    continue

                while not self._is_operator(s[0]):
                    temp_s += s[0]
                    s = "" + s[1:]

                if temp_s:
                    self.add(int(temp_s))
                    temp_s = ""
                s = "" + s[1:]

    def _check_balance(self, string):
        stack = Stack()
        for char in string:
            match char:
                case "(":
                    stack.push(")")
                case ")":
                    if stack.top() != char or stack.empty():
                        print("Bad balance")
                        return False
                    stack.pop()
                case _:
                    continue
        if not stack.empty():
            print("Bad balance")
            return False
        return True

    def _is_operator(self, char):
        ops = [",", "(", ")"]
        if char not in ops:
            return False
        return True

    def add(self, data):
        if self.root.data == None:
            self.root = self.Node(data)
            return
        v = self.root
        while data < v.data and v.left != None or \
                data > v.data and v.right != None:
            if data < v.data:
                v = v.left
            else:
                v = v.right
        if data == v.data:
            return
        new_node = self.Node(data)
        if data < v.data:
            v.left = new_node
        else:
            v.right = new_node


if __name__ == "__main__":
    l = BinaryTree("8 (3 (1, 6 (4,7)), 10 (, 14(13,)))")
