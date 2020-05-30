"""

Stack Data Structures


D
C
B
A

to access A , take D out first then C and so on. 
this is called popping 
A B C D

to push on stack:

D
C
B
A

Take note of push and pop
"""
"""

class Stack():
    def __init__(self):
        self.items = [] 
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == [] #Stack.is_empty() returns true if items is empty list as == is boolean operator
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")

print(s.get_stack())


s.push("C")
print(s.get_stack())

s.pop()

print(s.get_stack())
s.pop()
s.pop()
print(s.is_empty()) #True because list is empty
s.push("A")
print(s.is_empty())
s.push('B')
s.push('C')
s.push('D')
print(s.peek()
"""


"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.

Example:

    (), ()(), (({[]}))  <- Balanced.

    ((), {{{)}], [][]]] <- Not Balanced.

Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""
#MY CODE:
user_input = input('Enter the parantheses: ') #inputs parantheses
length_input = len(user_input) #length -1 as index starts from 0

#This function checks for the opposite parantheses
def opp_paran(p):
    if p == '(':
        return ')'
    elif p == '{':
        return '}'
    elif p == '[':
        return ']'
    
#Checks balance of user input
def check_balance(user_input, length_input):
    if length_input % 2 == 0:
        for i in range(length_input):
            if i<length_input//2:
                if user_input[length_input - i - 1] != opp_paran(user_input[i]):
                    return False
            else:
                return True
    else:
        return True


if check_balance(user_input, length_input):
    print('Balanced.')
else:
    print('Not Balanced.')

#Given Answer:

