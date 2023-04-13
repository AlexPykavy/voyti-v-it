import re


def calculate(e: str) -> float:
    g = []
    nums = re.findall('[0-9]+', e)

    for i in nums:
        g.append(float(i))

    a = float(g[0])
    b = float(g[1])

    if "+" in e:
        return a+b

    if "-" in e:
        return a-b

    if "*" in e:
        return a*b

    if "/" in e:
        return a/b
