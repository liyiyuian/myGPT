from os import wait
import openai
import time

from openai.types.beta import assistant


# create a class for assistant
class Assistant:
    def __init__(self,
                 assistant=None,
                 message=None,
                 ans_instructions=None,
                 ofilename=None):
        # Initialize the client
        self.client = openai.OpenAI()

        self.message = message
        self.ans_instructions = ans_instructions
        self.ofilename = ofilename
        if assistant:
            self.create_thread()
            self.add_message(message=message)
            self.runjob = self.run(assistant_id=assistant.id)
            print(f"> Assistant {assistant.name} loaded and start running your request!")
            result = self.check_status()
            output = []
            for i, data in reversed(list(enumerate(result.data))):
                # print(i, data.content[0].text.value)
                output.append(f"{i}: {data.content[0].text.value.strip()}")
            self.output_md(output)

    def init_assistant(self, name, instructions, description, filepaths=None,
                       model="gpt-3.5-turbo-1106",
                       tools=[{"type": "retrieval"}],
                       ofilename=None):
        self.name = name
        self.instructions = instructions
        self.description = description
        self.filepaths = filepaths
        self.model = model
        self.tools = tools

        if ofilename:
            self.ofilename = ofilename
        self.create_file()
        self.assistant = self.create_assistant()
        self.create_thread()


    def create_file(self):
        files = []
        for file in self.filepaths:
            files.append(self.client.files.create(file=open(file, "rb"),
                                                  purpose='assistants'))
        self.files = files

    def create_assistant(self):
        # create file object #TODO: do i need to change rb based on filetype?

        # Create an Assistant
        fileid = []
        if self.files:
            for file in self.files:
                fileid.append(file.id)
        self.fileid = fileid

        # A list of file IDs attached to this assistant.
        # There can be a maximum of 20 files attached to the assistant.
        # Files are ordered by their creation date in ascending order.
        return self.client.beta.assistants.create(
                name=self.name,
                description=self.description,
                instructions=self.instructions,
                model=self.model,
                tools=self.tools,
                file_ids=fileid
                )

    # Create a Thread
    def create_thread(self):
        self.thread = self.client.beta.threads.create()

    # Add a Message to a Thread
    def add_message(self, message):
        return self.client.beta.threads.messages.create(thread_id=self.thread.id,
                                                        role="user",
                                                        content=message
                                                        )

    # Run the Assistant
    def run(self, assistant_id):
        """
        By default, a Run will use the model and tools configuration specified in
        Assistant object, but you can override most of these when creating the Run
        for added flexibility:

        run = client.beta.threads.runs.create(
          thread_id=thread.id,
          assistant_id=assistant.id,
          model="gpt-4-1106-preview",
          instructions="additional instructions",
          tools=[{"type": "code_interpreter"}, {"type": "retrieval"}]
        )

        Note: file_ids associated with the Assistant cannot be overridden
        during Run creation. You must use the modify Assistant endpoint to do this.
        """
        return self.client.beta.threads.runs.create(thread_id=self.thread.id,
                                                    assistant_id=assistant_id,
                                                    instructions=self.ans_instructions
                                                    )

    # If run is 'completed', get messages and print
    def check_status(self):
        while True:
            # Retrieve the run statusrun_status
            run_status = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id,
                                                                run_id=self.runjob.id)
            time.sleep(10)
            if run_status.status == 'completed':
                messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
                break
            else:
                # sleep again
                time.sleep(2)
        return messages

    def del_assistant(self):
        response = self.client.beta.assistants.delete(self.assistant.id)
        print(response)

    def del_file(self):
        for file in self.fileid:
            response = self.client.files.delete(file)
            print(response)

    def output_md(self, message):
        with open(self.ofilename, 'w') as file:
            for line in message:
                file.write(f"{line}\n")
