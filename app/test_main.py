def get_coin_combination(cents: int) -> list[int]:
    quarters: int = cents // 25
    cents %= 25

    dimes: int = cents // 10
    cents %= 10

    nickels: int = cents // 5
    cents %= 5

    pennies: int = cents

    return [pennies, nickels, dimes, quarters]
  
