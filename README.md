# AI Tooling Setup & Research Project

This repo has two parts:

1. **[Research project](#research-project-ai-powered-seo-content-production)** — a
   curated, source-backed knowledge base on *AI-powered SEO content production for
   B2B SaaS*, built from 10 genuine practitioners.
2. **[Tooling setup log](#environment)** — how the AI dev environment was set up
   (tools, steps, and issues solved).

---

# Research project: AI-powered SEO content production

**Topic:** AI-powered SEO content production for B2B SaaS.

### Why this topic
Of the eight options, this is the one that's useful *beyond* any single job: AI content
production is the most transferable, future-proof marketing skill, and the underlying
playbook (programmatic SEO, AI content workflows, topical authority, AEO/GEO) applies
to any industry — not just SaaS. It also has the deepest bench of practitioners who post
on collectable channels (YouTube + LinkedIn), which made for a substantial collection.

### Why these 10 experts
I selected on four hard filters — they **operate** (run an agency/tool/in-house growth
or rank their own sites), they **show their work** (case studies with numbers, controlled
experiments, original data), they're **recent + active**, and they're **not grifters**.
I deliberately avoided "Top 10 SEO experts" listicles (SEO-gamed and circular) and
sourced names from where practitioners actually argue and get cited. Full reasoning and
per-person evidence: **[`research/sources.md`](research/sources.md)**.

The 10: **Jake Ward** (Byword, AI content at scale) · **Nick Jordan** (content-first
scaling) · **Kevin Indig** (ex-Shopify/G2/Atlassian, data) · **Bernard Huang**
(Clearscope, AEO/GEO) · **Koray Gübür** (semantic SEO / topical authority) ·
**Eli Schwartz** (product-led SEO) · **Brendan Hufford** (SaaS SEO/AEO) ·
**Cyrus Shepard** (SEO experiments) · **Aleyda Solís** (international + AI search) ·
**Gael Breton** (content sites + AI workflows).

### What was collected
- **8 YouTube transcripts** (~388k characters) across 5 experts — Nick Jordan, Koray
  Gübür (×2), Aleyda Solís, Bernard Huang (×2), Gael Breton (×2) — in
  [`research/youtube-transcripts/`](research/youtube-transcripts/).
- **Annotated index of written work** (newsletters, blog case studies, data studies) for
  all 10 — [`research/other/newsletters-and-articles.md`](research/other/newsletters-and-articles.md).
- **A "practitioner vs. packaging" contrast case** (Julian Goldie) documenting how I
  separated signal from sales — [`research/other/practitioner-vs-packaging.md`](research/other/practitioner-vs-packaging.md).
- **6 LinkedIn posts** across 3 experts (Jake Ward ×2, Kevin Indig ×2, Brendan
  Hufford ×2) — collected manually (no free LinkedIn API; scraping violates ToS), each
  with verbatim text, permalink, exact date (decoded from the post's activity ID), and a
  "why this matters" annotation — in [`research/linkedin-posts/`](research/linkedin-posts/).
  Includes a captured **practitioner disagreement** on AEO (Jake Ward vs. Brendan Hufford).

### How the transcripts were collected (the "API/technical" part)
YouTube transcripts were pulled programmatically with the free
[`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/) Python
package (no API key required) via [`scripts/fetch_transcripts.py`](scripts/fetch_transcripts.py).
To reproduce:
```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/fetch_transcripts.py
```

### Repository structure
```
research/
  sources.md                  # the 10 experts: links, dates, why-chosen evidence
  youtube-transcripts/        # transcripts organized by author / video id
  linkedin-posts/             # posts organized by author (manually collected)
  other/                      # annotated written-content index + contrast case
scripts/
  fetch_transcripts.py        # YouTube transcript collector
  requirements.txt
```

---

## Environment

- **OS:** macOS (Apple Silicon)
- **Shell:** zsh

## Tools installed

| Tool | Version | Purpose |
|------|---------|---------|
| [Cursor IDE](https://cursor.com/) | — | AI-native code editor |
| Claude Code (Cursor add-on) | — | Anthropic's AI coding assistant inside Cursor |
| Codex (Cursor add-on) | — | OpenAI's AI coding assistant inside Cursor |
| [Git](https://git-scm.com/) | 2.53.0 | Version control |
| [GitHub CLI (`gh`)](https://cli.github.com/) | 2.95.0 | Create and manage the repo from the terminal |
| [Homebrew](https://brew.sh/) | 5.1.6 | Package manager (used to install `gh`) |
| [Node.js](https://nodejs.org/) | v22.15.0 | JavaScript runtime (already present) |

## Steps completed

1. **Installed Cursor IDE** and confirmed it launches.
2. **Added the Claude Code add-on** in Cursor (Extensions → searched "Claude Code" →
   Install) and signed in to my Anthropic account.
3. **Added the Codex add-on** in Cursor (Extensions → searched "Codex" → Install) and
   signed in to my OpenAI account.
4. **Installed the GitHub CLI** with Homebrew so I could create and push the repository
   from the terminal:
   ```bash
   brew install gh
   ```
5. **Authenticated with GitHub** using the device-code (web browser) flow:
   ```bash
   gh auth login   # GitHub.com → HTTPS → Login with a web browser
   ```
6. **Created this public repository** and pushed an initial commit (see commands below).
7. **Wrote this README.md** documenting the process.

## Issues I ran into and how I solved them

### 1. GitHub device login failed: "Uh oh, we couldn't find anything"

When I ran `gh auth login` and entered the one-time code at
`https://github.com/login/device`, GitHub responded with **"Uh oh, we couldn't find
anything — Please make sure you entered the user code correctly."**

**Cause:** The device code is only valid for a short window, and it's only valid while
the `gh auth login` process that generated it is still running. My first code had gone
stale.

**Fix:** I re-ran `gh auth login` to generate a **fresh** code, reloaded the device page
in the browser so it wasn't re-submitting the old one, and entered the new code promptly
while leaving the terminal process running. GitHub then showed **"Congratulations,
you're all set!"** and the terminal confirmed the login.

I verified it with:
```bash
gh auth status
```

### 2. `gh` was not installed by default

The GitHub CLI wasn't on the machine, so the terminal returned `command not found: gh`.
I already had Homebrew, so installing it was a one-liner (`brew install gh`).

## How this repo was created

```bash
mkdir ai-tooling-setup && cd ai-tooling-setup
git init
git branch -M main
# ...wrote README.md...
git add README.md
git commit -m "Add README documenting AI tooling setup"
gh repo create ai-tooling-setup --public --source=. --remote=origin --push
```
