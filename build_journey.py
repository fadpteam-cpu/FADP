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
        icon='<circle cx="24" cy="16" r="7"/><path d="M10 40 Q10 28 24 28 Q38 28 38 40"/>',
        summary="A conversation about your project, your property and your budget. No cost, no obligation.",
        we=[
            "Meet you at the studio, on site, or by video call",
            "Listen to what you want to achieve and what you're worried about",
            "Give you an honest first read on whether it's likely to get planning",
            "Explain the route, the rough cost, and the realistic timeline",
        ],
        you=[
            "Tell us what you're hoping to do, and your budget if you have one",
            "Share any documents you already have (deeds, past drawings, surveys)",
            "Ask everything — no question is too basic",
        ],
        stop="Nothing is committed. You leave with a written note of where you stand and a fixed fee for the next stage, and you decide in your own time.",
    ),
    dict(
        key="feasibility", n="02", label="Feasibility & design",
        dur="Weeks 2–6", cost="Fixed fee, agreed first", weeks=5,
        icon='<path d="M12 38 V14 L24 8 L36 14 V38"/><path d="M12 22 H36"/><path d="M24 22 V38"/>',
        summary="We test what can actually be built, then design two or three options to your brief. You choose the direction before anything goes further.",
        we=[
            "Measure and survey the existing building or site",
            "Test what's possible against the local planning policy",
            "Design two to three real options, with drawings you can understand",
            "Band the likely build cost for each, so you can choose with your eyes open",
        ],
        you=[
            "React to the options honestly — tell us what you love and what you don't",
            "Confirm your budget and priorities so we design to them",
            "Pick the direction you want to take forward",
        ],
        stop="You can stop at the end of this stage with a set of drawings and a clear understanding of what your property can do — useful even if you pause the project for a year.",
    ),
    dict(
        key="planning", n="03", label="Planning & approvals",
        dur="Weeks 6–16", cost="Fixed fee, agreed first", weeks=10,
        icon='<rect x="12" y="8" width="24" height="32" rx="1"/><path d="M18 18 H30 M18 24 H30 M18 30 H26"/>',
        summary="We prepare and submit the application, handle the council, and manage every question through to a decision.",
        we=[
            "Prepare the full application and any supporting statements",
            "Submit to the council and manage the case officer throughout",
            "Respond to questions, objections and conditions on your behalf",
            "Keep you updated in plain language at every step — no silence",
        ],
        you=[
            "Approve the final drawings before we submit",
            "Sit back — this is the stage we take off your plate entirely",
            "Talk to neighbours early if we advise it (we'll guide you)",
        ],
        stop="Most householder applications are decided within eight weeks of validation. If approval matters before you commit further, you can stop here with a consent that adds value to your property.",
    ),
    dict(
        key="technical", n="04", label="Technical design",
        dur="After approval", cost="Fixed fee, agreed first", weeks=6,
        icon='<circle cx="24" cy="24" r="6"/><path d="M24 6 V12 M24 36 V42 M6 24 H12 M36 24 H42 M11 11 L15 15 M33 33 L37 37 M37 11 L33 15 M15 33 L11 37"/>',
        summary="The drawings that turn a planning permission into something a builder can actually price and build — structure, regulations, details.",
        we=[
            "Produce building regulations drawings and specifications",
            "Coordinate the structural engineer and any other consultants",
            "Prepare a tender package so builders price the same thing",
            "Take formal Principal Designer duties where they apply",
        ],
        you=[
            "Make your final choices on materials, layouts and finishes",
            "Review the package before it goes out to builders",
        ],
        stop="You can stop here with a complete, priced-ready package and take it to builders yourself, or ask us to carry on and run the build.",
    ),
    dict(
        key="build", n="05", label="On site to completion",
        dur="To completion", cost="Fixed fee, agreed first", weeks=None,
        icon='<path d="M8 40 H40 M12 40 V22 L24 14 L36 22 V40"/><rect x="20" y="28" width="8" height="12"/>',
        summary="The build itself, with a director inspecting on site, through to the certificates you keep for resale.",
        we=[
            "Help you tender and appoint the right builder",
            "Inspect the work on site as it progresses",
            "Deal with the questions and decisions that come up during the build",
            "See you through to completion and sign-off",
        ],
        you=[
            "Choose your builder with our guidance",
            "Enjoy watching it take shape — we handle the technical side",
        ],
        stop="This is completion: your finished project, with the certificates and records you'll need if you ever sell.",
    ),
]


def stage_nav():
    out = []
    for i, s in enumerate(STAGES):
        out.append(
            f'''      <button class="jn-tab{' active' if i==0 else ''}" data-stage="{s['key']}" role="tab" aria-selected="{'true' if i==0 else 'false'}" aria-controls="panel-{s['key']}" id="tab-{s['key']}">
        <span class="jn-icon" aria-hidden="true"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{s['icon']}</svg></span>
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
    """A proportional visual timeline: how long each stage takes, at a glance."""
    total = sum(s['weeks'] for s in STAGES if s['weeks'])
    segs, labels = [], []
    x = 0.0
    W = 1000.0
    for s in STAGES:
        w = s['weeks'] if s['weeks'] else 4      # 'to completion' shown as an open tail
        frac = (w / (total + 4)) * W
        mid = x + frac / 2
        segs.append(
            f'<rect class="tl-seg" data-stage="{s["key"]}" x="{x:.1f}" y="26" width="{max(frac-4,10):.1f}" height="16" rx="8"/>')
        segs.append(f'<circle class="tl-dot" data-stage="{s["key"]}" cx="{x+6:.1f}" cy="34" r="4"/>')
        labels.append(
            f'<text class="tl-num" x="{x:.1f}" y="16">{s["n"]}</text>')
        labels.append(
            f'<text class="tl-wk" x="{x:.1f}" y="62">{s["dur"]}</text>')
        x += frac
    return f'''
    <figure class="jn-timeline">
      <figcaption>The whole journey at a glance. Each bar is roughly how long that stage takes.</figcaption>
      <svg viewBox="0 0 1000 72" preserveAspectRatio="none" role="img" aria-label="Visual timeline of the five project stages, from a one week consultation through to completion on site.">
        {''.join(segs)}
        {''.join(labels)}
      </svg>
      <p class="jn-timeline-note">Typical householder project: about six to nine months from first call to starting on site. Bigger schemes take longer &#8212; we tell you which yours is at the first meeting.</p>
    </figure>
'''



def explainers():
    """Illustrated explanations of the things clients find most confusing."""
    return '''
<section class="jn-explain">
  <div class="wrap">
    <div class="sec-label"><span>The bits everyone finds confusing</span><em class="sec-sub">Three things clients ask us about most, explained simply.</em></div>
    <div class="ex-grid">

      <figure class="ex-card">
        <svg viewBox="0 0 260 150" role="img" aria-label="Diagram of a house with a rear extension, showing the three metre permitted development depth for an attached house and four metres for a detached house.">
          <rect class="ex-fill" x="20" y="52" width="90" height="72"/>
          <path class="ex-line" d="M20 52 L65 26 L110 52"/>
          <rect class="ex-ext" x="110" y="82" width="62" height="42"/>
          <line class="ex-dim" x1="110" y1="136" x2="172" y2="136"/>
          <path class="ex-dim" d="M110 132 v8 M172 132 v8"/>
          <text class="ex-t" x="141" y="149" text-anchor="middle">3m / 4m</text>
          <text class="ex-lbl" x="65" y="94">Existing</text>
          <text class="ex-lbl ex-lbl-b" x="141" y="106" text-anchor="middle">New</text>
          <line class="ex-ground" x1="8" y1="124" x2="252" y2="124"/>
        </svg>
        <figcaption>
          <h3>How far can I go out?</h3>
          <p>Without planning permission, a single-storey rear extension can usually project <strong>3 metres</strong> from the original back wall on an attached house, or <strong>4 metres</strong> on a detached one. Go further and you need permission &#8212; which is often still achievable.</p>
        </figcaption>
      </figure>

      <figure class="ex-card">
        <svg viewBox="0 0 260 150" role="img" aria-label="Diagram of two neighbouring houses sharing a party wall on the boundary line, with a three metre notice zone either side.">
          <rect class="ex-fill" x="18" y="56" width="102" height="68"/>
          <rect class="ex-fill" x="140" y="56" width="102" height="68"/>
          <line class="ex-boundary" x1="130" y1="34" x2="130" y2="132"/>
          <rect class="ex-zone" x="100" y="56" width="60" height="68"/>
          <text class="ex-lbl" x="69" y="96" text-anchor="middle">You</text>
          <text class="ex-lbl" x="191" y="96" text-anchor="middle">Neighbour</text>
          <text class="ex-t" x="130" y="26" text-anchor="middle">Party wall</text>
          <line class="ex-ground" x1="8" y1="124" x2="252" y2="124"/>
        </svg>
        <figcaption>
          <h3>What is a party wall?</h3>
          <p>The wall or boundary you share with a neighbour. If you build on it, cut into it, or excavate deep foundations near it, the law says you must <strong>notify them in writing first</strong> &#8212; usually two months ahead. We handle the notices for you.</p>
        </figcaption>
      </figure>

      <figure class="ex-card">
        <svg viewBox="0 0 260 150" role="img" aria-label="Flow diagram showing a planning application moving from submission to validation, then a consultation period, then a decision.">
          <rect class="ex-node" x="8" y="52" width="58" height="36" rx="6"/>
          <text class="ex-nt" x="37" y="74" text-anchor="middle">Submit</text>
          <path class="ex-arrow" d="M70 70 h20"/>
          <rect class="ex-node" x="94" y="52" width="66" height="36" rx="6"/>
          <text class="ex-nt" x="127" y="74" text-anchor="middle">Consult</text>
          <path class="ex-arrow" d="M164 70 h20"/>
          <rect class="ex-node ex-node-b" x="188" y="52" width="64" height="36" rx="6"/>
          <text class="ex-nt ex-nt-w" x="220" y="74" text-anchor="middle">Decision</text>
          <text class="ex-t" x="127" y="112" text-anchor="middle">usually about 8 weeks</text>
          <path class="ex-dim" d="M12 100 H248 M12 96 v8 M248 96 v8"/>
        </svg>
        <figcaption>
          <h3>What actually happens at the council?</h3>
          <p>We submit, the council checks it is complete, then neighbours and consultees get their say for 21 days. An officer visits, writes a report, and a decision follows &#8212; <strong>usually within eight weeks</strong> for a house. We chase it throughout.</p>
        </figcaption>
      </figure>

    </div>
  </div>
</section>
'''


body = f'''
<div class="page-hero journey-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Your project, step by step</div>
    <h1>What happens, from first call to finished project.</h1>
    <p class="lede">Every project runs the same clear path. Explore each stage below to see exactly what we do, what you do, and where you can stop. No jargon, no surprises.</p>
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
      <h2>Ready to start at stage one?</h2>
      <p>The first consultation is free, with no obligation. Answer five quick questions and a director will come back to you within one working day.</p>
      <a class="btn" href="index.html#quote">Get a fixed-fee quote</a>
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
