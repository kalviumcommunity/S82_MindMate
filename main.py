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
        temperature=0.7
    )
    # Log the number of tokens used
    if hasattr(response, 'usage') and response.usage:
        print(f"Tokens used: {response.usage.get('total_tokens', 'N/A')}")
    else:
        print("Token usage information not available.")
    return response.choices[0].text.strip()

# Example usage
entry = "I feel overwhelmed with work and can't focus."
mood = "stressed"
result = dynamic_prompt(entry, mood)
print(result)