from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    try:
        assert get_coin_combination(1) == [1, 0, 0, 0]  # 1 пенні
        print("Ok!")
    except:
        print("Not ok!")
    try:
        assert get_coin_combination(6) == [1, 1, 0, 0]  # 1 пенні + 1 нікель
        print("Ok!")
    except:
        print("Not ok!")
    try:
        assert get_coin_combination(17) == [2, 1, 1, 0]  # 2 пенні + 1 нікель + 1 дайм
        print("Ok!")
    except:
        print("Not ok!")
    try:
        assert get_coin_combination(50) == [0, 0, 0, 2]  # 2 кварталі
        print("Ok!")
    except:
        print("Not ok!")


test_get_coin_combination()
