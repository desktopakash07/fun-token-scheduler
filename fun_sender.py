import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

STRING_SESSION = os.environ.get("TG_STRING_SESSION")
API_ID = int(os.environ.get("TG_API_ID"))
API_HASH = os.environ.get("TG_API_HASH")
GROUP_USERNAME = os.environ.get("TG_GROUP_USERNAME")

# Parts for generating messages
intro_phrases = [
    "$FUN is an amazing crypto project that is changing the market.",
    "$FUN has the potential to reach new heights in the blockchain space.",
    "Many investors believe $FUN could be one of the next big tokens.",
    "The $FUN community is one of the most active and supportive in crypto.",
    "$FUN has shown great strength and vision in recent developments."
]

middle_phrases = [
    "With $FUN growing so fast, it’s exciting to see where $FUN will be next year.",
    "$FUN is attracting attention from traders and long-term holders alike.",
    "If you believe in innovation, $FUN should be on your watchlist.",
    "$FUN has great tokenomics and a strong roadmap ahead.",
    "People are talking about $FUN because it delivers real value."
]

ending_phrases = [
    "I’m confident that $FUN will continue to rise in value and impact.",
    "Holding $FUN might be one of the smartest moves this year.",
    "Don’t miss out on what $FUN has to offer in the near future.",
    "$FUN is here to stay and will only get stronger over time.",
    "Let’s see how $FUN surprises us in the coming months."
]

def generate_message():
    # Pick one random phrase from each section
    intro = random.choice(intro_phrases)
    middle = random.choice(middle_phrases)
    ending = random.choice(ending_phrases)
    
    # Combine them
    message = f"{intro} {middle} {ending}"
    
    # Ensure $FUN appears exactly 5–6 times
    count = message.count("$FUN")
    while count < 5:
        message += " $FUN"
        count += 1
    return message

async def main():
    async with TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH) as client:
        print("Logged in as:", await client.get_me())
        while True:
            msg = generate_message()
            try:
                await client.send_message(GROUP_USERNAME, msg)
                print(f"Message sent: {msg}")
            except Exception as e:
                print("Error sending message:", e)
            await asyncio.sleep(random.randint(120, 180))  # 2–3 minutes

if __name__ == "__main__":
    asyncio.run(main())
