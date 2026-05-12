print("Customer Support Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "product" in user:
        print("Bot: We sell laptops, phones, and accessories.")

    elif "service" in user:
        print("Bot: We provide delivery and repair services.")

    elif "price" in user:
        print("Bot: Prices vary depending on the product.")

    elif "contact" in user:
        print("Bot: You can contact us at support@gmail.com")

    elif "bye" in user:
        print("Bot: Thank you for visiting!")
        break

    else:
        print("Bot: Sorry, I don't understand.")