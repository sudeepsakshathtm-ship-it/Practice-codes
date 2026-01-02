"""
Rock–Paper–Scissor: 5-round scoreboard version
"""

import random

item_list = ["Rock", "Paper", "Scissor"]

def decide_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"
    if user_choice == "Rock":
        return "User" if comp_choice == "Scissor" else "Computer"
    if user_choice == "Paper":
        return "User" if comp_choice == "Rock" else "Computer"
    if user_choice == "Scissor":
        return "User" if comp_choice == "Paper" else "Computer"

wins = {"User": 0, "Computer": 0, "Tie": 0}
history = []  # (round, user, comp, result)

for r in range(1, 6):  # exactly 5 rounds
    # --- input (case-insensitive + validation) ---
    while True:
        raw = input(f"Round {r} - Enter your move (Rock, Paper, Scissor): ").strip()
        user_choice = raw.capitalize()
        if user_choice in item_list:
            break
        print("Invalid choice. Please type exactly Rock, Paper, or Scissor.")

    comp_choice = random.choice(item_list)
    result = decide_winner(user_choice, comp_choice)
    history.append((r, user_choice, comp_choice, result))
    wins[result] += 1

    # per-round feedback
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
    if result == "Tie":
        print("Result: Tie")
    elif result == "User":
        print(f"Result: {user_choice} beats {comp_choice} — You win this round!")
    else:
        print(f"Result: {comp_choice} beats {user_choice} — Computer wins this round!")
    print("-" * 50)

# --- summary ---
print("\n=== MATCH SUMMARY ===")
for r, u, c, res in history:
    print(f"Round {r}: You={u}, Computer={c} -> {res}")

print("\nScores:")
print(f"You: {wins['User']} | Computer: {wins['Computer']} | Ties: {wins['Tie']}")

if wins["User"] > wins["Computer"]:
    print("\n🏆 Overall Winner: YOU")
elif wins["User"] < wins["Computer"]:
    print("\n🏆 Overall Winner: COMPUTER")
else:
    print("\n🤝 Overall Result: TIE")
