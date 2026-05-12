print("ChatBot:")
print("Type \"Bye\" to exit")

while True:
    user  = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hi, how can i assist you?")

    elif "product" in user or "products" in user:
        print("Bot: Our product lineup contains laptops, smartphones, etc.")

    elif "price" in user:
        print("Bot: Our prices vary depending on the product")

    elif "contact" in user:
        print("Bot: You can contact us at support@gmail.com")

    elif "service" in user or "services" in user:
        print("Bot: We do provide Pan India Delivery and Service")

    elif "bye" in user:
        print("Bot: You're most welcome!")
        break
    
    else:
        print("Bot: Sorry, I don't understand")


    