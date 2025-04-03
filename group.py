from google import genai

client = genai.Client(api_key="AIzaSyA-hHDr3567dc7Z_nD4TTPm6Z445l3nKOE")

# First three prompts
prompts = [
    "Explain the concept of artificial intelligence in simple terms",
    "What are the main applications of AI in today's world?",
    "Describe the potential future developments in AI technology"
]

responses = []

# Get responses for each prompt
for prompt in prompts:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    responses.append(response.text)
    print(f"Response to '{prompt}':\n{response.text}\n")

# Combine all responses into one final prompt
final_prompt = """I've gathered some information about AI. Here are the responses:
1. """ + responses[0] + """
2. """ + responses[1] + """
3. """ + responses[2] + """

Based on all this information, can you create a comprehensive overview of artificial intelligence, its current uses, and future potential?"""

# Get final response
final_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=final_prompt
)

print("\nFinal comprehensive response:")
print(final_response.text)