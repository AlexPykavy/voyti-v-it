from bin_search import bin_search
from bin_search_reс import bin_search_rec


def test_bin_search():
    assert bin_search(list=[2, 3, 4, 10, 40], x=10) == 3


def test_bin_search_rec():
    list = [2, 3, 4, 10, 40]
    assert bin_search_rec(list, low=0, high=len(list)-1, x=10) == 3
