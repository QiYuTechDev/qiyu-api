from typing import Iterable


def gen_n(n: int) -> Iterable[int]:
    for i in range(n):
        yield from range(i)


def test_coroutine_simple():
    """
    测试 coroutine 函数
    :return:
    """
    for i in gen_n(4):
        print(i)
