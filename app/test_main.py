from app.main import get_coin_combination


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),     # pennies
        (5, [0, 1, 0, 0]),     # nickel
        (10, [0, 0, 1, 0]),    # dime
        (25, [0, 0, 0, 1]),    # quarter
        (6, [1, 1, 0, 0]),     # mixed: penny + nickel
        (17, [2, 1, 1, 0]),    # mixed: penny + nickel + dime (з прикладу)
        (50, [0, 0, 0, 2]),    # multiple quarters (з прикладу)
        (4, [4, 0, 0, 0]),     # boundary before nickel
        (9, [4, 1, 0, 0]),     # boundary before dime
        (24, [4, 0, 2, 0]),    # boundary before quarter
        (26, [1, 0, 0, 1]),    # after quarter
        (99, [4, 0, 2, 3]),    # bigger combined case
    ],
)
def test_coin_combinations(cents, expected):
    assert get_coin_combination(cents) == expected