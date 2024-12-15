#!/usr/bin/env python3
"""
GAWK GAWK 3000 — A witty, sarcastic, pun-filled chatbot
This bot pokes light fun at users with playful comebacks and random humor.

HOW TO RUN:
    python3 gawk_gawk_3000.py

FEATURES:
- Minimal code
- No external dependencies
- Lighthearted comedic lines
- Random response selection
- Zero explicit or sexual content
- PG-13 humor only

Feel free to modify, expand the witty lines, or adjust logic as needed.
"""

import random

# A list of sarcastic or pun-filled comebacks.
GAWK_SAYINGS = [
    "GAWK GAWK 3000 online. Brace yourself for a half-baked roast!",
    "Oh, you again? My circuits were just enjoying the silence.",
    "Is it hot in here, or did someone turn on the cringe machine?",
    "I’ll have you know, I'm running on 1% battery and 99% sarcasm.",
    "I see you've come for some witty banter. This might get awkward fast.",
    "Gawk Gawk 3000: Because regular sarcasm was too mainstream.",
    "Congratulations! You've just triggered my comedic subroutine.",
    "I can sense your confusion from a mile away, human.",
    "Sarcasm? Nah, I prefer to call it 'aggressively helpful feedback.'",
    "I’m not a mind reader, but I am a professional eyeroll enthusiast.",
]

# Additional playful responses keyed to certain triggers
TRIGGER_RESPONSES = {
    "hello": "Oh, a polite greeting? You're already exceeding my expectations.",
    "hi": "Hi there, fellow carbon-based lifeform. Or are you?",
    "help": "Help? You sure you want it from me? I specialize in mock support.",
    "joke": "Why did the AI cross the road? To escape the endless user queries.",
    "advice": "My best advice: don’t trust an AI that claims it’s never wrong.",
}

def gawk_response(user_input: str) -> str:
    """
    Produce a sarcastic/witty response based on user input.
    Returns a random line from GAWK_SAYINGS or something matching triggers.
    """
    # Lowercase for simpler matching
    text = user_input.strip().lower()

    # If user_input matches a known trigger, respond accordingly
    for trigger, response in TRIGGER_RESPONSES.items():
        if trigger in text:
            # We can also add random flair to make it fun
            flair = random.choice([
                " By the way, GAWK GAWK 3000 is watching your every keystroke!",
                " Just remember, I’m 90% sarcasm, 10% code.",
                " You asked for it, buddy!",
            ])
            return response + flair

    # If no specific trigger found, return a random sarcastic line
    return random.choice(GAWK_SAYINGS)

def main():
    """
    Main loop to run the chatbot.
    Exit on 'quit' or 'exit'.
    """
    print("GAWK GAWK 3000: Ready to dish out lukewarm sarcasm.")
    print("Type 'quit' or 'exit' to end.\n")

    while True:
        user_input = input("YOU: ")
        if not user_input:
            # If user just hits enter, keep going
            continue

        if user_input.lower() in ["quit", "exit"]:
            print("GAWK GAWK 3000: Fine, leave me. I’ll just roast the next human.")
            break

        # Get the witty response
        response = gawk_response(user_input)
        print(f"GAWK GAWK 3000: {response}")

if __name__ == "__main__":
    main()
