def precedence(op):

    if op == '+' or op == '-':
        return 1

    if op == '*' or op == '/':
        return 2

    return 0


def calc(a, b, op):

    if op == '+':
        return a + b

    if op == '-':
        return a - b

    if op == '*':
        return a * b

    if op == '/':
        return round(a / b, 1)


def calculate(e: str) -> float:
    list = e.split()
    stack = []
    ops = []

    for tok in list:
        if tok == '(':
            ops.append(tok)

        elif tok == ')':
            while ops and ops[-1] != '(':

                numb2 = stack.pop()
                numb1 = stack.pop()
                op = ops.pop()

                stack.append(calc(numb1, numb2, op))

            ops.pop()

        elif tok in '+-/*':
            while ops and precedence(ops[-1]) >= precedence(tok):        #while ops similar while ops != 0 

                numb2 = stack.pop()
                numb1 = stack.pop()
                op = ops.pop()

                stack.append(calc(numb1, numb2, op))

            ops.append(tok)

        else:
            stack.append(float(tok))

    while len(ops) != 0:

        numb2 = stack.pop()
        numb1 = stack.pop()
        op = ops.pop()

        stack.append(calc(numb1, numb2, op))

    return stack[-1]
