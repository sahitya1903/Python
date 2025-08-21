def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

expression = "a+b*(c^d-e)^(f+g*h)-i"
print(infix_to_postfix(expression))  # Output: abcd^e-fgh*+^*+i-

def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    # Reverse the infix expression
    expression = expression[::-1]

    # Replace '(' with ')' and vice versa
    expression = expression.replace('(', 'temp')
    expression = expression.replace(')', '(')
    expression = expression.replace('temp', ')')

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] < precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    # Reverse the output to get the prefix expression
    return ''.join(output[::-1])

expression = "a+b*(c^d-e)^(f+g*h)-i"
print(infix_to_prefix(expression))  # Output: -+a*b^-^cde+f*ghi
