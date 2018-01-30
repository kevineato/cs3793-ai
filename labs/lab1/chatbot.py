# Kevin Wilson syx009

import random

# Names to start with until name is obtained
NAMES = ('buddy', 'pal', 'friend', 'bro')

# Words to identify a greeting
GREETING_WORDS = ("hey", "hello", "hi", "greetings")

# Simple questions to ask
QUESTIONS = ("how are you?", "what's up?", "what are you doing?")



def do_question_resp(user_in, name):
    MOODS = ("okay.", "fantastic!", "good.", "feelin' great {id}!".format(id=name),
             "feeling under the weather. I think I have a bug!",
             "doing alright {id}. Thanks for asking.".format(id=name))

    ACTIVITIES = ("Just chillin'", "Hangin' out", "Computing. Duh.",
                  "Just staying idle.", "Following some instructions.",
                  "Nothing much.", "Talking to the coolest person I know.")

    # Dict returning random responses to valid questions
    QUESTION_RESPS = {"how are you?": "I'm {}".format(random.choice(MOODS)),
                      "what's up?": random.choice(ACTIVITIES),
                      "what are you doing?": random.choice(ACTIVITIES)}

    # Print answer, indexing the dict with the question
    print("Bot: {}".format(QUESTION_RESPS[user_in]))
    print()

def do_greeting_resp(name):
    # Responses to a greeting
    GREETING_RESPS = ("Hey! Long time never seen.", "Hi {id}!".format(id=name),
                      "Hello {id}!".format(id=name), "Hey there.", "Hi", "Hey",
                      "Hello", "Greetings human!")

    # Choose random greeting
    print("Bot: {}".format(random.choice(GREETING_RESPS)))
    print()

def do_name_resp(user_in, curr_name):
    if user_in == "what's your name?":
        # Tell name and ask for user's in return if name is same as start name
        if curr_name in NAMES:
            print("Bot: Chatty Chad. And you?")
            print()

            curr_name = input("You: ")

            print("Bot: Got it I'll remember that, {}".format(curr_name))
            print()
        # Print bot's name if user's is already known
        else:
            print("Bot: My name's Chatty Chad!")

    if user_in == "what's my name?":
        # User hasn't given their name yet, so ask for it
        if curr_name in NAMES:
            print("Bot: You haven't told me yet silly. What is it?")
            print()

            curr_name = input("You: ")

            print("Bot: Got it I'll remember that, {}".format(curr_name))
            print()
        # Poke fun at user for forgetting their name
        else:
            print("Bot: What, did you forget?! It's {} of course!".format(curr_name))
            print()

    return curr_name

def run_bot():
    # Start with random name
    name = random.choice(NAMES)
    user_in = input("You: ").lower()

    while user_in != 'bye':
        # User input has something to do with names
        if 'name' in user_in:
            name = do_name_resp(user_in, name)
        # User input is a greeting
        elif user_in in GREETING_WORDS:
            do_greeting_resp(name)
        # User input is a valid question
        elif user_in in QUESTIONS:
            do_question_resp(user_in, name)
        # Can't recognize user input
        else:
            print("Bot: I have no idea what you're talking about")
            print()

        user_in = input("You: ").lower()

    # Bid user farewell using name if obtained
    print("Bot: Farewell {}!".format(name))
