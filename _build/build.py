"""Builds the Scout jobs site from _build/roles.py.

Run from the repo root:  python3 _build/build.py
Writes index.html and one <slug>/index.html per active role.
"""
import html
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from roles import ROLES, CAL  # noqa: E402

e = html.escape
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@500;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">')


def head(title, prefix):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta property="og:title" content="{e(title)}">
<link rel="icon" href="{prefix}assets/logo.png">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
"""


def header(prefix, right_href, right_text):
    return f"""<header class="top">
  <div class="wrap">
    <a class="brand" href="{prefix or './'}" aria-label="Scout Talent open roles">
      <img src="{prefix}assets/logo.png" alt="Scout Talent logo" class="logo">
    </a>
    <a class="top-link" href="{right_href}">{right_text} &rarr;</a>
  </div>
</header>
"""


FOOTER = """<footer>
  <div class="wrap">Scout Talent &middot; Recruiting for startups and mission-driven teams &middot; <a href="https://www.letscout.co">letscout.co</a></div>
</footer>

</body>
</html>
"""


def paras(block):
    out = f'    <p class="lead">{e(block["lead"])}</p>\n'
    for p in block["paras"]:
        out += f"    <p>{e(p)}</p>\n"
    return out


def bullets(items):
    return "\n".join(f"      <li>{e(i)}</li>" for i in items)


def role_page(r):
    p = "../"
    facts = "\n".join(
        f'      <div class="fact"><div class="k">{e(k)}</div><div class="v">{e(v)}</div><div class="s">{e(s)}</div></div>'
        for k, v, s in r["facts"])
    own = "\n".join(f"      <li><strong>{e(b)}</strong> {e(t)}</li>" for b, t in r["own"])
    steps = "\n".join(
        f'      <div class="step"><div><div class="t">{e(t)}</div><div class="d">{e(d)}</div></div></div>'
        for t, d in r["steps"])
    about = ""
    if r.get("about"):
        about = f"""
  <section class="block">
    <h2>{e(r["about_title"])}</h2>
{paras(r["about"])}  </section>
"""
    ct, cb = r["callout"]
    return head(f'{r["title"]} at {r["company"]} | Scout', p) + "\n" + header(p, p, "All open roles") + f"""
<main class="wrap">

  <section class="hero">
    <span class="eyebrow">{e(r["tag"])}</span>
    <h1>{e(r["title"])}</h1>
    <p class="company">at <strong>{e(r["company"])}</strong> &middot; {e(r["location"])}</p>

    <div class="facts">
{facts}
    </div>

    <div class="cta-row">
      <a class="btn" href="{CAL}">Book 15 minutes to talk</a>
      <span class="cta-note">No resume needed for a first chat.</span>
    </div>

    <div class="urgent">
      <span class="dot" aria-hidden="true"></span>
      <div><strong>{e(ct)}</strong> {e(cb)}</div>
    </div>
  </section>
{about}
  <section class="block">
    <h2>The opportunity</h2>
{paras(r["opportunity"])}  </section>

  <section class="block">
    <h2>What you'll own</h2>
    <ul class="clean">
{own}
    </ul>
  </section>

  <section class="block">
    <h2>What they're looking for</h2>
    <div class="sub">Must-haves</div>
    <ul class="clean">
{bullets(r["must"])}
    </ul>
    <div class="sub">Bonus points</div>
    <ul class="clean">
{bullets(r["bonus"])}
    </ul>
  </section>

  <section class="block">
    <h2>Interview process</h2>
    <div class="steps">
{steps}
    </div>
  </section>

  <section class="block">
    <h2>Interested?</h2>
    <div class="recruiter">
      <div class="who">
        <div class="avatar" aria-hidden="true">M</div>
        <div>
          <div class="name">Monica</div>
          <div class="role">Founder &amp; Recruiter, Scout</div>
        </div>
      </div>
      <p>I'm recruiting for this role. If it sounds like you, or you want to know more before deciding, grab a time and we'll talk it through. Happy to share more on the team, comp, and what the first few months look like.</p>
      <div class="cta-row" style="margin-top:18px">
        <a class="btn" href="{CAL}">Book a time with me</a>
      </div>
      <div class="contact-line">Or email me: monica@letscout.co</div>
    </div>
  </section>

</main>

""" + FOOTER


def index_page(active):
    cards = "".join(f"""
    <a class="role-card" href="{r["slug"]}/">
      <span class="eyebrow">{e(r["tag"])}</span>
      <div class="rc-title">{e(r["title"])}</div>
      <div class="rc-co">{e(r["company"])} &middot; {e(r["location"])}</div>
      <p class="rc-blurb">{e(r["card_blurb"])}</p>
      <div class="rc-foot"><span class="rc-comp">{e(r["card_comp"])}</span><span class="rc-link">View role &rarr;</span></div>
    </a>""" for r in active)
    return head("Open Roles | Scout Talent", "") + "\n" + header("", "https://www.letscout.co", "letscout.co") + f"""
<main class="wrap">
  <section class="hero">
    <h1>Open roles</h1>
    <p class="company">Roles I'm recruiting for right now at startups and mission-driven teams. See one you like? Grab a time to talk, no resume needed for a first chat.</p>
    <div class="cta-row" style="margin:0 0 32px">
      <a class="btn" href="{CAL}">Book 15 minutes with Monica</a>
    </div>
  </section>
  <section class="roles">{cards}
  </section>
</main>

""" + FOOTER


def main():
    active = [r for r in ROLES if r.get("active", True)]
    active_slugs = {r["slug"] for r in active}
    all_slugs = {r["slug"] for r in ROLES}
    for r in active:
        d = os.path.join(ROOT, r["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w") as f:
            f.write(role_page(r))
    # Remove pages for roles marked inactive.
    for slug in all_slugs - active_slugs:
        d = os.path.join(ROOT, slug)
        if os.path.isdir(d):
            shutil.rmtree(d)
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(index_page(active))
    print("Built", len(active), "role pages:", ", ".join(sorted(active_slugs)))


if __name__ == "__main__":
    main()
