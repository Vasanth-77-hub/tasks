import random

# Function to get risk values based on user's choice
def get_risk_values(risk_level):
    if risk_level == "low":
        return 10, 1  # ₹10, win if user_roll > comp_roll
    elif risk_level == "medium":
        return 30, 2  # ₹30, win if user_roll >= comp_roll + 2
    elif risk_level == "high":
        return 60, 3  # ₹60, win if user_roll >= comp_roll + 3
    else:
        return None, None  # Invalid input

# Function to play one round
def play_round(risk_level):
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    reward, diff_required = get_risk_values(risk_level)

    if reward is None:
        print("Invalid risk level. Round skipped.")
        return 0, False, False, None, None

    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {comp_roll}")

    if user_roll >= comp_roll + diff_required:
        print(f"You win ₹{reward}!")
        return reward, True, False, user_roll, comp_roll
    else:
        print(f"You lose ₹{reward}.")
        return -reward, False, True, user_roll, comp_roll

# Main game function
def play_game():
    balance = 0
    wins = 0
    losses = 0

    rounds = int(input("Enter number of rounds to play: "))

    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        risk = input("Choose your risk (low/medium/high): ").strip().lower()

        round_result, win, lose, ur, cr = play_round(risk)
        if ur is not None:
            balance += round_result
            if win:
                wins += 1
            elif lose:
                losses += 1

    print("\n=== Game Over ===")
    print(f"Total Wins: {wins}")
    print(f"Total Losses: {losses}")
    print(f"Final Balance: ₹{balance}")

# Start the game
play_game()
