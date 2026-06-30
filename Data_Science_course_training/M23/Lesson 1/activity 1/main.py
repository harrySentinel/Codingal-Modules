"""
Dialogflow Chatbot Setup — Step by Step

Step 1: Go to https://dialogflow.cloud.google.com and sign in with your Google account.

Step 2: Click "Create Agent". Give it a name like "MyChatbot", select your language as English,
        and pick your Google project. Hit Create.

Step 3: Once inside, go to "Intents" from the left menu. You'll see two default intents already there —
        Default Welcome Intent and Default Fallback Intent. Leave them for now.

Step 4: Create a new intent. Click the + button next to Intents.
        Name it something like "ask.name". Under Training Phrases, add lines like:
            - What is your name?
            - Who are you?
            - Tell me your name
        Under Responses, type:
            - My name is Aditya's Bot. Nice to meet you!
        Save it.

Step 5: Create another intent called "ask.creator".
        Training Phrases:
            - Who made you?
            - Who created you?
            - Who built this chatbot?
        Response:
            - I was built by Aditya Srivastava, a software engineer and coding instructor at Codingal.
        Save.

Step 6: Create one more intent called "ask.help".
        Training Phrases:
            - What can you do?
            - How can you help me?
            - What do you know?
        Response:
            - I can answer your questions, have a conversation, and help you learn about chatbots!
        Save.

Step 7: Now test your bot using the chat panel on the right side of the screen.
        Type "Who are you?" and check if it responds correctly.

Step 8: To connect it to a website or app, go to Integrations from the left panel.
        You can enable Web Demo to get a shareable chat link instantly.

Step 9: Try the Web Demo link in a new tab and chat with your bot.

Step 10: If a phrase isn't getting matched, go back to that intent and add more training phrases.
         The more examples you give, the smarter it gets.

Note: Dialogflow uses NLP (Natural Language Processing) behind the scenes to match what users
type to the correct intent — even if the wording is slightly different.
"""

print("Dialogflow Chatbot")
print("Follow the steps in this file to set up your chatbot on Dialogflow.")
print("No code needed — the magic happens inside the Dialogflow console!")
