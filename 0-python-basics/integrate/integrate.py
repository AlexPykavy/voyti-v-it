from typing import Callable, Tuple


def integrate(f: Callable[float, float], interval: Tuple[float, float]) -> float:
    step = 0.001
    a, b = interval
    n = int((b - a) / step)

    return sum(f(a + i * step) * step for i in range(n))
