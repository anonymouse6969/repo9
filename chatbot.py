print("This is a customer support chatbot :)")
print("Type \"Bye\" to exit")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hey there! How can i help you?")
    
    elif "product" in user or "products" in user:
        print("Bot: We sell laptops, smartphones, etc.")
    
    elif "bye" in user:
        print("See You!")
        break

    else:
        print("Bot: Sorry, nahi samjha :( \nBot: Try Again with some valid input...")