from app.your_module import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",  # один рядок з комою
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents, expected):
    assert get_coin_combination(cents) == expected
   
