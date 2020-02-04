import pytest
from functools import partial
from operator import mul

dobro= partial(mul, 2)

cem_decorator=pytest.mark.parametrize(
    'i',
    list(range(100))
)

@cem_decorator
def test_dobro(i):
    # for i in range(100):
    assert dobro(i) == i * 2

triplo = partial(mul, 3)

@cem_decorator
def test_triplo(i):
    # for i in range(100):
    assert triplo(i) == i * 3  