import openai

openai.api_key = "AIzaSyCWC-uxToNmYxsMgiNH_rF5QahPbhFu6ds"

def analyze_journal_entry(entry):
    prompt = (
        "Given the following journal entry, analyze the user's mood and suggest one personalized coping strategy or affirmation to improve their mental well-being. "
        f"Journal entry: '{entry}'"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Example usage
entry = "I feel overwhelmed with work and can't focus."
result = analyze_journal_entry(entry)
print(result)