"""Generate a PDF in L:\nothing\nothing 1 recommending ~29 time-saving automations.

Based on the user's profile (AI engineer, likes coding + automation, AI-first).
Run: python L:\nothing\nothing 1\generate_automations_pdf.py
"""
import textwrap
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

OUT = Path(r"L:\nothing\nothing 1\automations_recommendations.pdf")

AUTOMATIONS = [
    ("Auto CI + Lint on every push (GitHub Actions)",
     "Runs tests and linters automatically on each push; fails the PR if something breaks.",
     "GitHub Actions (free minutes), ESLint/Ruff"),
    ("Auto Vercel deploy on push to main",
     "Every push to main triggers a production deploy of the linked app automatically.",
     "Vercel GitHub Integration (free tier)"),
    ("Daily GitHub issue/PR digest bot",
     "Every morning, sends you a summary of open issues, PRs waiting on you, and CI status.",
     "GitHub Actions + webhook to Slack/Telegram, free tier"),
    ("AI-powered issue triage (auto-label + auto-triage)",
     "New issues are automatically labeled (bug/feature/question) using AI based on title/body.",
     "GitHub Actions or OpenCode on CI, free tier"),
    ("AI PR review on open PRs",
     "Automatically requests/gets AI review of new PRs; posts review comments on GitHub.",
     "Codex/Copilot AI review (free tiers), GitHub API"),
    ("Changelog builder from commit history",
     "Turns recent commits into a clean changelog entry (categorized by type) with AI summaries.",
     "Python script + AI on a GitHub Action, free"),
    ("Auto README/API docs sync",
     "Docs are generated from code comments/schema and deployed to GitHub Pages / Vercel.",
     "Typedoc/mkdocs + GitHub Pages, free tier"),
    ("Dead-code & code-smell detector (scheduled)",
     "Weekly run of ESLint/Ruff + heuristics; posts unused-code or quality findings to Slack.",
     "GitHub Actions, free"),
    ("Auto coverage drop alert",
     "Monitors test coverage; if it drops below a threshold, alerts you in chat with details.",
     "Python + GitHub Actions/webhook alerts, free"),
    ("AI daily journal: summarize yesterday's commits",
     "At end of day, AI summarizes your day's commits/PRs into a short daily note file.",
     "OpenCode/AI + script run on cron, free tier"),
    ("GitHub <-> Notion sync for tasks",
     "New GitHub issues/PRs are mirrored into a Notion workspace as tasks you manage centrally.",
     "GitHub webhook + Apps Script/n8n, free tiers"),
    ("Vercel runtime error alerts -> Slack",
     "Watches Vercel production logs and sends you a chat alert with error details.",
     "Vercel Insights + webhook (free tier)"),
    ("Production uptime checker",
     "Checks your deployed sites every 5 min; pings you on failure (cron + curl + notify).",
     "Free cron + tiny script; any domain, free"),
    ("Auto website preview links for PRs",
     "Comments a preview deploy URL on every PR via GitHub webhook (vercel, free tier).",
     "Vercel + GitHub API, free tier"),
    ("Automated test generator from specs",
     "From a markdown spec of a feature, AI generates unit tests and places them in the repo.",
     "AI + pytest/jest + GitHub Actions, free tiers"),
    ("API change detector",
     "Monitors external free APIs for changes (new endpoints, breaking changes) and notifies you.",
     "Cron + AI summary + notify, free"),
    ("Bulk video render pipeline (n8n)",
     "Automate: ingest clips -> trim/caption -> export with ffmpeg -> upload. Uses n8n (local or free tier).",
     "n8n Cloud free tier or local n8n, free"),
    ("Scheduled weekly research digest",
     "Each week: AI searches the web for topics you care about (AI, automation, Vercel) and emails you a digest.",
     "Free search API (Tavily/Exa) + email script, free tiers"),
    ("TODO triager",
     "Auto-tags open TODOs by urgency/impact using AI on your task files.",
     "OpenCode/AI script on TODO files, free"),
    ("RSS digest -> Telegram bot",
     "Pulls RSS feeds; every day sends you a summary digest in chat.",
     "RSS feed + AI summary + Telegram bot, free tiers"),
    ("Auto issue auto-merge bot",
     "Auto-merges PRs that pass CI + have approved reviews + requested-review label set to 'ready'.",
     "GitHub API script, free"),
    ("Auto domain SSL monitoring + renewal alerts",
     "Weekly check that HTTPS still works on all your sites; alerts when certs expire.",
     "Cron + tiny script, free"),
    ("Wiki auto-sync from PRs",
     "Merges PRs with a 'docs:' label into a central docs repo automatically.",
     "GitHub Actions, free"),
    ("Private n8n workflow module library",
     "Export common automations as n8n modules you reuse across projects (matches your n8n dirs).",
     "n8n, free tier/local"),
    ("Auto backup to GitHub/cloud",
     "Daily scripts that push your key projects or data files to a private repo; emails on failure.",
     "GitHub Actions or cron + git push, free"),
    ("AI meeting notes -> tasks",
     "Turns your voice/text notes into structured tickets on GitHub issues.",
     "AI + GitHub API, free tiers"),
    ("Emoji/label auto-tagging on PRs",
     "Comments on new PRs with an emoji tag of the change type (feat/fix/doc) + AI summary.",
     "GitHub Actions + AI, free tiers"),
    ("Automated video thumbnail generator",
     "From a video file, generate a clean title card thumbnail with ffmpeg + AI text.",
     "ffmpeg + AI (free tiers), local"),
    ("AI-generated weekly progress report",
     "Every Friday: AI pulls your week's commits/PRs/issues and writes a 1-page summary to Notion.",
     "AI + GitHub API + Notion webhook, free tiers"),
    ("Mining missed automations from your folder",
     "Each month: scan your own scripts/projects (C:\\Users\\karth, L:\\nothing\\1) for repeated tasks you still do manually, and suggest the matching OpenCode skill + automation idea.",
     "Script + AI, free tiers"),
]

X = 72
W = 430  # text width in points


def ncols(font_name, size):
    return max(1, int(W // max(pdfmetrics.stringWidth(" ", font_name, size, None), 1)))


def draw_block(c, x, y, text, font_name, size, leading):
    c.setFont(font_name, size)
    if text:
        for line in textwrap.wrap(text, ncols(font_name, size)) or [""]:
            c.drawString(x, y, line)
            y -= leading
    return y


def draw_item(c, i, title, task, tools, y):
    y = draw_block(c, X, y, f"{i}. {title}", "Helvetica-Bold", 10, 12)
    y = draw_block(c, X + 8, y, task, "Helvetica", 9, 11)
    y = draw_block(c, X + 8, y, f"Tools: {tools}", "Helvetica-Oblique", 7, 9)
    return y - 6


def main():
    c = canvas.Canvas(str(OUT), pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, h - 60, "Automations you might have missed")

    c.setFont("Helvetica", 9)
    c.drawString(X, h - 80, "Time-saving automations for an AI-first coder. Mostly free of cost.")
    c.drawString(X, h - 92, "Recommended via your OpenCode skills knowledge. First pick: #2 and #3.")

    y = h - 110
    for i, (title, task, tools) in enumerate(AUTOMATIONS, 1):
        y = draw_item(c, i, title, task, tools, y)
        if y < 80:
            c.showPage()
            y = h - 110

    c.setFont("Helvetica-Oblique", 8)
    c.drawString(X, 40, "Generated by you + OpenCode. See skills/ in your workspace for AI skills that do similar work.")
    c.showPage()
    c.save()
    print(f"PDF written: {OUT}")


if __name__ == "__main__":
    main()
