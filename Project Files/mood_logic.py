from quote_provider import get_motivational_quote
from breathing_guide import get_breathing_guide
from journal_prompts import get_journaling_prompt

def get_response(mood: str) -> str:
    quote = get_motivational_quote()
    breathing = get_breathing_guide()
    journal = get_journaling_prompt(mood)
    return f"**Motivational Quote:**\n{quote}\n\n**Breathing Exercise:**\n{breathing}\n\n**Journaling Prompt:**\n{journal}"
