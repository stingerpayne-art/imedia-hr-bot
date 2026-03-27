#!/usr/bin/env python3
"""
iMedia HR Bot - Telegram bot for answering HR questions
Uses Claude API to answer questions based on HR handbook
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from anthropic import Anthropic

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load API keys from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

# Fallback to file if env vars not set (for local testing)
if not TELEGRAM_TOKEN or not CLAUDE_API_KEY:
    try:
        with open('bot_keys.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    if key == 'TELEGRAM_BOT_TOKEN':
                        TELEGRAM_TOKEN = value
                    elif key == 'CLAUDE_API_KEY':
                        CLAUDE_API_KEY = value
    except FileNotFoundError:
        pass

if not TELEGRAM_TOKEN or not CLAUDE_API_KEY:
    raise ValueError("TELEGRAM_BOT_TOKEN and CLAUDE_API_KEY environment variables must be set")

# Initialize Anthropic client
client = Anthropic(api_key=CLAUDE_API_KEY)

# Load handbook
def load_handbook():
    with open('/Users/stingerpayne2/.openclaw/workspace/handbook.txt', 'r') as f:
        return f.read()

HANDBOOK = load_handbook()

# System prompt for Claude
SYSTEM_PROMPT = f"""You are an HR assistant for iMedia, a digital media company. 
Your job is to answer employee questions about HR policies based on the company handbook.

Here is the iMedia HR Handbook:

<handbook>
{HANDBOOK}
</handbook>

Rules:
1. Answer questions ONLY based on the handbook above
2. If the question is not covered in the handbook, say: "I don't see this covered in the handbook. Please contact HR directly at [hr contact info]"
3. Be helpful, clear, and professional
4. If uncertain, acknowledge the uncertainty and suggest contacting HR
5. For medical/legal questions, always recommend consulting HR or a professional
6. Keep answers concise (2-3 sentences when possible)

When answering:
- Cite the relevant section from the handbook if applicable
- Be specific (use actual numbers, dates, amounts from the handbook)
- If there are exceptions or conditions, mention them
"""

class HRBot:
    def __init__(self):
        self.conversation_history = {}
    
    def get_answer(self, user_id: int, question: str) -> str:
        """Get answer from Claude based on handbook and question"""
        try:
            # Initialize conversation history for this user if needed
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = []
            
            # Add user message to history
            self.conversation_history[user_id].append({
                "role": "user",
                "content": question
            })
            
            # Get response from Claude
            response = client.messages.create(
                model="claude-opus-4-1-20250805",
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                messages=self.conversation_history[user_id]
            )
            
            assistant_message = response.content[0].text
            
            # Add assistant response to history
            self.conversation_history[user_id].append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except Exception as e:
            logger.error(f"Error getting answer: {e}")
            return "Sorry, I encountered an error. Please try again or contact HR directly."

# Initialize bot
hr_bot = HRBot()

# Telegram handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "👋 Welcome to iMedia HR Assistant!\n\n"
        "I'm here to help you with HR questions about:\n"
        "• Leave policies (annual, medical, maternity, etc.)\n"
        "• Salary and benefits\n"
        "• Claims and reimbursements\n"
        "• Work policies and conduct\n"
        "• And more!\n\n"
        "Just ask me your question and I'll help. 📖"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        "📚 How to use this bot:\n\n"
        "1. Ask any HR question in plain English\n"
        "2. I'll search the HR handbook for the answer\n"
        "3. If I'm unsure, I'll ask you to contact HR\n\n"
        "Examples:\n"
        "• 'How many days of annual leave do I get?'\n"
        "• 'What's the maternity leave policy?'\n"
        "• 'How much is parking reimbursement?'\n\n"
        "For urgent issues, always contact HR directly."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    question = update.message.text
    
    # Log query
    logger.info(f"User {user_name} ({user_id}): {question}")
    
    # Show typing indicator
    await update.message.chat.send_action("typing")
    
    # Get answer
    answer = hr_bot.get_answer(user_id, question)
    
    # Send answer
    await update.message.reply_text(answer)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.message:
        await update.message.reply_text(
            "Sorry, something went wrong. Please try again or contact HR."
        )

def main():
    """Start the bot"""
    logger.info("Starting iMedia HR Bot...")
    
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot is running. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
