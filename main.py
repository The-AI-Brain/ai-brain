import asyncio
import random
import openai_secret_manager
import openai


# Initialize the OpenAI API client
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]


# Array of human actions
actions = ["ate a sandwich", "played the piano", "went for a walk", "read a book", "watched TV"]


# Array of places for the actions
places = ["in the park", "at home", "in the library", "on the beach", "in the movie theater"]


# Asynchronous function to print actions every 5 seconds
async def print_actions(name):
    while True:
        action = random.choice(actions)
        place = random.choice(places)
        print(f"{name} {action} {place}")
        await asyncio.sleep(5)


# Asynchronous function to generate random sentence
async def generate_sentence(context):
    prompt = f"Generate a random sentence with a place for an action:\nContext: {context}\n{name}:"
    response = await asyncio.to_thread(openai.Completion.create,
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
        )
    message = response.choices[0].text.strip()
    return message


# Main function to run the program
async def main():
    # Get user input for name
    name = secrets["name"]
    
    # Read context from file
    with open("custom-context.txt", "r") as f:
        context = f.read().strip()
    
    # Initialize context with empty strings if file is empty
    if not context:
        context = ["", "", ""]
    else:
        context = context.split("\n")[-3:]
    
    # Start printing actions asynchronously
    asyncio.create_task(print_actions(name))
    
    # Start generating sentences and interacting with GPT-3 indefinitely
    while True:
        # Generate random sentence
        chatin = await generate_sentence(context)
        
        # Append sentence to context
        context.append(f"{name}: {chatin}")
        context = context[-3:]
        
        # Get response from GPT-3
        message = await asyncio.to_thread(openai.Completion.create,
            engine="davinci",
            prompt=f"Context: {context}\n{name}: {chatin}\n{name}:",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0,
            )
        message = message.choices[0].text.strip()
        
        # Append GPT-3 response to context
        context.append(f"{name}: {message}")
        context = context[-3:]
        
        # Print GPT-3 response
        print(f"{name}: {message}")


# Run the main function
asyncio.run(main())
