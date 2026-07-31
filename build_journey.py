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
        dur="Week 1", cost="No charge",
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
        dur="Weeks 2–6", cost="Fixed fee, agreed first",
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
        dur="Weeks 6–16", cost="Fixed fee, agreed first",
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
        dur="After approval", cost="Fixed fee, agreed first",
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
        dur="To completion", cost="Fixed fee, agreed first",
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
    <div class="jn-progress-line" aria-hidden="true"></div>
    <div class="jn-tabs" role="tablist" aria-label="Project stages">
{stage_nav()}
    </div>
    <div class="jn-panels">
{stage_panels()}
    </div>
  </div>
</section>

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
