import random

def roll_die():
    return random.randint(1, 6)

def play_game(rounds):
    balance = 0
    even = 0
    odd = 0
    for _ in range(rounds):
        roll = roll_die()
        if roll % 2 == 0:
            balance += 50
            even += 1
        else:
            balance -= 20
            odd += 1
    return even, odd, balance

rounds = int(input("Enter number of rounds: "))
even, odd, balance = play_game(rounds)
print(f"Even rolls: {even}, Odd rolls: {odd}")
print(f"Final balance: ₹{balance}")
