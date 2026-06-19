import os, datetime, textwrap
from youtube_transcript_api import YouTubeTranscriptApi

OUT = "research/youtube-transcripts"
TODAY = datetime.date.today().isoformat()

# (expert_slug, expert_name, video_id, title)
VIDEOS = [
    ("nick-jordan", "Nick Jordan", "EJlgEt9CfCI", "Insane Organic Traffic Growth w/ Nick Jordan (Content Distribution)"),
    ("koray-gubur", "Koray Tuğberk Gübür", "p6_0qWCgh3Q", "How to Rank #1 with Semantic SEO"),
    ("koray-gubur", "Koray Tuğberk Gübür", "81pe-YM9iRI", "AI-Powered Semantic SEO with Koray Gübür"),
    ("aleyda-solis", "Aleyda Solís", "pqrwpXpMM6s", "AI search crawlability & technical foundations (Humans of Martech #202)"),
    ("bernard-huang", "Bernard Huang", "RMg2eTZL7Jk", "How To Do AEO: prompt research, query fan-out, content (Live Session)"),
    ("bernard-huang", "Bernard Huang", "f84ovVChEh4", "AI-driven SEO revolution: the future of discoverability"),
    ("gael-breton", "Gael Breton", "blG6gss-mUY", "Automate $10K/Month in Tasks with AI (REAL Workflows You Can Steal)"),
    ("gael-breton", "Gael Breton", "c2fgBO0cpcw", "Cutting Through the AI Hype"),
]

api = YouTubeTranscriptApi()
ok, fail = 0, 0
for slug, name, vid, title in VIDEOS:
    d = os.path.join(OUT, slug)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{vid}.md")
    try:
        fetched = api.fetch(vid)
        text = " ".join(seg.text.replace("\n", " ") for seg in fetched)
        # wrap into readable paragraphs ~ every 700 chars at sentence-ish boundaries
        words = text.split()
        lines, cur = [], ""
        for w in words:
            cur += w + " "
            if len(cur) > 700:
                lines.append(cur.strip()); cur = ""
        if cur.strip(): lines.append(cur.strip())
        body = "\n\n".join(lines)
        header = textwrap.dedent(f"""\
        ---
        expert: {name}
        title: "{title}"
        source: https://www.youtube.com/watch?v={vid}
        video_id: {vid}
        collected: {TODAY}
        method: youtube-transcript-api (auto-captions, no API key)
        segments: {len(fetched)}
        ---

        # {title}
        **{name}** · [Watch on YouTube](https://www.youtube.com/watch?v={vid})

        > Transcript collected programmatically via `youtube-transcript-api`.
        > Lightly reformatted into paragraphs for readability; wording unchanged.

        ---

        """)
        with open(path, "w") as f:
            f.write(header + body + "\n")
        print(f"OK   {slug:14} {vid}  ({len(fetched)} segs, {len(text)} chars)")
        ok += 1
    except Exception as e:
        print(f"FAIL {slug:14} {vid}  {type(e).__name__}: {str(e)[:160]}")
        fail += 1
print(f"\nDone: {ok} ok, {fail} failed")
