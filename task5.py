# import random

# def play_die():
#     return random.choice(heads,tails)

# def play_game(rounds):
#     heads=0
#     tails=0
#     balance=0

# rounds =input(int("Enter the number of round you want to play"))

# for in range(rounds):
#     result = toss_coin()
#     print(f"Toss result: {result}")

#     # if result =='heads'
#     # heads=30
#     # tails=10
#     # balance=0
import random  # To simulate the coin toss

def toss_coin():
    return random.choice(['Heads', 'Tails'])  # Returns either 'Heads' or 'Tails' randomly

def play_game(rounds):
    balance = 0
    heads_count = 0
    tails_count = 0

    for _ in range(rounds):  # Loop for the number of rounds
        result = toss_coin()
        print(f"Toss result: {result}")  # Show result for each round

        if result == 'Heads':
            balance += 30
            heads_count += 1
        else:
            balance -= 10
            tails_count += 1

    return heads_count, tails_count, balance  # Final results

# Main program
rounds = int(input("Enter the number of rounds to play: "))
heads, tails, final_balance = play_game(rounds)

# Display results
print(f"\nTotal Heads: {heads}")
print(f"Total Tails: {tails}")
print(f"Final Balance: ₹{final_balance}")
