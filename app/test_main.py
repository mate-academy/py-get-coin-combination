import pytest

from app.main import get_coin_combination


def return_date() -> None:
    return [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]


def gen_key(dataset: list) -> str:
    number, _ = dataset
    return f"test for number {number}"


@pytest.mark.parametrize("dataset",
                         return_date(),
                         ids=gen_key)
def test_func(dataset: list) -> None:
    number, expected = dataset
    assert get_coin_combination(number) == expected
