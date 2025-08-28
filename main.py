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


# One-shot prompting function
def one_shot_prompt(journal_entry, mood):
    example = (
        "Example:\n"
        "Journal entry: 'I feel anxious about my exams.'\n"
        "Mood: 'anxious'\n"
        "Suggestion: Take a few deep breaths and remind yourself that preparation is key. Try a short meditation to calm your mind.\n\n"
    )
    prompt = (
        example +
        f"Now, given the following journal entry: '{journal_entry}'\n"
        f"Mood: '{mood}'\n"
        "Suggestion:"
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

# Example usage for one-shot prompting
entry = "I feel overwhelmed with work and can't focus."
mood = "stressed"
result = one_shot_prompt(entry, mood)
print(result)