import chainlit as cl
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

def get_breathing_guide() -> str:
    return (
        "Let's relax with a breathing exercise:\n"
        "1. Inhale slowly through your nose (4 seconds)\n"
        "2. Hold your breath (4 seconds)\n"
        "3. Exhale slowly through your mouth (4 seconds)\n"
        "4. Repeat this cycle 3 times 🧘‍♀️"
    )

def get_journaling_prompt(mood: str) -> str:
    prompts = {
        "happy": "What made you feel happy today? How can you bring more of this into your life?",
        "sad": "What is weighing on your heart today? Can you name it and let it go?",
        "anxious": "What’s one small step you can take to feel more in control today?"
    }
    return prompts.get(mood, "Take a moment to reflect on how you're feeling right now.")

def get_response(mood: str) -> str:
    quote = get_motivational_quote()
    breathing = get_breathing_guide()
    journal = get_journaling_prompt(mood)
    return f"**Motivational Quote:**\n{quote}\n\n**Breathing Exercise:**\n{breathing}\n\n**Journaling Prompt:**\n{journal}"

@cl.on_chat_start
async def start():
    await cl.Message(content="Hi! I'm your Mental Fitness Buddy 🤗\nHow are you feeling today?\nChoose one: Happy 😊, Sad 😔, Anxious 😰").send()

@cl.on_message
async def on_message(message: cl.Message):
    mood = message.content.strip().lower()
    if mood not in ["happy", "sad", "anxious"]:
        await cl.Message(content="Please choose a valid mood: Happy, Sad, or Anxious.").send()
        return

    response = get_response(mood)
    await cl.Message(content=response).send()
    await cl.Message(content="Would you like to try again? Type a mood or 'exit' to quit.").send()