# add_test.py
from src.add import add


def test_add_positive():
    # test_で始まっているのでテストとして実行される
    assert add(1, 2) == 3


def not_a_test():
    # test_で始まっていないのでテストとして実行されない
    assert add(10, 20) == 30
