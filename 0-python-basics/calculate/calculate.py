# flake8: noqa: C901
def calculate(e: str) -> float:
    g = e.split()

    def precedence(op):

        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2

        return 0

    def calc(a, b, op):

        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return round(a / b, 1)

    def evaluate(g):
        stack = []
        ops = []
        i = 0

        while i < len(g):
            if g[i] == '(':
                ops.append(g[i])
            elif g[i] not in '+-/*()':
                stack.append(float(g[i]))
            elif g[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':

                    numb2 = stack.pop()
                    numb1 = stack.pop()
                    op = ops.pop()
                    stack.append(calc(numb1, numb2, op))

                ops.pop()
            else:
                while (len(ops) != 0 and precedence(ops[-1]) >= precedence(g[i])):

                    numb2 = stack.pop()
                    numb1 = stack.pop()
                    op = ops.pop()

                    stack.append(calc(numb1, numb2, op))

                ops.append(g[i])

            i += 1

        while len(ops) != 0:

            numb2 = stack.pop()
            numb1 = stack.pop()
            op = ops.pop()

            stack.append(calc(numb1, numb2, op))

        return stack[-1]

    return evaluate(g)
