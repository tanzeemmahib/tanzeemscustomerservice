import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

with open("prompts/customer_service_prompt.txt", "r") as f:
    base_prompt = f.read()

def get_response(user_input):
    """Generate AI response based on user input."""
    prompt = f"{base_prompt}\nCustomer: {user_input}\nAssistant:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5-like model
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=1,
        n=1,
        stop=["Customer:", "Assistant:"]
    )
    
    return response.choices[0].text.strip()

def chat():
    print("Customer Service AI (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break
        answer = get_response(user_input)
        print(f"Assistant: {answer}")

if __name__ == "__main__":
    chat()
