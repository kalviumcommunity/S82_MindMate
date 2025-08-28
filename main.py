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
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=0.9
    )
    # Log the number of tokens used
    if hasattr(response, 'usage') and response.usage:
        print(f"Tokens used: {response.usage.get('total_tokens', 'N/A')}")
    else:
        print("Token usage information not available.")
    # Parse and return structured output
    try:
        result_json = json.loads(response.choices[0].text.strip())
        return result_json
    except Exception as e:
        print("Failed to parse JSON output:", e)
        print("Raw output:", response.choices[0].text.strip())
        return None

# Example usage for one-shot prompting with structured output
entry = "I feel overwhelmed with work and can't focus."
mood = "stressed"
result = one_shot_prompt_structured(entry, mood)
print(result)