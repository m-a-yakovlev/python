'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid.
That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''
def evalRPN(tokens: 'list[str]') -> int:
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(token))
    
    return stack[0]

