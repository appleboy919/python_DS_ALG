# apply stack DS

import ch1_Stack.stack as stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.stack()

for c in string:
    s.push(c)

while s.size() != 0:
    reversed_string += s.pop()

print(reversed_string)