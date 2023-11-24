import openai

messages = []


# Append the message to the conversation history
def add_message(role, message):
    messages.append({"role": role, "content": message})


def converse_with_chatGPT():
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        stream=True
    )

    print("GPT > ", end='')
    for part in response:
        if part:
            print(part.choices[0].delta.content or "", end='', sep=' ')
    print("\n", end='')


# process user prompt
def process_user_query(prompt):
    user_prompt = (f"{prompt}")
    add_message("user", user_prompt)
    converse_with_chatGPT()


# Request user to provide the query
def user_query():
    while True:
        prompt = input("You > ")
        # TODO: add exit option; 
        process_user_query(prompt)


