# Deploy to Railway

## Step 1: Set Up GitHub (5 minutes)

1. Go to github.com
2. Sign up (or log in)
3. Create new repository called `imedia-hr-bot`
4. **DO NOT** add any files yet

---

## Step 2: Push Code to GitHub

Run these commands in Terminal:

```bash
cd /Users/stingerpayne2/.openclaw/workspace

# Initialize git (if not already done)
git init

# Add all files (except bot_keys.txt - it's in .gitignore)
git add .

# Commit
git commit -m "Initial HR bot commit"

# Add GitHub remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/imedia-hr-bot.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 3: Set Up Railway (10 minutes)

1. Go to **railway.app**
2. Sign up with GitHub (authorize)
3. Click "New Project"
4. Select "Deploy from GitHub"
5. Find and select `imedia-hr-bot` repo
6. Click "Deploy"

Railway will automatically detect it's a Python project and deploy it.

---

## Step 4: Set Environment Variables (5 minutes)

In Railway dashboard:

1. Go to your project
2. Click the service (should say "imedia-hr-bot")
3. Go to "Variables" tab
4. Add two variables:

   ```
   TELEGRAM_BOT_TOKEN = [paste your token]
   CLAUDE_API_KEY = [paste your API key]
   ```

5. Click "Deploy" button

---

## Step 5: Verify Deployment (5 minutes)

1. In Railway, go to "Deployments" tab
2. Wait for status to show "✓ Success"
3. Open Telegram
4. Search for your bot (e.g., `@iMediaHRBot`)
5. Send a test message: "How many days of annual leave?"
6. Bot should respond within 5 seconds

---

## That's It!

Bot is now live 24/7. Staff can message it anytime.

---

## Troubleshooting

**Bot doesn't respond?**
- Check Railway "Logs" tab for errors
- Verify environment variables are set correctly
- Verify API key is still valid

**Bot crashes?**
- Check logs in Railway dashboard
- Usually means API key is wrong or API is down

---

## Cost

- **Railway:** Free (free tier covers this use case)
- **Claude API:** ~$2-5/month based on usage

Total: ~$2-5/month
