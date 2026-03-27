# HR Bot Build Plan

## Project: iMedia HR Assistant Bot
**Status:** In Progress
**Timeline:** 3-4 days
**Cost:** ~$2-5/month (Claude API)

---

## What We're Building

A Telegram bot that answers HR questions from iMedia staff using the HR handbook.

**Features:**
- Staff message bot with HR questions
- Bot searches handbook, answers using Claude
- Escalates to HR for uncertain questions
- Logs all queries for analytics

---

## Tech Stack

- **Platform:** Telegram (free, no API costs)
- **LLM:** Claude API (Anthropic) — costs ~$0.01-0.05 per question
- **Hosting:** Railway or Render (free tier, ~$5/month paid)
- **Language:** Python
- **Libraries:** 
  - `python-telegram-bot` (Telegram integration)
  - `anthropic` (Claude API)

---

## Build Phases

### Phase 1: Core Bot (Day 1-2)
- [ ] Create Telegram bot via BotFather
- [ ] Set up Claude API key
- [ ] Build basic bot structure
- [ ] Test locally

### Phase 2: Handbook Integration (Day 2-3)
- [ ] Load handbook.txt into bot
- [ ] Create Claude prompt for HR questions
- [ ] Test Q&A with sample questions
- [ ] Add escalation logic

### Phase 3: Deployment & Polish (Day 3-4)
- [ ] Deploy to Railway/Render
- [ ] Add logging
- [ ] Create admin dashboard for logs
- [ ] Documentation for staff

---

## Next Steps

1. **Get Telegram bot token** (I'll guide you)
2. **Get Claude API key** (you create via Anthropic)
3. **Start coding**

---

## Files to Track

- `handbook.txt` — Already extracted ✓
- `hr_bot.py` — Main bot code (to create)
- `config.py` — API keys, settings
- `requirements.txt` — Dependencies

---

## What I Need From You

**Before starting:**
1. Create Claude API key (free account at api.anthropic.com, get key)
2. Create Telegram bot (I'll guide you through BotFather)
3. Decide: Deploy to Railway or Render? (I'll help with either)

**Want to proceed?** Give me the green light.
