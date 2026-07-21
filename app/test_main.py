import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeros if amount of cents is 0"
        ),
        pytest.param(
            1019,
            [4, 1, 1, 40],
            id="should return correct combination for big amount of cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return correct combination"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return correct combination"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return correct combination"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return correct combination"
        ),

    ]
)
def test_should_return_correct_combination(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            -20,
            ValueError,
            id="should raise 'ValueError' if amount of cents is negative"
        ),
        pytest.param(
            None,
            TypeError,
            id="should raise 'TypeError' if amount of cents id empty"
        ),
        pytest.param(
            "cent",
            TypeError,
            id="should raise 'TypeError' if cents type is wrong"
        ),
        pytest.param(
            1.3,
            TypeError,
            id="should raise 'TypeError' if cents type is wrong"
        )
    ]
)
def test_should_raise_expected_errors(
        cents: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
