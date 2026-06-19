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

## Priority authors for LinkedIn (most active there)
- **Jake Ward** — AI content case studies (highest priority; LinkedIn is his main stage)
- **Kevin Indig** — data threads
- **Brendan Hufford** — SaaS content/AEO takes
- **Eli Schwartz** — product-led SEO commentary
- **Cyrus Shepard** — experiment results
- **Nick Jordan** — content-scaling notes

## File naming
`research/linkedin-posts/<author-slug>/NN-topic-slug.md`
e.g. `jake-ward/01-worlds-largest-ai-seo-case-study.md`
