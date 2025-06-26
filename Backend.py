import random

USERS = {"player1": {"balance": 100}}
ADMINS = {"admin": "password123"}
REDEMPTIONS = []
SYMBOLS = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

def spin_slot(username):
    if username not in USERS:
        USERS[username] = {"balance": 100}
    user = USERS[username]
    if user["balance"] <= 0:
        return {"result": ["❌", "❌", "❌"], "win": 0, "balance": user["balance"]}

    user["balance"] -= 1
    result = [random.choice(SYMBOLS) for _ in range(3)]
    win = 10 if len(set(result)) == 1 else 0
    user["balance"] += win
    return {"result": result, "win": win, "balance": user["balance"]}

def admin_login(username, password):
    return ADMINS.get(username) == password

def redeem_user(username, amount):
    if username in USERS and USERS[username]["balance"] >= amount:
        USERS[username]["balance"] -= amount
        REDEMPTIONS.append({"username": username, "amount": amount, "status": "approved"})
        return "Redeemed"
    return "Redemption failed"

def get_redemptions():
    return REDEMPTIONS
