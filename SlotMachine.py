import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    result = []

    for _ in range(3): 
        result.append(random.choice(symbols))
    return result  



def print_row(row, bet):
    print(" ".join(row))
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] ==  '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0  
    

def get_payout(row, bet):
    return print_row(row, bet) 

def main():
    balance = 100

    print("**************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("**************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print(f"Game over! Your final balance is ${balance}")


if __name__ == '__main__':
    main()