import pytest
from app import main


@pytest.mark.parametrize(
    "cents",
    [
        2.4,
        [7],
        "5",
        "60",
        True,
        (4, 6),
        {"cents": 4},
    ],
)
def test_data_input_is_integer(
    cents: int,
) -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [
        -5,
        -23,
        0,
    ],
)
def test_data_input_is_positive(
    cents: int,
) -> None:
    with pytest.raises(ValueError):
        main.get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (83, [3, 1, 0, 3]),
    ],
)
def test_get_coin_combination_return_values(cents: int, result: list) -> None:
    assert main.get_coin_combination(cents) == result, (
        f"The combination of the smallest possible number of coins "
        f"to give the amount {cents} is {result}"
    )


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, 4),
        (6, 4),
        (17, 4),
    ],
)
def test_animal_age_to_human_years(cents: int, result: int) -> None:
    assert (
        len(main.get_coin_combination(cents)) == result
    ), f"The function has to returned a {result} elements list "
