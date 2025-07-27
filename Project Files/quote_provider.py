import requests

def get_motivational_quote() -> str:
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            return f"{data[0]['q']} — {data[0]['a']}"
        else:
            return "Stay strong, the sun will rise again ☀️"
    except Exception:
        return "Keep going, you're doing better than you think 💪"
