# iMedia HR Bot - Deployment Guide

## ✅ Status: Code Ready

The bot is built and tested. Now we deploy it to the cloud so it runs 24/7.

---

## Step 1: Choose Hosting (Pick One)

### Option A: Railway (Recommended - Easiest)
1. Go to railway.app
2. Sign up with GitHub
3. Create new project → Deploy from GitHub
4. I'll help with the rest

### Option B: Render
1. Go to render.com
2. Sign up
3. Create new service
4. (Similar process)

---

## Step 2: Prepare Files for Deployment

All files are ready in `/Users/stingerpayne2/.openclaw/workspace/`:
- `hr_bot.py` — Main bot code
- `handbook.txt` — HR handbook
- `bot_keys.txt` — API keys (will move to environment variables)
- `requirements.txt` — Python dependencies

---

## Step 3: Set Environment Variables

When deploying, don't upload `bot_keys.txt`. Instead, set environment variables:

```
TELEGRAM_BOT_TOKEN=your_token_here
CLAUDE_API_KEY=your_api_key_here
```

---

## Step 4: Deploy

**Once you decide on hosting platform, I'll:**
1. Update code for cloud deployment
2. Guide you through the hosting setup
3. Deploy the bot
4. Test it live

---

## What Happens After Deploy

1. Bot runs on Railway/Render servers (not your Mac)
2. Staff find the bot on Telegram: `@YourBotName`
3. They ask HR questions
4. Bot answers using the handbook

---

## Cost Estimate

- **Railway/Render:** $0/month (free tier)
- **Claude API:** ~$2-5/month (depending on usage)
- **Telegram:** Free
- **Total:** ~$2-5/month

---

## Next Action

**Decide:** Railway or Render?

Let me know, and I'll finish the deployment.
