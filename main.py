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

def dynamic_prompt(journal_entry, mood):
    prompt = (
        f"Given the following journal entry: '{journal_entry}', and the user's current mood: '{mood}', "
        "suggest a personalized coping strategy or affirmation to improve their mental well-being."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=0.9
    )
    # Log the number of tokens used
    if hasattr(response, 'usage') and response.usage:
        print(f"Tokens used: {response.usage.get('total_tokens', 'N/A')}")
    else:
        print("Token usage information not available.")
    return response.choices[0].text.strip()



# One-shot prompting function with structured (JSON) output
import json
def one_shot_prompt_structured(journal_entry, mood):
    example = (
        "Example (respond in JSON):\n"
        "{\n"
        "  \"journal_entry\": \"I feel anxious about my exams.\",\n"
        "  \"mood\": \"anxious\",\n"
        "  \"suggestion\": \"Take a few deep breaths and remind yourself that preparation is key. Try a short meditation to calm your mind.\"\n"
        "}\n\n"
    )
    prompt = (
        example +
        f"Now, given the following journal entry and mood, respond in the same JSON format.\n"
        f"journal_entry: '{journal_entry}'\n"
        f"mood: '{mood}'\n"
    )
    # Note: OpenAI's API does not support top_k. Only top_p and temperature are available.
    # If using HuggingFace Transformers, you could use top_k like this:
    # output = model.generate(input_ids, top_k=50, top_p=0.9, temperature=0.7)

    # For OpenAI API, you can only set top_p and temperature:
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
    try:
        # Add the closing brace if the stop sequence cuts it off
        text = response.choices[0].text.strip()
        if not text.endswith('}'):
            text += '}'
        result_json = json.loads(text)
        return result_json
    except Exception as e:
        print("Failed to parse JSON output:", e)
        print("Raw output:", response.choices[0].text.strip())
        return None

# Example usage for RTFC-based prompting
entry = "I feel overwhelmed with work and can't focus."
mood = "stressed"
result = mindmate_rtfc_prompt(entry, mood)
print(result)