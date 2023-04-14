from calculate import calculate


def test_calculate__sum_4():
    assert calculate(" 2 + 2") == 4.0


def test_calculate_2():
    assert calculate("2 + 2 * 3 + ( 2 + 6 )") == 16.0


def test_calculate_3():
    assert calculate("( ( 2 + 2 ) + 2 ) * 3 * ( 2 + 6 )") == 144.0


def test_calculate_4():
    assert calculate("2 / 4 * 3 * ( 6 + 2 )") == 12.0
