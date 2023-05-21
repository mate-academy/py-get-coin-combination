import pytest

from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert isinstance(get_coin_combination(50), list)


def test_should_return_list_of_4_elements() -> None:
    assert len(get_coin_combination(50)) == 4


@pytest.mark.parametrize(
    "cents",
    [50, 70, 80, 100, 120, 200, 250]
)
def test_should_return_quarters_if_count_of_cents_over_25(cents: int) -> None:
    assert get_coin_combination(cents)[3] > 0


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (87, [2, 0, 1, 3])
    ]
)
def test_should_return_correct_answer(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result
