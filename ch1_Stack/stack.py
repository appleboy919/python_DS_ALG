# implementing Stack data structure

class stack:
    def __init__(self):
        self.itmes = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, newItem):
        self.itmes.append(newItem)

    def pop(self):
        return self.itmes.pop()

    def peek(self):
        return self.itmes[-1]

    def size(self):
        return len(self.itmes)

    def __str__(self):
        return str(self.itmes)


if __name__ == '__main__':
    stack = stack()
    print(stack)
    for i in range(3):
        stack.push(i)
    print(stack)

    print(f'peek top item: {stack.peek()}')
    print(f'pop one item: {stack.pop()}\nNow: {stack}')

### Note ###
# DS in which all insertion and deletions are made at one end, called "top of the stack"
# LIFO
# Common operation: push, pop, peek, is_empty
# Application: reverse Polish notation for evaluating arithmetic expressions,
#               syntax parsing, cold stack(space in CPU for param and local vars is created),
#               used in recursion, undo, redo operations, low-level assembly programming
