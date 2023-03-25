from calculate import calculate


def test_calculate__sum_4():
    assert calculate("2+2") == 4.0


def test_calculate_with_sub_10():
    assert calculate("20-10") == 10.0


def test_calculate_with_mult_100():
    assert calculate("10*10") == 100.0


def test_calculate_with_div_50():
    assert calculate("500/10") == 50.0
