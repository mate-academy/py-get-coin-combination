from app.main import get_coin_combination
import pytest


def test_must_return_two_elements() -> None:
    assert len(get_coin_combination(10)) == 4


def test_all_elements_of_return_array_must_be_int() -> None:
    for coin in get_coin_combination(20):
        assert isinstance(coin, int)


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="if cents == 1"),
        pytest.param(6, [1, 1, 0, 0], id="if cents == 6"),
        pytest.param(17, [2, 1, 1, 0], id="if cents == 17"),
        pytest.param(50, [0, 0, 0, 2], id="if cents == 50"),
    ]
)
def test_converted_to_human_years(
        cents: int,
        expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result
