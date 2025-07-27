def get_journaling_prompt(mood: str) -> str:
    prompts = {
        "happy": "What made you feel happy today? How can you bring more of this into your life?",
        "sad": "What is weighing on your heart today? Can you name it and let it go?",
        "anxious": "What’s one small step you can take to feel more in control today?"
    }
    return prompts.get(mood, "Take a moment to reflect on how you're feeling right now.")
