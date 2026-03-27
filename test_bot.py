#!/usr/bin/env python3
"""Quick test of bot logic without Telegram"""

import sys
from pathlib import Path
from anthropic import Anthropic

# Load keys
def load_keys():
    keys = {}
    with open('/Users/stingerpayne2/.openclaw/workspace/bot_keys.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                keys[key] = value
    return keys

KEYS = load_keys()
CLAUDE_API_KEY = KEYS['CLAUDE_API_KEY']

# Load handbook
def load_handbook():
    with open('/Users/stingerpayne2/.openclaw/workspace/handbook.txt', 'r') as f:
        return f.read()

HANDBOOK = load_handbook()

SYSTEM_PROMPT = f"""You are an HR assistant for iMedia. Answer questions based on this handbook only:

<handbook>
{HANDBOOK}
</handbook>

Rules:
1. Answer ONLY from the handbook
2. If not in handbook, say: "I don't see this in the handbook. Contact HR."
3. Be concise (2-3 sentences)
4. Cite relevant sections"""

# Initialize client
client = Anthropic(api_key=CLAUDE_API_KEY)

# Test questions
test_questions = [
    "How many days of annual leave do I get?",
    "What's the maternity leave policy?",
    "How much is parking reimbursement?",
    "What happens if I'm absent without leave?"
]

print("🧪 Testing HR Bot...\n")

for question in test_questions:
    print(f"Q: {question}")
    
    response = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": question}]
    )
    
    answer = response.content[0].text
    print(f"A: {answer}\n")
    print("-" * 60 + "\n")

print("✅ Bot logic test complete!")
