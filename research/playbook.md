# The AI-Powered SEO Content Production Playbook (B2B SaaS)

A synthesis of the 10 practitioners in this repo — distilled into one operating playbook.
Every claim links back to the captured source (LinkedIn post or YouTube transcript) so you
can trace it. This is the "what would I actually *do*" layer, not a summary.

> **Scope & honesty note:** this is synthesized from the sources collected here, not a
> guarantee of results. Where practitioners disagree, I've kept the disagreement visible
> (see [§7](#7-the-live-debates-dont-paper-over-these)) rather than forcing a false
> consensus.

---

## 0. The five mental-model shifts everything else hangs on

1. **AI expanded SEO; it didn't kill it.** Good SEO ≈ good AI visibility. Search is up
   ~26% since ChatGPT launched.
   — [Jake Ward, LinkedIn](linkedin-posts/jake-ward/02-seo-aeo-geo-aio-2026.md)
2. **Engagement signals, not backlinks, increasingly drive rankings.** Google sees
   time-on-site, pages/session, return visits, branded search (Chrome/Android/Analytics).
   — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)
3. **Mentions/citations now rival links for AI search.** LLMs weight being *mentioned*
   (even unlinked) across Reddit, YouTube, comparison pages.
   — [Aleyda Solís, transcript](youtube-transcripts/aleyda-solis/pqrwpXpMM6s.md);
   [Jake Ward, LinkedIn](linkedin-posts/jake-ward/01-best-x-lists-ai-citations.md)
4. **Use AI to create *better*, not to *care less*.** Lazy AI content signals disrespect
   for the reader's time, and audiences detect it.
   — [Brendan Hufford, LinkedIn](linkedin-posts/brendan-hufford/01-ai-content-quality-respect-debate.md)
5. **Treat every authority's guidance (incl. Google's) as one data point, validated
   against your own tracking.** — [Brendan Hufford, LinkedIn](linkedin-posts/brendan-hufford/02-dont-fully-trust-googles-aeo-guidance.md)

---

## 1. Strategy & topic architecture (before you produce anything)

- **Start from purchase intent, not volume.** Build the prompt/topic set weighted toward
  *problem* queries — that's where buying intent lives. For a CRM category Kevin uses ~40
  seeds: 12 brand / 12 category / 16 problem.
  — [Kevin Indig, LinkedIn](linkedin-posts/kevin-indig/01-prompt-tracking-aeo-b2b-saas.md)
- **Treat SEO as a product problem.** Ask *why* a searcher finds you, what experience they
  get, and whether they enter a real funnel — don't just chase top-of-funnel keywords.
  — [Eli Schwartz, *Product-Led SEO*](other/newsletters-and-articles.md)
- **Scope realistically — hundreds of pages, not a handful.** A single B2B use case needs
  5–10 landing-page variants *plus* hundreds of mid-funnel articles to capture all
  intent. 30–50 pages is trivial; authority starts ~100+ pages.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)
- **Build a topical map, not a keyword list.** Cover the *intersecting zones* between the
  domains you span; the map should show the actual pages to build. Maintain a "core"
  (monetization, all signals) + "periphery" (trend/historical coverage) structure.
  — [Koray Gübür, transcript](youtube-transcripts/koray-gubur/81pe-YM9iRI.md)
- **Pick one central entity / site focus.** Don't spawn a page per brand if one is central;
  on core-update recovery, *reduce* URL count so PageRank per URL rises (merge weak pages
  into strong). — [Koray Gübür, transcript](youtube-transcripts/koray-gubur/p6_0qWCgh3Q.md)

---

## 2. The AI-assisted production workflow (where most people go wrong)

**Golden rule from the operators: AI does the grunt work; humans own ideas + final QA.**

- **Ideas human, polish AI.** Gael's engagement *tanked* when AI wrote posts from scratch;
  generate your own ideas, then use AI for hooks/framing/storytelling (~5 min).
  — [Gael Breton, transcript](youtube-transcripts/gael-breton/blG6gss-mUY.md)
- **Use AI to extract IP you already have.** Brendan's weekly workflow: a Claude skill +
  Fathom MCP pulls his last 7 days of calls, runs Erica Schneider's "MP4" process, and
  resurfaces his own best lines. AI mines genuine expertise rather than inventing generic
  content. — [Brendan Hufford, LinkedIn](linkedin-posts/brendan-hufford/01-ai-content-quality-respect-debate.md)
- **Draft with a strong, example-loaded system prompt + human review gates.** Gael feeds
  rough bullets → bot researches gaps (Perplexity) → full draft → he iterates ~7 feedback
  points → ships. ~2 hrs/week, ~80% faster, review gate is load-bearing.
  — [Gael Breton, transcript](youtube-transcripts/gael-breton/blG6gss-mUY.md)
- **System prompt > model choice.** Pick one stable model, build repetition tests, iterate
  the prompt on failures. (Gael finds Gemini 2.5 Pro stable/cheap; GPT-5 volatile in
  automations.) — [Gael Breton, transcript](youtube-transcripts/gael-breton/c2fgBO0cpcw.md)
- **Start automations simple (<10 steps); automate only the tedious steps you've done
  manually.** Complex automations no one uses are the common failure.
  — [Gael Breton, transcript](youtube-transcripts/gael-breton/c2fgBO0cpcw.md)
- **Make on-page SEO executable by non-SEOs via a template.** Give writers the H1/meta/URL
  keyword + variations for H2s/body; editors swap same-intent variants, keep unique-intent
  phrases as separate sections — no manual density-checking.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)
- **Quality threshold is non-negotiable.** Automated slop damages brand trust; "done beats
  perfect" but a quality gate gates it. Watch your own tells (e.g. em-dash overuse).
  — [Brendan Hufford](linkedin-posts/brendan-hufford/01-ai-content-quality-respect-debate.md) ·
  [Gael Breton](youtube-transcripts/gael-breton/c2fgBO0cpcw.md)

---

## 3. Writing for relevance (the semantic layer that actually ranks)

- **Match answer phrasing to the query's grammar.** Reorder sentences to shift emphasis
  toward the target query ("Financial advisor helps families…" vs "Families achieve… with
  a financial advisor") without changing the substance.
  — [Koray Gübür, transcript](youtube-transcripts/koray-gubur/p6_0qWCgh3Q.md)
- **Use response templates for Boolean/modality questions.** Yes/No or "It depends" openers;
  mirror the query's modal verb ("Can…" → answer with "can").
  — [Koray Gübür, transcript](youtube-transcripts/koray-gubur/81pe-YM9iRI.md)
- **Chain the entities the model expects.** Content wins when it includes the full entity
  set an answer needs (e.g. Ahrefs + Semrush + Moz for "SEO tools"). Extract entities from
  both Google top-20 *and* the model's own answers.
  — [Bernard Huang, transcript](youtube-transcripts/bernard-huang/RMg2eTZL7Jk.md)
- **Relevance density beats domain authority.** Nick outranked Instagram's own support page
  with better-structured, heading-matched content.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)

---

## 4. Optimizing for AI search (AEO/GEO)

- **Run "query fan-out" sampling 10–20× per prompt.** AI output is probabilistic; sample
  repeatedly to map the (often near-zero-volume) "long-long-tail" queries the model
  actually searches, then build pages for those gaps.
  — [Bernard Huang, transcript](youtube-transcripts/bernard-huang/RMg2eTZL7Jk.md)
- **Win the "best X" / comparison / alternatives pages.** ~43.8% of AI citations come from
  third-party "best X" lists — more than owned pages combined. Earn placement on the lists
  AI already trusts, aim for top positions, publish your own, keep them fresh (~80% of
  cited lists are recently updated). — [Jake Ward, LinkedIn](linkedin-posts/jake-ward/01-best-x-lists-ai-citations.md)
- **Refresh pages AI already cites first.** Don't guess — prioritize pages already used by
  AI, add missing entities + fresh data + your differentiators.
  — [Bernard Huang, transcript](youtube-transcripts/bernard-huang/f84ovVChEh4.md)
- **Reinforce the strengths models already associate with you.** Ask the LLM your brand's
  perceived strengths/weaknesses; bake the strengths into entity-rich passages.
  — [Bernard Huang, transcript](youtube-transcripts/bernard-huang/RMg2eTZL7Jk.md)
- **Size chunks for conversational context (~a minute of content), not one-liners**, so
  extracted passages survive multi-turn follow-ups.
  — [Bernard Huang, transcript](youtube-transcripts/bernard-huang/RMg2eTZL7Jk.md)
- **Write meta titles/descriptions to be "scroll-stopping."** On AIO SERPs ~47.5% of
  scrolling goes *backward* — your listing earns 2–3 impressions (down + back up), so the
  snippet must re-earn the click. — [Kevin Indig, LinkedIn](linkedin-posts/kevin-indig/02-aio-back-scroll-meta-descriptions.md)

### Technical foundations (or none of the above gets seen)
- **Server-side render critical content** — AI crawlers don't execute JavaScript.
- **Verify AI crawlers aren't blocked** by your host/CDN (many block by default) and test
  *each* platform's user agent (Claude/GPT/Perplexity ≠ Googlebot). Aleyda's own host was
  silently blocking AI bots. — [Aleyda Solís, transcript](youtube-transcripts/aleyda-solis/pqrwpXpMM6s.md)

---

## 5. Distribution & authority

- **Test organically, scale with ads.** If a post can't earn attention organically, paying
  to distribute it just helps more people ignore it. (B2B journey ≈ 272 days → sustained
  presence > one viral hit.) — Brendan Hufford (LinkedIn; distribution principle)
- **Content velocity signals legitimacy.** Sustained 100+ quality pages proves real
  business behind the site — spammers can't sustain it.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)
- **Build cross-web consensus.** One mention is an opinion; repeated mentions across
  trusted sources become an AI-visibility signal.
  — [Jake Ward, LinkedIn](linkedin-posts/jake-ward/01-best-x-lists-ai-citations.md)

---

## 6. Measurement (the part most teams fake)

- **GSC impressions are your 60-day leading indicator.** Impressions precede clicks; flat
  impressions for 60 days = course-correct now, don't wait 9 months.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)
- **Design a prompt-tracking *panel*, not a dashboard.** Score each engine separately
  (ChatGPT/Perplexity/Gemini/AIO), 5 reps/prompt/week, segment by buyer persona (CFO/IT/
  marketing), report mention rate + citation rate + avg position + sentiment **with
  confidence intervals**. — [Kevin Indig, LinkedIn](linkedin-posts/kevin-indig/01-prompt-tracking-aeo-b2b-saas.md)
- **Track topic-level share-of-voice, not individual prompts** (prompts are too
  personalized/long-tail to chase). — [Aleyda Solís, transcript](youtube-transcripts/aleyda-solis/pqrwpXpMM6s.md)
- **Test assumptions; don't inherit them.** Run controlled experiments (Cyrus's 23M
  internal-link study → internal-linking rules); measurement baselines are often wrong
  (Kevin: GSC data ~75% incomplete).
  — [Cyrus Shepard](other/newsletters-and-articles.md) · [Kevin Indig](other/newsletters-and-articles.md)
- **Internal links are the lever you control.** When target pages don't rank, point 20–50
  internal links from high-authority hubs.
  — [Nick Jordan, transcript](youtube-transcripts/nick-jordan/EJlgEt9CfCI.md)

---

## 7. The live debates (don't paper over these)

**AEO tactics — is it "just SEO"?**
- **Jake Ward:** 90% of AEO is SEO done well; schema, llms.txt, and .md files have ~0
  measurable impact — don't burn budget on them.
  [post](linkedin-posts/jake-ward/02-seo-aeo-geo-aio-2026.md)
- **Brendan Hufford:** Google says the same — and Google's public advice has historically
  protected Google (Chrome data, link building, both reversed at antitrust trial). His
  100+ AEO-prompts-per-client data doesn't match the official line; treat it as one data
  point. [post](linkedin-posts/brendan-hufford/02-dont-fully-trust-googles-aeo-guidance.md)
- **Working resolution:** skip the cheap "AI-specific" tactics (cheap to skip if useless),
  but *validate against your own AEO tracking* rather than trusting any party line.

**Quality vs. scale** — Nick (produce 100s of pages) vs. Brendan (lazy AI content is
disrespect). Resolution: scale is right *only* behind a real quality gate and genuine IP
extraction; volume of slop is the failure mode both would reject.

---

## 8. A concrete 30/60/90 starting sequence

**Days 0–30 — Foundation**
- Define central entity + topical map (Koray); pick the ~40 problem-weighted seed
  prompts/topics (Kevin, Eli).
- Run query fan-out sampling (Bernard) to find the AI-searched gaps.
- Fix technical foundations: SSR critical content, confirm AI crawlers aren't blocked
  (Aleyda).

**Days 31–60 — Production engine**
- Stand up the AI-assisted workflow with human review gates + on-page template (Gael, Nick).
- Publish 20–40 pages, prioritizing problem-intent + "best X"/comparison pages (Nick, Jake).
- Stand up the prompt-tracking panel + GSC impression baseline (Kevin, Nick).

**Days 61–90 — Compound & correct**
- Refresh pages AI already cites; build internal links to money pages (Bernard, Nick).
- Pursue third-party mentions/list placements for cross-web consensus (Jake, Aleyda).
- Read the panel: per-engine mention/citation trends + GSC impressions; cut what's flat.

---

## Source map

| Section | Primary sources |
|---|---|
| Mental models | Jake Ward, Brendan Hufford, Nick Jordan, Aleyda Solís |
| Strategy/architecture | Koray Gübür, Eli Schwartz, Nick Jordan, Kevin Indig |
| Production workflow | Gael Breton, Brendan Hufford, Nick Jordan |
| Semantic writing | Koray Gübür, Bernard Huang, Nick Jordan |
| AEO/GEO | Bernard Huang, Jake Ward, Kevin Indig, Aleyda Solís |
| Distribution/authority | Brendan Hufford, Nick Jordan, Jake Ward |
| Measurement | Kevin Indig, Nick Jordan, Aleyda Solís, Cyrus Shepard |

Full source list & selection rationale: [`sources.md`](sources.md).
