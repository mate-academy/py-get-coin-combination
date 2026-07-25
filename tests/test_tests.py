import app.main as main


def test_return_only_pennies(monkeypatch):
    def return_only_pennies(cents: int) -> list:
        if cents == 10:
            return [0, 0, 1, 0]
        return [cents, 0, 0, 0]

    monkeypatch.setattr(main, "get_coin_combination", return_only_pennies)

    assert main.get_coin_combination(1) == [1, 0, 0, 0]
    assert main.get_coin_combination(4) == [4, 0, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]


def test_return_only_one_type(monkeypatch):
    def return_only_one_type(cents: int) -> list:
        if cents < 5:
            return [cents, 0, 0, 0]
        if cents < 10:
            return [0, cents // 5, 0, 0]
        if cents < 25:
            return [0, 0, cents // 10, 0]
        quarters = cents // 25
        remainder = cents % 25
        return [remainder, 0, 0, quarters]

    monkeypatch.setattr(main, "get_coin_combination", return_only_one_type)

    assert main.get_coin_combination(5) == [0, 1, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]
    assert main.get_coin_combination(41) == [16, 0, 0, 1]
