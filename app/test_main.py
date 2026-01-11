from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cat_year, result", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_cheking_values(cat_year: int,
                        result: list) -> None:
    func_result = get_coin_combination(cat_year)
    assert (get_coin_combination(cat_year) == result),\
        (f"Somothing wrong with cat calculate: "
         f"waited {result[0]}, get {func_result[0]}")
