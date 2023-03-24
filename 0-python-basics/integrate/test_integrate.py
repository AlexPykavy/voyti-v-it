from integrate import integrate


def test_integrate_x_pow2():
    assert round(integrate(lambda x: x**2, (0, 2))), 3 == 2.665
