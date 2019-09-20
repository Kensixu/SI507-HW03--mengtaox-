import random
def my_function():
    question = input("What is your question?")
    return question

magic_answer = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes - definitely.", "You may rely on it.",
 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
 "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
 "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
answer = random.choice(magic_answer)

while True:
    quest = my_function()
    if quest[-1] == "?":
        print(answer)
        break
    elif quest == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
