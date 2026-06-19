# LinkedIn posts

LinkedIn has no free public API for pulling a person's posts, and scraping it violates
their ToS — so these are **manually collected** (the brief explicitly allows this:
"scrape or manually collect"). Each author has a folder; each post is one Markdown file
using `_TEMPLATE.md`.

## How posts were collected
1. Open the author's LinkedIn "Activity → Posts" feed.
2. Copy 3–5 of their strongest *recent* posts on AI / SEO / content production.
3. Save each as `NN-short-slug.md` in the author's folder, filling in the template
   (URL, date, the post text, and a one-line "why this matters" annotation).

## Collected (6 posts, 3 authors)
LinkedIn collection focused on the experts whose primary, most current content lives on
LinkedIn:
- **Jake Ward** (2) — AEO "best X" citation data; SEO-vs-AEO/GEO/AIO hype-cutting
- **Kevin Indig** (2) — prompt-tracking panel design; AIO back-scroll behavior + meta copy
- **Brendan Hufford** (2) — AI content quality + a Claude/MCP workflow; AEO skepticism of
  Google's guidance (a deliberate counterpoint to Jake Ward's view)

The other experts are represented through captured **YouTube transcripts**
(Nick Jordan, Bernard Huang, Koray Gübür, Aleyda Solís, Gael Breton — see
`../youtube-transcripts/`) and the **annotated written-content index** (Eli Schwartz,
Cyrus Shepard, and all others — see `../other/newsletters-and-articles.md`), so every
one of the 10 has captured primary or annotated material.

## File naming
`research/linkedin-posts/<author-slug>/NN-topic-slug.md`
e.g. `jake-ward/01-worlds-largest-ai-seo-case-study.md`
