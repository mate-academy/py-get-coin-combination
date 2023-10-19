from app.main import get_coin_combination


class TestAmountOfPenny:

    def test_amount_of_penny_under_5(self) -> None:
        assert get_coin_combination(1) == [1, 0, 0, 0], (
            "wrong count of penny"
        )

    def test_amount_of_penny_with_nickels(self) -> None:
        assert get_coin_combination(6) == [1, 1, 0, 0], (
            "wrong count of penny"
        )

    def test_amount_of_penny_with_dimes(self) -> None:
        assert get_coin_combination(16) == [1, 1, 1, 0], (
            "wrong count of penny"
        )

    def test_amount_of_penny_with_quarters(self) -> None:
        assert get_coin_combination(41) == [1, 1, 1, 1], (
            "wrong count of penny"
        )


class TestAmountOfNickel:

    def test_amount_of_nickel(self) -> None:
        assert get_coin_combination(5) == [0, 1, 0, 0], (
            "wrong count of nickel"
        )

    def test_amount_of_nickel_with_dimes(self) -> None:
        assert get_coin_combination(15) == [0, 1, 1, 0], (
            "wrong count of nickel"
        )

    def test_amount_of_nickel_with_quarters(self) -> None:
        assert get_coin_combination(40) == [0, 1, 1, 1], (
            "wrong count of nickel"
        )


class TestAmountOfDime:

    def test_amount_of_dime(self) -> None:
        assert get_coin_combination(10) == [0, 0, 1, 0], (
            "wrong count of dime"
        )

    def test_amount_of_dime_with_quarters(self) -> None:
        assert get_coin_combination(35) == [0, 0, 1, 1], (
            "wrong count of dime"
        )


def test_right_amount_of_quarters() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1], (
        "wrong amount of quarters"
    )
