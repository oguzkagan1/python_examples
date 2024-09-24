"""Functions for calculating steps in exchanging currency"""

def exchange_money(budget, exchange_rate):

    return budget / exchange_rate


def get_change(budget, exchanging_value):

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):

    return amount // denomination


def get_leftover_of_bills(amount, denomination):

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_ratio = spread / 100
    adjusted_rate = exchange_rate * (1 + spread_ratio)
    total_value = budget / adjusted_rate
    max_value = int(total_value // denomination * denomination)

    return max_value

print("Estimate Value After Exchange:", exchange_money(127.5, 1.2), "\n",
      "Calculate Currency Left After An Exchange:", get_change(127.5, 120), "\n",
      "Calculate Value Of Bills:", get_value_of_bills(5, 128), "\n",
      "Calculate Number Of Bills:", get_number_of_bills(127.5, 5), "\n",
      "Calculate Leftover After Exchanging Into Bills:", get_leftover_of_bills(127.5, 20), "\n",
      "Calculate Value After exchange:", exchangeable_value(127.25, 1.20, 10, 20))
