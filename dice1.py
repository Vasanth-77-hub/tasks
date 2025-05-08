# import random

# # Step 1: Get number of rounds from user
# rounds = int(input("Enter number of rounds you want to play: "))

# # Step 2: Initialize counters
# total_money = 0
# win_count = 0

# # Step 3: Play the game for the given number of rounds
# for round_number in range(1, rounds + 1):
#     print(f"\nRound {round_number}:")
#     dice = random.randint(1, 6)
#     print(f"You rolled a {dice}.")

#     if dice == 3:
#         print("You won ₹100!")
#         total_money += 100
#         win_count += 1
#     else:
#         print("No prize this round.")

# # Step 4: Final results
# print("\nGame Over!")
# print(f"You won ₹{total_money} in total.")
# print(f"You won {win_count} time(s).")


import random

def play_die():
    return random.randint(1, 6)

def play_game(rounds):
    money = 0
    wins = 0
    for _ in range(rounds):
        if play_die() == 3:
            money += 100
            wins += 1
    return money, wins

rounds = int(input("Enter number of die: "))
money, wins = play_game(rounds) 
print(f"You won ₹{money} in total and won {wins} time(s).")
