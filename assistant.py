import ollama

print("AI Coding Assistant (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": user_input}]
    )

    print("\nAI:", response["message"]["content"])
    print()