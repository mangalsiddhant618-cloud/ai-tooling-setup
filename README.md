# AI Tooling Setup

A short, honest log of setting up an AI-assisted development environment: the tools I
installed, the steps I followed, and the problems I ran into along the way (and how I
got past them).

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
