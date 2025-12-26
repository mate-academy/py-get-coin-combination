from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("coiin, total", [
    # when coin is 1
    (1, [1, 0, 0, 0]),
    # when coin is 5
    (5, [0, 1, 0, 0]),
    # when coin is 10
    (10, [0, 0, 1, 0]),
    # when coin is 25
    (25, [0, 0, 0, 1]),
    # when coin is 0
    (0, [0, 0, 0, 0]),
    # when coin too big
    (1872, [2, 0, 2, 74]),
    # when coin less 0
    (-17, [3, 1, 0, -1])])
def test_universal_tests(coiin: int, total: list) -> None:
    result = get_coin_combination(coiin)
    assert result == total


def test_type_error() -> None:
    cent = []
    with pytest.raises(TypeError):
        get_coin_combination(cent)
