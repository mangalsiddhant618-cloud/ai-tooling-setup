# Fact-check: auditing the experts' claims

Collecting sources isn't the same as trusting them. The experts in this repo are
practitioners, but practitioners make bold, round-number claims — so before any of this
feeds a real playbook, the headline claims get independently verified. Each is rated:

- ✅ **Verified** — confirmed against an independent primary/credible source
- 🟡 **Partially true / overstated / needs nuance** — the direction is right but the
  specific claim is shaky, conflated, or context-dependent
- ⚪ **Unverified / self-reported** — couldn't independently confirm; treat with care

> Method: cross-checked each claim via independent web sources (studies, the DOJ
> antitrust record, vendor research), not against the experts' own restatements.

---

## ✅ Verified

**"AI crawlers (ChatGPT/Claude/Perplexity) don't render JavaScript."** — *Aleyda Solís*
A Vercel + Merj study of 500M+ GPTBot requests found **zero evidence** GPTBot executes
JS, even when it downloads JS files; ClaudeBot and PerplexityBot behave the same (they
fetch some JS — ~11–24% of requests — but don't run it). Googlebot/Gemini is the
exception (uses Google's render infra). **Verdict: solid, and one of the highest-leverage
technical facts in the whole repo.**
Sources: [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler) · [GSQi case study](https://www.gsqi.com/marketing-blog/ai-search-javascript-rendering/)

**"The average B2B buying journey is ~272 days."** — *Brendan Hufford (via Dreamdata)*
Dreamdata's 2026 report (3.5M+ journeys, 66M+ sessions) puts it at exactly **272 days**,
up from 211 the prior year, with 88 touchpoints and 10 stakeholders. **Verdict: accurate,
correctly attributed.**
Source: [PPC Land](https://ppc.land/linkedin-ads-hit-121-roas-as-b2b-buyer-journeys-stretch-to-272-days/)

**"Google publicly downplayed signals (Chrome data, link building) that its systems
actually reward."** — *Brendan Hufford*
The DOJ antitrust trial + 2024 API leak confirm **Navboost** uses click data (incl. from
Chrome) as "one of the important signals" (Pandu Nayak's testimony), and that click/
anchor signals matter — despite years of public hedging. **Verdict: well-supported; his
skepticism is earned, not contrarian for its own sake.**
Source: [Hobo: Google vs DOJ](https://www.hobo-web.co.uk/google-vs-doj/)

**"llms.txt has 0 measurable impact."** — *Jake Ward*
Google's John Mueller confirmed (2025) **no Google Search system reads or acts on
llms.txt**; it's not a factor in rankings, AI Overviews, or AI Mode. He likened it to the
long-dead keywords meta tag. **Verdict: confirmed — don't spend production time on it.**
Source: [SEOVendor](https://seovendor.co/google-confirms-llms-txt-doesnt-help-rankings-what-seo-agencies-should-do-instead/)

---

## 🟡 Partially true / needs nuance

**"Search is up 26% since ChatGPT launched."** — *Jake Ward*
True **but the framing matters**: it's *total discovery* (search engines **+** LLMs)
that grew ~26% globally (Q1'23→Q4'25), not Google search in isolation. Google alone also
grew (~21% '23→'24), so his point ("AI expanded search, didn't kill it") holds — just
don't quote "26%" as if it's Google-only.
Source: [Graphite](https://graphite.io/five-percent/ai-is-much-bigger-than-you-think)

**"43.8% of AI citations come from 'best X' lists."** — *Jake Ward*
**Directionally well-supported, exact number unverified.** Semrush's "Ghost Citations"
study found comparative/"best" queries drive a ~43.3% mention rate and ~2.4× more brand
mentions than informational content — close to Jake's figure, but it measures *mention
rate for comparative queries*, not "share of all citations." The takeaway (listicles/
comparison pages punch far above their weight in AI citations) is real; the precise stat
may be conflated across studies. **Use the strategy, cite the number cautiously.**
Source: [Semrush Ghost Citations](https://www.semrush.com/blog/the-ghost-citations-study/)

**"Schema isn't parsed [so don't bother]."** — *Jake Ward*
**Overstated.** Google says structured data **isn't required** for generative-AI search
and there's no special AI schema — *but* it still recommends schema for rich-results
eligibility in classic search. So "skip schema for AEO" ≈ fair; "schema is useless" ≈ too
strong. Keep schema for traditional SERP features.
Source: [Google AI search guidance](https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit)

---

## ⚪ Unverified / self-reported (treat as case studies, not proof)

**"0 → 200k–333k organic visits in ~5 months" (Koray) · "1M traffic from 7,000 AI pages"
(Jake Ward) · "scaled brands to 100k+/mo" (Nick Jordan).**
These are **self-reported case studies** with no independent audit available. They're
plausible and come from people who clearly operate — but a single unaudited case study is
an existence proof, not a benchmark. **Don't promise these numbers to a stakeholder;
treat them as "this is possible," not "this is expected."**

**"~80% of AI-cited list pages are recently updated." — *Jake Ward***
Couldn't locate the underlying dataset. Freshness mattering is consistent with other
findings, but the specific 80% is **unverified**.

**"47.5% of scrolling on AIO SERPs goes backward." — *Kevin Indig***
Attributed in-post to **Clickstream Solutions + Surfer SEO** (a named primary source),
which is good practice — but I didn't independently re-run it. Trust level: medium-high
given the named source; flagged for transparency.

---

## What this audit changes in the playbook

1. **Promote** the JS-rendering, llms.txt, Dreamdata, and antitrust facts to "act on with
   confidence."
2. **Soften** the "26%," "43.8%," and "schema is useless" claims to directional guidance.
3. **Never quote** the self-reported traffic numbers as benchmarks — only as proof a
   ceiling exists.
4. General rule earned here: **round, dramatic stats usually trace back to one vendor
   study measuring something narrower than the claim implies.** Verify before repeating.
