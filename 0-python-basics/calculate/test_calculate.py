from calculate import calculate


def test_calculate_():
    assert calculate(" 2 * 2 - ( 2 + 1 )") == 1.0


def test_calculate_sum_4():
    assert calculate("2 + 2") == 4
