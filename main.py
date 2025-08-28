# RTFC-based system and user prompt for MindMate
def mindmate_rtfc_prompt(journal_entry, mood):
    """
    RTFC: Role, Task, Format, Context
    Role: You are an empathetic AI mental wellness assistant.
    Task: Analyze the user's journal entry and mood, then suggest a coping strategy or affirmation.
    Format: Respond in JSON with keys: journal_entry, mood, suggestion.
    Context: The user is seeking support for mental wellness and productivity.
    """
    system_prompt = (
        "You are an empathetic AI mental wellness assistant. "
        "Your job is to analyze a user's journal entry and mood, then suggest a coping strategy or affirmation. "
        "Respond in JSON with the following keys: journal_entry, mood, suggestion. "
        "The user is seeking support for mental wellness and productivity."
    )
    user_prompt = (
        f"journal_entry: '{journal_entry}'\n"
        f"mood: '{mood}'"
    )
    # For OpenAI Completion API, concatenate system and user prompt
    prompt = system_prompt + "\n" + user_prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=0.9,
        stop=["}"]
    )
    # Log the number of tokens used
    if hasattr(response, 'usage') and response.usage:
        print(f"Tokens used: {response.usage.get('total_tokens', 'N/A')}")
    else:
        print("Token usage information not available.")
    # Parse and return structured output
    import json
    try:
        text = response.choices[0].text.strip()
        if not text.endswith('}'): text += '}'
        result_json = json.loads(text)
        return result_json
    except Exception as e:
        print("Failed to parse JSON output:", e)
        print("Raw output:", response.choices[0].text.strip())
        return None
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def suggest_coping_strategy(journal_entry, mood):
    # Define the function schema for the LLM
    functions = [
        {
            "name": "suggest_coping_strategy",
            "description": "Suggest a coping strategy or affirmation based on the user's journal entry and mood.",
            "parameters": {
                "type": "object",
                "properties": {
                    "journal_entry": {"type": "string", "description": "The user's journal entry."},
                    "mood": {"type": "string", "description": "The user's current mood."},
                    "suggestion": {"type": "string", "description": "A coping strategy or affirmation."}
                },
                "required": ["journal_entry", "mood", "suggestion"]
            }
        }
    ]

    messages = [
        {"role": "system", "content": "You are an empathetic AI mental wellness assistant."},
        {"role": "user", "content": f"Journal entry: {journal_entry}\nMood: {mood}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",  # or "gpt-4-0613" if available
        messages=messages,
        functions=functions,
        function_call={"name": "suggest_coping_strategy"}
    )

    # Extract the function call arguments
    function_args = response.choices[0].message.get("function_call", {}).get("arguments", None)
    if function_args:
        import json
        args = json.loads(function_args)
        print(f"Tokens used: {response.usage.get('total_tokens', 'N/A')}")
        return args
    else:
        print("No function call detected.")
        return None

# Example usage for RTFC-based prompting
entry = "I feel overwhelmed with work and can't focus."
mood = "stressed"
result = mindmate_rtfc_prompt(entry, mood)
print(result)

# Example usage for suggest_coping_strategy function
result = suggest_coping_strategy(entry, mood)
print(result)