# HR Bot Project - Session 1

**Date:** 2026-03-27
**Status:** Just kicked off
**Owner:** Ken (COO, iMedia)

## What We're Building

Telegram bot for iMedia staff to ask HR questions. Bot reads the HR handbook, answers via Claude API.

## Why This

- 200 staff keep asking HR basic questions (leave, claims, medical, etc.)
- HR team gets overloaded
- Bot can handle 80% of FAQs instantly
- Escalates edge cases to HR

## Files Gathered

- **handbook.txt** (287 lines, clean) — Extracted from HR manual v7.0
- **3 more P&P files coming:** Claims, Training, Crisis (Ken will share when ready)

## Tech Stack Decided

- **Telegram bot** (free, no per-message costs)
- **Claude API** (~$0.01-0.05 per question)
- **Cloud hosting** (Railway/Render, ~$5/month)
- **No database for now** (Option 1: simple, fast)

## Timeline

- Phase 1 (Day 1-2): Bot setup + testing
- Phase 2 (Day 2-3): Handbook integration
- Phase 3 (Day 3-4): Deploy + polish

**Total: 3-4 working days**

## Next Actions

1. Ken creates Claude API key (api.anthropic.com)
2. Ken creates Telegram bot via BotFather
3. I start coding `hr_bot.py`
4. Deploy to cloud

## Notes

- Ken prefers direct, truth-seeking communication
- Budget conscious but willing to invest in right solution
- Plans to add more P&P files later (can expand bot easily)
- Wants fast MVP, not perfect

---

**Source:** Session with Ken via Telegram, 2026-03-27
