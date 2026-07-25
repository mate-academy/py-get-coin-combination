import pytest
import app.main as main  # import do módulo, não da função


@pytest.mark.parametrize("cents, expected", [
    # Zero
    (0, [0, 0, 0, 0]),

    # Fronteira de cada moeda
    (1, [1, 0, 0, 0]),    # mínimo de penny
    (4, [4, 0, 0, 0]),    # máximo antes do nickel
    (5, [0, 1, 0, 0]),    # vira nickel
    (9, [4, 1, 0, 0]),    # máximo antes do dime
    (10, [0, 0, 1, 0]),   # vira dime
    (24, [4, 0, 2, 0]),    # máximo antes do quarter
    (25, [0, 0, 0, 1]),   # vira quarter

    # Combinações mistas
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (41, [1, 1, 1, 1]),   # uma de cada
    (99, [4, 0, 2, 3]),   # valor grande
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


def test_raises_on_wrong_type() -> None:
    with pytest.raises((TypeError, ValueError)):
        main.get_coin_combination("hundred")
