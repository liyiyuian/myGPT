import openai


# delete_all removes all running assistants
def delete_all():
    client = openai.OpenAI()
    my_assistants = client.beta.assistants.list(
            order="desc",
            limit="100",
            )
    if len(my_assistants.data) > 0:
        for a in my_assistants.data:
            response = client.beta.assistants.delete(a.id)
            print(response)
    else:
        print("> There is no running assistant.")
