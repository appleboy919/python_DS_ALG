# apply stack DS

import ch1_Stack.stack as stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.stack()

for c in string:
    s.push(c)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)