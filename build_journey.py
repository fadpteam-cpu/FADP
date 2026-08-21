"""Builds journey.html — the explorable project-journey tool.
Imports shared head/header/footer/cta from build_pages."""
import importlib.util, os

spec = importlib.util.spec_from_file_location("bp", os.path.join(os.path.dirname(__file__), "build_pages.py"))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

# Each stage: key, label, duration, one-line summary, what-we-do list,
# what-you-do list, cost note, and the "can I stop here" note.
STAGES = [
    dict(
        key="consult", n="01", label="Free consultation",
        dur="Week 1", cost="No charge", weeks=1,
        img='assets/img/phases/phase-01.png',
        summary="A conversation about your project, property and budget. No cost, no obligation.",
        we=[
            "Meet at the studio, on site, or by video call",
            "Understand the brief and the constraints",
            "An initial view on whether it will secure planning",
            "Explain the route, rough cost and realistic timeline",
        ],
        you=[
            "Tell us what you want to do, and your budget",
            "Share what you have: deeds, drawings, surveys",
            "Ask anything",
        ],
        stop="Nothing is committed. You leave with a written note of where you stand.",
    ),
    dict(
        key="feasibility", n="02", label="Feasibility & design",
        dur="Weeks 2–6", cost="Fixed fee, agreed first", weeks=5,
        img='assets/img/phases/phase-02.png',
        summary="We test what can be built, then design two or three options. You choose the direction.",
        we=[
            "Measure and survey the building or site",
            "Test what is possible against local policy",
            "Design two or three options, in drawings you can read",
            "Band the likely build cost for each",
        ],
        you=[
            "Tell us which option works and which does not",
            "Confirm your budget and priorities",
            "Pick the direction to take forward",
        ],
        stop="Stop here with drawings and a clear understanding of what your property can do.",
    ),
    dict(
        key="planning", n="03", label="Planning & approvals",
        dur="Weeks 6–16", cost="Fixed fee, agreed first", weeks=10,
        img='assets/img/phases/phase-03.png',
        summary="We prepare, submit and handle the council through to a decision.",
        we=[
            "Prepare the application and supporting statements",
            "Submit and manage the case officer throughout",
            "Respond to questions and objections on your behalf",
            "Update you in plain language at every step",
        ],
        you=[
            "Approve the drawings before we submit",
            "Nothing, at this stage",
            "Talk to neighbours early if we advise it",
        ],
        stop="Stop here with a consent that adds value to your property.",
    ),
    dict(
        key="technical", n="04", label="Technical design",
        dur="After approval", cost="Fixed fee, agreed first", weeks=6,
        img='assets/img/phases/phase-04.png',
        summary="The drawings that turn permission into something a builder can price and build.",
        we=[
            "Building regulations drawings and specifications",
            "Coordinate the structural engineer and consultants",
            "A tender package so builders price the same thing",
            "Take Principal Designer duties where they apply",
        ],
        you=[
            "Choose materials, layouts and finishes",
            "Review the package before it goes to builders",
        ],
        stop="Stop here with a priced-ready package and take it to builders yourself.",
    ),
    dict(
        key="build", n="05", label="On site to completion",
        dur="To completion", cost="Fixed fee, agreed first", weeks=None,
        img='assets/img/phases/phase-05.png',
        summary="The build, with a director on site, through to the certificates you keep.",
        we=[
            "Help you tender and appoint the builder",
            "Inspect the work on site as it goes",
            "Handle the questions that come up during the build",
            "See you through to completion and sign-off",
        ],
        you=[
            "Choose your builder with our guidance",
            "Watch it take shape; we handle the technical side",
        ],
        stop="Completion: your finished project, with the records you need if you sell.",
    ),
]


def stage_nav():
    out = []
    for i, s in enumerate(STAGES):
        p = f'../{s["img"]}' if False else s['img']  # journey.html is at root, so no prefix needed
        out.append(
            f'''      <button class="jn-tab{' active' if i==0 else ''}" data-stage="{s['key']}" role="tab" aria-selected="{'true' if i==0 else 'false'}" aria-controls="panel-{s['key']}" id="tab-{s['key']}">
        <span class="jn-icon" aria-hidden="true"><img src="{s['img']}" alt="" loading="lazy"></span>
        <span class="jn-num">{s['n']}</span>
        <span class="jn-label">{s['label']}</span>
        <span class="jn-dur">{s['dur']}</span>
      </button>''')
    return '\n'.join(out)


def stage_panels():
    out = []
    for i, s in enumerate(STAGES):
        we = '\n'.join(f'          <li>{x}</li>' for x in s['we'])
        you = '\n'.join(f'          <li>{x}</li>' for x in s['you'])
        hidden = '' if i == 0 else ' hidden'
        out.append(
            f'''    <div class="jn-panel{' active' if i==0 else ''}" id="panel-{s['key']}" role="tabpanel" aria-labelledby="tab-{s['key']}"{hidden}>
      <div class="jn-panel-head">
        <div class="jn-panel-meta"><span class="jn-panel-num">{s['n']}</span><span class="jn-panel-dur">{s['dur']} &#183; {s['cost']}</span></div>
        <h2>{s['label']}</h2>
        <p class="jn-summary">{s['summary']}</p>
      </div>
      <div class="jn-cols">
        <div class="jn-col">
          <h3>What we do</h3>
          <ul class="jn-do">
{we}
          </ul>
        </div>
        <div class="jn-col">
          <h3>What you do</h3>
          <ul class="jn-do you">
{you}
          </ul>
        </div>
      </div>
      <div class="jn-stop">
        <span class="jn-stop-icon" aria-hidden="true">&#10005;</span>
        <div><strong>Can you stop here?</strong> {s['stop']}</div>
      </div>
    </div>''')
    return '\n'.join(out)



def timeline():
    """Proportional timeline built in HTML so nothing distorts."""
    total = sum(s['weeks'] for s in STAGES if s['weeks']) + 4
    cells = []
    for s in STAGES:
        w = s['weeks'] if s['weeks'] else 4
        pct = (w / total) * 100
        cells.append(
            f'''      <div class="tl-cell" style="flex:{pct:.2f} 1 0">
        <span class="tl-num">{s['n']}</span>
        <span class="tl-bar"><i></i></span>
        <span class="tl-wk">{s['dur']}</span>
      </div>''')
    return '''
    <figure class="jn-timeline">
      <figcaption>Each bar is roughly how long that stage takes.</figcaption>
      <div class="tl-track">
''' + '\n'.join(cells) + '''
      </div>
      <p class="jn-timeline-note">A typical householder project: six to nine months, first call to starting on site.</p>
    </figure>
'''




def explainers():
    """The confusing bits, explained with a photo and plain English."""
    items = [
        (bp.IMG['p5'], "A rear extension under construction",
         "How far can I go out?",
         "Without planning permission, a single-storey rear extension can usually project <strong>3 metres</strong> from the original back wall on an attached house, or <strong>4 metres</strong> on a detached one. Go further and you need permission &#8212; which is often still achievable."),
        (bp.IMG['p8'], "Terraced houses sharing party walls",
         "What is a party wall?",
         "The wall or boundary you share with a neighbour. If you build on it, cut into it, or excavate deep foundations near it, the law says you must <strong>notify them in writing first</strong> &#8212; usually two months ahead. We handle the notices for you."),
        (bp.IMG['draw'], "Drawings prepared for a planning application",
         "What actually happens at the council?",
         "We submit, the council checks it is complete, then neighbours and consultees get their say for 21 days. An officer visits, writes a report, and a decision follows &#8212; <strong>usually within eight weeks</strong> for a house. "),
    ]
    cards = []
    for img, alt, h, p in items:
        cards.append(f'''      <figure class="ex-card">
        <img src="{img}" alt="{alt}" loading="lazy">
        <figcaption>
          <h3>{h}</h3>
          <p>{p}</p>
        </figcaption>
      </figure>''')
    return '''
<section class="jn-explain">
  <div class="wrap">
    <div class="sec-label"><span>The bits everyone finds confusing</span><em class="sec-sub">The three we are asked about most.</em></div>
    <div class="ex-grid">
''' + '\n'.join(cards) + '''
    </div>
  </div>
</section>
'''



body = f'''
<div class="page-hero journey-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Your project, step by step</div>
    <h1>What happens, from first call to finished project.</h1>
    <p class="lede">Explore each stage: what we do, what you do, and where you can stop.</p>
  </div>
</div>

<section class="journey-tool">
  <div class="wrap">
{timeline()}
    <div class="jn-tabs" role="tablist" aria-label="Project stages">
{stage_nav()}
    </div>
    <div class="jn-panels">
{stage_panels()}
    </div>
  </div>
</section>

{explainers()}

<section class="journey-cta">
  <div class="wrap">
    <div class="jc-inner">
      <h2>Ready to begin?</h2>
      <p>The first consultation is free.</p>
      <a class="btn" href="index.html#quote">Get in touch</a>
    </div>
  </div>
</section>
'''

html = (bp.head('Your project, step by step &#183; FADP Architecture',
                'Explore exactly what happens on an FADP project, from the first free consultation to a finished build. What we do, what you do, and where you can stop at every stage.',
                depth=0)
        + bp.header('journey', depth=0) + body + bp.cta_band(depth=0) + '\n' + bp.footer(depth=0))

open(os.path.join(os.path.dirname(__file__), 'journey.html'), 'w').write(html)
print("journey.html written")
