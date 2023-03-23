from integrate import integrate


def test_integrate_x_pow2():
    assert integrate(lambda x: x**2, (0, 2)) == 2.6646670000000015
