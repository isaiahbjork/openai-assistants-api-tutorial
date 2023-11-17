from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


# Step 1
def create_assistant():
    my_assistant = client.beta.assistants.create(
        instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        name="Math Tutor",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4",
    )
    print(my_assistant)

# create_assistant()


# Step 2
def create_thread():
    empty_thread = client.beta.threads.create()
    print(empty_thread)

# create_thread()


# Step 3
def create_message():
    thread_message = client.beta.threads.messages.create(
        "thread_id",
        role="user",
        content="What is the square root of 64?",
    )
    print(thread_message)

# create_message()

# Step 4
def run_assistant():
    run = client.beta.threads.runs.create(
        thread_id="thread_id", assistant_id="assistant_id"
    )
    print(run)

#run_assistant()

# Step 5
def retrieve_run():
    run = client.beta.threads.runs.retrieve(
        thread_id="thread_id",
        run_id="run_id"
    )
    print(run)

#retrieve_run()

# Step 6
def get_messages():
    thread_messages = client.beta.threads.messages.list("thread_id")
    print(thread_messages.data)

#get_messages()