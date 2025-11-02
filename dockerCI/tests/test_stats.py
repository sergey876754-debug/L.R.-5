import pytest
from math_utils import mean, variance


def test_mean_basic():
    assert mean([1, 2, 3]) == 2


def test_variance_basic():
    assert pytest.approx(2 / 3) == variance([1, 2, 3])


def test_empty_mean_raises():
    with pytest.raises(ValueError):
        mean([])


def test_empty_variance_raises():
    with pytest.raises(ValueError):
        variance([])