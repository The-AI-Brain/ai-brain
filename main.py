import asyncio
import random
import openai_secret_manager
import openai
import os
import requests
import subprocess
import datetime
import sys

compEmote = ""
extraContext = ""

# Define URLs for requirements.txt and main.py
REQS_URL = 'https://raw.githubusercontent.com/The-AI-Brain/ai-brain/main/requirements.txt'
MAIN_URL = 'https://raw.githubusercontent.com/The-AI-Brain/ai-brain/main/main.py'

# Define paths for local requirements.txt and main.py files
REQS_PATH = 'requirements.txt'
MAIN_PATH = 'main.py'

# Read context from file
with open("custom-context.txt", "r") as f:
    extraContext = f.read().strip()

# Initialize context with empty strings if file is empty
context: List[str] = []
context += [""] * (9 - len(context))

# Check for updates
def check_updates():
    # Download remote requirements.txt file
    remote_reqs = requests.get(REQS_URL).text
    
    # Compare local and remote requirements.txt files
    with open(REQS_PATH, 'r') as f:
        local_reqs = f.read()
        
    if local_reqs != remote_reqs:
        # Install updated requirements
        subprocess.run(['pip', 'install', '-r', REQS_PATH])
        
        # Download updated main.py file
        remote_main = requests.get(MAIN_URL).text
        
        # Write updated main.py file
        with open(MAIN_PATH, 'w') as f:
            f.write(remote_main)
        
        # Restart the script
        os.execv(sys.argv[0], sys.argv)


# Initialize the OpenAI API client
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]
max_year = datetime.datetime.now().year
year = min(int(secrets["year"]), max_year)

emotions = [
    "happy", "sad", "angry", "surprised", "disgusted", "fearful",
    "excited", "nostalgic", "hopeful", "anxious", "relaxed", "curious",
    "confused", "amused", "bored", "ecstatic", "exhausted", "grateful",
    "guilty", "embarrassed", "envious", "proud", "ashamed", "content",
    "depressed", "fascinated", "frustrated", "inspired", "irritated",
    "jealous", "lonely", "melancholic", "optimistic", "overwhelmed",
    "peaceful", "playful", "reflective", "remorseful", "restless",
    "satisfied", "sympathetic", "tense", "terrified", "triumphant",
    "uncomfortable", "vulnerable", "wistful", "yearning", "zealous"
]

actionsEmote = [
    "dancing", "singing", "laughing", "crying", "smiling", "frowning",
    "jumping", "running", "walking", "writing", "drawing", "painting",
    "playing", "reading", "cooking", "eating", "sleeping", "dreaming",
    "working", "learning", "teaching", "helping", "listening", "talking",
    "watching", "observing", "meditating", "praying", "driving", "riding",
    "flying", "swimming", "diving", "hiking", "camping", "travelling",
    "exploring", "adventuring", "competing", "collaborating", "creating",
    "designing", "programming", "testing", "debugging", "fixing", "building",
    "repairing", "upgrading", "maintaining", "cleaning", "organizing"
]

async def printEmote():
    while True:
        emote = random.choice(emotions)
        action = random.choice(actionsEmote)
        compEmote = f"I feel {emote} when {action}."
        context = context + compEmote
        # print(compEmote) # DEBUGGING
        await asyncio.sleep(7)

asyncio.run(printEmote())

# Array of human actions
actions = [
    "walked the dog",
    "cooked dinner",
    "read a book",
    "went swimming",
    "played soccer",
    "listened to music",
    "watched a movie",
    "painted a picture",
    "wrote a story",
    "rode a bike",
    "danced in the rain",
    "visited a museum",
    "went on a road trip",
    "went to a concert",
    "built a sandcastle",
    "went to the beach",
    "played video games",
    "climbed a mountain",
    "played with a pet",
    "went for a run",
    "did yoga",
    "went camping",
    "visited a new city",
    "went to a party",
    "took a nap",
    "had a picnic",
    "played a musical instrument",
    "tried a new food",
    "went on a hike",
    "took a bath",
    "visited a friend",
    "went to a theme park",
    "went to a zoo",
    "went to a sporting event",
    "went to a play",
    "went to a comedy show",
    "went to a ballet",
    "went to a musical",
    "went to a poetry reading",
    "went to a book club meeting",
    "went to a cooking class",
    "went to a painting class",
    "went to a wine tasting",
    "went to a beer festival",
    "went to a farmers' market",
    "went to a flea market",
    "went shopping",
    "went to a garage sale",
    "went to a thrift store",
    "volunteered at a charity",
    "went to a political rally",
    "went to a religious service",
    "attended a wedding",
    "attended a funeral",
    "graduated from school",
    "started a new job",
    "retired from a job",
    "got married",
    "got divorced",
    "had a baby",
    "raised a child",
    "adopted a pet",
    "moved to a new city",
    "bought a house",
    "rented an apartment",
    "remodeled a home",
    "gardened",
    "landscaped a yard",
    "went on a cruise",
    "went on a safari",
    "went on a skiing trip",
    "went on a snowboarding trip",
    "went on a fishing trip",
    "went on a hunting trip",
    "went on a scuba diving trip",
    "went on a surfing trip",
    "went on a kayaking trip",
    "went on a canoeing trip",
    "went on a rafting trip",
    "went on a hot air balloon ride",
    "went on a helicopter ride",
    "went on a plane ride",
    "went on a train ride",
    "went on a road trip",
    "went skydiving",
    "went bungee jumping",
    "went zip lining",
    "went rock climbing",
    "went to a spa",
    "got a massage",
    "got a facial",
    "got a manicure",
    "got a pedicure",
    "went to a chiropractor",
    "went to a physical therapist",
    "went to a dentist",
    "went to a doctor",
    "got surgery",
    "recovered from an illness",
    "overcame an addiction",
    "learned a new skill",
    "learned a new language",
    "took a class",
    "ate",
    "played the piano",
    "went for a walk"
]


# Array of places for the actions
places = [
    "in the park",
    "at home",
    "in the library",
    "on the beach",
    "in the movie theater",
    "at the doctor's office",
    "at school",
    "at the spa",
    "at the airport",
    "at the gym",
    "in a cafe",
    "in a museum",
    "in a grocery store",
    "in a restaurant",
    "at a concert",
    "at a stadium",
    "in a hospital",
    "in a church",
    "in a mosque",
    "in a temple",
    "in a theater",
    "in a nightclub",
    "in a casino",
    "at a zoo",
    "at a theme park",
    "at a water park",
    "in a shopping mall",
    "in a department store",
    "at a gas station",
    "in a parking lot",
    "in a hotel",
    "in a motel",
    "in a hostel",
    "in a campground",
    "in a forest",
    "on a mountain",
    "in a desert",
    "in a valley",
    "by a river",
    "by a lake",
    "at sea",
    "in the ocean",
    "in a cave",
    "at a train station",
    "at a bus station",
    "at a subway station",
    "at a ferry terminal",
    "at a harbor",
    "in a space station",
    "in a laboratory"
]



# Asynchronous function to print actions every 5 seconds
async def print_actions(name):
    while True:
        action = random.choice(actions)
        place = random.choice(places)
        complete = f"{name} {action} {place} in the year {year}"
        #print(complete) #DEBUG
        context.append(complete)
        return complete
        


# Asynchronous function to generate random sentence
async def generate_sentence(context):
    prompt = f"Generate a random sentence with the context:\nContext:{context}\nExtra context:${extraContext}\n{name}:"
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
    
    # Start printing actions asynchronously
    asyncio.create_task(print_actions(name))
    
    # Start generating sentences and interacting with GPT-3 indefinitely
    while True:
        check_updates()
        # Generate random sentence
        chatin = await generate_sentence(context)
        
        # Append sentence to context
        context.append(f"{name}: {chatin}")
        context = context[-3:]
        
        # Get response from GPT-3
        message = await asyncio.to_thread(openai.Completion.create,
            engine="davinci",
            prompt=f"Context: {context}\nExtra context: {extraContext}\n{name}: {chatin}\n{name}:",
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
        context = context[-9:]
        
        # Print GPT-3 response and what it said
        print(f"{name}: {chatin}")
        print(f"{name}: {message}")


# Run the main function
asyncio.run(main())
