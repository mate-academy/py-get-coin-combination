from app.main import get_coin_combination
import pytest

parametrize_dict = {
    1: [1, 0, 0, 0], 6: [1, 1, 0, 0],
    17: [2, 1, 1, 0], 50: [0, 0, 0, 2]
}


def test_raise_error_when_cents_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents="1")


@pytest.mark.parametrize(
    "cents,expected",
    [(1, parametrize_dict[1]), (6, parametrize_dict[6]),
     (17, parametrize_dict[17]), (50, parametrize_dict[50])]
)
def test_can_get_absolute_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
