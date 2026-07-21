#!/usr/bin/env python3
"""Generates the FADP multi-page site from shared templates. Run once; commit output."""
import re

# ---------------------------------------------------------------- shared
def head(title, desc, depth=0, body_class=''):
    p = '../' * depth
    bc = f' class="{body_class}"' if body_class else ''
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="{p}favicon.svg">
<link rel="icon" type="image/png" href="{p}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/styles.css">
</head>
<body{bc}>
"""

def header(active, depth=0):
    p = '../' * depth
    def a(href, label, key):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{p}{href}"{cur}>{label}</a>'
    return f"""<header>
  <div class="header-inner">
    <a class="logo" href="{p}index.html">FADP Architecture</a>
    <nav class="site-nav">
      {a('index.html','Home','home')}
      {a('projects.html','Projects','projects')}
      <div class="has-mega">
        <button type="button" class="mega-btn{' current' if active=='services' else ''}" aria-haspopup="true">Services</button>
        <div class="mega" aria-label="Services menu">
          <div class="mega-inner">
            <div class="mega-col">
              <h5>Architectural Design &amp; Planning</h5>
              <a href="{p}services/planning-applications.html">Planning Permission</a>
              <a href="{p}services/feasibility-studies.html">Feasibility Studies</a>
              <a href="{p}services/site-analysis.html">Site Analysis</a>
              <a href="{p}services/outbuild-design.html">Outbuild Design</a>
              <a href="{p}services/sunroom.html">Sunroom</a>
              <a href="{p}services/dropped-kerb.html">Dropped Kerb</a>
            </div>
            <div class="mega-col">
              <h5>Renovation &amp; Remodelling</h5>
              <a href="{p}services/kitchen-renovation.html">Kitchen Renovation</a>
              <a href="{p}services/bathroom-renovation.html">Bathroom Renovation</a>
              <a href="{p}services/bedroom-renovation.html">Bedroom Renovation</a>
              <a href="{p}services/chimney-removal.html">Chimney Removal</a>
            </div>
            <div class="mega-col">
              <h5>Home Extension</h5>
              <a href="{p}services/side-extension.html">Side Extension</a>
              <a href="{p}services/rear-extension.html">Rear Extension</a>
              <a href="{p}services/wrap-around-extension.html">Wrap-around Extension</a>
              <h5 class="stacked">Structural Engineering</h5>
              <a href="{p}services/wall-removal.html">Wall Removal</a>
              <a href="{p}services/structural-calculations.html">Structural Calculations</a>
            </div>
            <div class="mega-col">
              <h5>Survey &amp; Inspection</h5>
              <a href="{p}services/crack-inspection.html">Crack Inspection</a>
              <a href="{p}services/structural-inspection.html">Structural Inspection</a>
              <a href="{p}services/snagging-survey.html">Snagging Survey</a>
              <a href="{p}services/property-condition-survey.html">Property Condition Survey</a>
              <a href="{p}services/structural-report.html">Structural Report</a>
            </div>
            <div class="mega-col">
              <h5>Home Conversion</h5>
              <a href="{p}services/loft-conversion.html">Loft Conversion</a>
              <a href="{p}services/basement-conversion.html">Basement Conversion</a>
              <a href="{p}services/garage-conversion.html">Garage Conversion</a>
              <a href="{p}services/hmo-conversion.html">HMO Conversion</a>
              <a href="{p}services/barn-conversion.html">Barn Conversion</a>
              <a href="{p}services/smart-flat-conversion.html">Smart Flat Conversion</a>
            </div>
            <div class="mega-col">
              <h5>Heritage &amp; Compliance</h5>
              <a href="{p}services/listed-buildings.html">Listed Buildings</a>
              <a href="{p}services/conservation-areas.html">Conservation Areas</a>
              <a href="{p}services/principal-designer.html">Principal Designer</a>
              <a href="{p}services/party-wall-award.html">Party Wall Award</a>
              <a href="{p}services/boundary-dispute-solutions.html">Boundary Dispute Solutions</a>
              <a href="{p}services/build-over-agreements.html">Build Over Agreements</a>
              <h5 class="stacked">New Build Design</h5>
              <a href="{p}services/new-homes.html">New Homes</a>
              <a href="{p}services/conservatory.html">Conservatory</a>
            </div>
            <div class="mega-foot">
              <span>Not sure where to start?</span>
              <a href="{p}index.html#quote">Get a fixed-fee quote</a>
            </div>
          </div>
        </div>
      </div>
      {a('about.html','About','about')}
      {a('blog.html','Blog','blog')}
    </nav>
    <div class="header-right">
      <a class="header-tel" href="tel:+442080000000">020 8000 0000</a>
      <a class="btn header-btn" href="{p}index.html#quote">Get a quote</a>
      <button class="menu-btn">Menu</button>
    </div>
  </div>
</header>
"""

def trust_band():
    return """<div class="trust-band">
  <div class="wrap">
    <ul>
      <li>Fixed written fees</li>
      <li>Fast turnaround</li>
      <li>Free consultation</li>
      <li>Director-led projects</li>
    </ul>
    <span class="tb-reviews"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 5.0 on Google &#183; 42 reviews</span>
  </div>
</div>
"""

def cta_band(depth=0):
    p = '../' * depth
    return f"""<div class="cta-band">
  <div class="wrap">
    <div>
      <h2>Get a fixed-fee quote for your project.</h2>
      <p>Five quick questions. A written quote within one working day.</p>
    </div>
    <a class="btn" href="{p}index.html#quote">Get a fixed-fee quote</a>
  </div>
</div>
"""

def footer(depth=0):
    p = '../' * depth
    return f"""<footer>
  <div class="footer-grid">
    <div class="footer-logo">
      <div class="f-mark">FADP</div>
      <div class="f-sub">Architecture London</div>
    </div>
    <div class="footer-col">
      <h5>London</h5>
      <address>
        66 Paul Street<br>
        London EC2A 4NA<br>
        United Kingdom
      </address>
      <a class="f-tel" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
    </div>
    <div class="footer-col">
      <h5>Services</h5>
      <a class="f-link" href="{p}services/planning-applications.html">Planning Applications</a>
      <a class="f-link" href="{p}services/bim.html">BIM</a>
      <a class="f-link" href="{p}services/feasibility-studies.html">Feasibility Studies</a>
      <a class="f-link" href="{p}services/listed-buildings.html">Listed Buildings</a>
      <a class="f-link" href="{p}services/principal-designer.html">Principal Designer</a>
    </div>
    <div class="footer-col">
      <h5>Information</h5>
      <a class="f-link" href="{p}projects.html">Projects</a>
      <a class="f-link" href="{p}about.html">About &amp; Team</a>
      <a class="f-link" href="{p}blog.html">Blog</a>
      <a class="f-link" href="{p}index.html#quote">Get a Quote</a>
      <a class="f-link" href="#">Privacy Policy</a>
    </div>
  </div>
  <div class="footer-bottom">
    <a class="g-badge" href="#" aria-label="Read our Google reviews">
      <svg viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
      <span class="g-body">
        <span class="g-score">5.0 <span class="g-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span></span>
        <span class="g-count">42 reviews</span>
      </span>
    </a>
    <div class="socials">
      <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.5" fill="#FFFFFF"/></svg></a>
      <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M6.5 10v10 M6.5 5.8v.01 M11.5 20V13.8c0-1.9 1.4-3.3 3.2-3.3s3.3 1.4 3.3 3.3V20 M11.5 10v10"/></svg></a>
      <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M15.5 4.5h-2.2c-2 0-3.3 1.3-3.3 3.4v2.3H7.5v3.1H10v7.2h3.2v-7.2h2.6l.5-3.1h-3.1V8.3c0-.6.3-.9 1-.9h2.3z"/></svg></a>
      <a href="#" aria-label="Houzz"><svg viewBox="0 0 24 24"><path d="M5 21V10.5L12 6l7 4.5V21h-5v-6h-4v6z"/></svg></a>
    </div>
  </div>
  <div class="footer-legal">
    <span>&#169; 2026 Fa Design Partners Limited, trading as FADP Architecture &#183; Registered in England &amp; Wales, company no. 17331773 &#183; Registered office: 66 Paul Street, London EC2A 4NA</span>
  </div>
</footer>
<div class="mobile-bar">
  <a href="tel:+442080000000">Call the studio</a>
  <a class="mb-primary" href="{p}index.html#quote">Get a fixed-fee quote</a>
</div>
<script src="{'../' * depth}js/main.js"></script>
</body>
</html>
"""

def councils(depth=0):
    return """<div class="councils">
  <div class="wrap">
    <span class="c-label">London boroughs we work across</span>
    <span class="c-list">Camden &#183; Islington &#183; Hackney &#183; Westminster &#183; Haringey &#183; Barnet &#183; Lambeth &#183; Wandsworth</span>
  </div>
</div>
"""

U = 'https://images.unsplash.com/'
IMG = {
    # -------- Hero: original kitchen interior --------
    'hero':    U+'photo-1600607687939-ce8a6c25118c?w=2200&q=90',  # modern kitchen interior with breakfast bar and pendant lights

    # -------- Projects: verified finished interiors + UK exteriors --------
    # Interiors (kitchens, refurbishments, extensions, new-build interiors)
    'p1':      U+'photo-1600607687939-ce8a6c25118c?w=1200&q=90',  # finished kitchen interior (repeats hero — Willow Road hero case study)
    'p2':      U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # white kitchen island (Jason Briscoe, verified finished)
    'p4':      U+'photo-1600607687939-ce8a6c25118c?w=1200&q=90',  # same finished kitchen (Chepstow, Notting Hill refurb)
    'p5':      U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # finished kitchen (Cadogan Mews extension)
    'p7':      U+'photo-1600607687939-ce8a6c25118c?w=1200&q=90',  # finished kitchen (Elder Yard new build)

    # UK exteriors (verified from earlier Unsplash fetches)
    'p3':      U+'photo-1683619589011-a0a8c7260029?w=1200&q=90',  # Clapham brick building (Regan-Asante) — Shoreditch commercial
    'p6':      U+'photo-1509732499382-20be2145852e?w=1200&q=90',  # Kensington doorway (Bruno Martins) — Barnsbury private house
    'p8':      U+'photo-1512359953714-f0c9a632ab85?w=1200&q=90',  # Portobello Road (Bethany Opler) — Rowan House Highgate
    'p9':      U+'photo-1683619589011-a0a8c7260029?w=1200&q=90',  # Clapham brick (repeats p3) — Fenwick Studios Peckham

    # -------- Contextual images (studio/technical/heritage) --------
    'studio':  U+'photo-1503387762-592deb58ef4e?w=1200&q=90',  # architectural desk / studio interior
    'draw':    U+'photo-1581092160562-40aa08e78837?w=1200&q=90',  # architectural drawings
    'model':   U+'photo-1503389152951-9f343605f61e?w=1200&q=90',  # 3D model / drawings
    'site':    U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # finished kitchen (was construction — now shows finished work)
    'listed':  U+'photo-1509732499382-20be2145852e?w=1200&q=90',  # Kensington heritage doorway (Bruno Martins)

    # -------- Team headshots (neutral professional) --------
    'team1':   U+'photo-1560250097-0b93528c311a?w=800&q=85',
    'team2':   U+'photo-1573496359142-b8d87734a5a2?w=800&q=85',
    'team3':   U+'photo-1519085360753-af0119f7cbe7?w=800&q=85',
    'team4':   U+'photo-1580489944761-15a19d654956?w=800&q=85',
}

def project(img, name, meta):
    return f"""      <a class="project" href="projects.html">
        <img src="{img}" alt="" loading="lazy">
        <div class="p-cap">
          <div class="p-name">{name}</div>
          <div class="p-loc">{meta}</div>
        </div>
      </a>"""

# ---------------------------------------------------------------- HOME
home_body = f"""
<div class="hero-overlay">
  <img class="hero-bg" src="{IMG['hero']}" alt="A contemporary open-plan living space">
  <div class="hero-content wrap">
    <h1>Architecture for houses, extensions and commercial buildings across London.</h1>
    <div class="hero-ctas">
      <a class="btn btn-light" href="#quote">Get a fixed-fee quote</a>
    </div>
  </div>
</div>

<section id="work">
  <div class="wrap">
    <div class="sec-label"><span>Recent work</span><a class="link" href="projects.html">All projects</a></div>
    <div class="work-grid">
{project(IMG['p1'],'Private house','Hampstead &#183; 2025')}
{project(IMG['p2'],'Refurbishment','Islington &#183; 2024')}
{project(IMG['p5'],'Extension','Chelsea &#183; 2023')}
{project(IMG['p3'],'Commercial','Shoreditch &#183; 2024')}
    </div>
  </div>
</section>

<section id="services-panels">
  <div class="wrap">
    <div class="sec-label"><span>What do you want to build?</span><a class="link" href="services.html">All services</a></div>
    <div class="svc-panels">
      <a class="panel" href="#quote" data-project="Extension">
        <img src="{IMG['p5']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Extensions</h3><span class="panel-cta">Get a fixed-fee quote</span></div>
      </a>
      <a class="panel" href="#quote" data-project="Loft conversion">
        <img src="{IMG['p8']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Loft conversions</h3><span class="panel-cta">Get a fixed-fee quote</span></div>
      </a>
      <a class="panel" href="#quote" data-project="Refurbishment">
        <img src="{IMG['p2']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Refurbishment</h3><span class="panel-cta">Get a fixed-fee quote</span></div>
      </a>
      <a class="panel" href="#quote" data-project="New build">
        <img src="{IMG['p1']}" alt="" loading="lazy">
        <div class="panel-body"><h3>New homes</h3><span class="panel-cta">Get a fixed-fee quote</span></div>
      </a>
      <a class="panel" href="#quote" data-project="Commercial">
        <img src="{IMG['p3']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Commercial</h3><span class="panel-cta">Get a fixed-fee quote</span></div>
      </a>
      <a class="panel" href="services/planning-applications.html">
        <img src="{IMG['draw']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Planning only</h3><span class="panel-cta">How we handle planning</span></div>
      </a>
    </div>
  </div>
</section>

<section id="reviews">
  <div class="wrap">
    <div class="sec-label"><span>What working with us looks like</span></div>
    <div class="promises">
      <div class="promise">
        <h4>You deal with a director</h4>
        <p>From the first consultation to the last site visit, the person you meet is the person doing the work. Nothing is handed down a chain.</p>
      </div>
      <div class="promise">
        <h4>Fees are fixed, in writing</h4>
        <p>Every stage is quoted and agreed before it begins. No hourly billing, no scope creep, no invoice you did not see coming.</p>
      </div>
      <div class="promise">
        <h4>You can stop at any stage</h4>
        <p>Work is staged so you can review, decide, and leave at the end of any stage without penalty. The commitment is earned, not locked in.</p>
      </div>
    </div>
    <p class="reviews-note">As a new practice we are building our public review record. Early clients receive our fullest attention &#8212; and our request for an honest review at the end.</p>
  </div>
</section>

<section id="directors">
  <div class="wrap">
    <div class="sec-label"><span>Who you\'ll work with</span><a class="link" href="about.html">More about the practice</a></div>
    <div class="directors-strip">
      <div class="director">
        <img src="{IMG['team1']}" alt="Aun Naeem, Director" loading="lazy">
        <div class="d-body">
          <h3>Aun Naeem</h3>
          <div class="d-role">Director &#183; Leads design</div>
          <p>Your first consultation is with a director. So is your last site visit.</p>
        </div>
      </div>
      <div class="director">
        <img src="{IMG['team2']}" alt="Fatima Shakeel, Director" loading="lazy">
        <div class="d-body">
          <h3>Fatima Shakeel</h3>
          <div class="d-role">Director &#183; Leads planning strategy</div>
          <p>Reads the local plan before drawing a line. Approvals first time, not argued twice.</p>
        </div>
      </div>
    </div>
    <p class="founding-note">FADP is a new London practice. Between them, its directors have delivered projects of every scale and stage inside established firms &#8212; houses, extensions, commercial and mixed-use. That experience now goes straight into your project, director-led, with terms most practices will not put in writing. Be one of our first clients.</p>
  </div>
</section>
"""

# ---------------------------------------------------------------- read the wizard + partners from current index
cur = open('index.html').read()
wiz = re.search(r'(<!-- QUOTE WIZARD -->.*?</section>)', cur, re.S).group(1)
partners = re.search(r'(<!-- PARTNERS -->.*?</section>)', cur, re.S).group(1)

home = head('FADP Architecture &#183; Architects, London',
            'FADP is an independent architecture practice in London. Planning, design and delivery with fixed written fees. Free consultation.', body_class='overlay-hero') \
     + header('home') + home_body + '\n' + wiz + '\n' + partners + '\n' + footer()

# ---------------------------------------------------------------- PROJECTS
projects_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Projects</div>
    <h1>Projects</h1>
    <p class="lede">Residential, commercial and conservation work across London. Every project photographed on completion; full drawings and planning history available at a studio visit.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="case">
      <img src="{IMG['p1']}" alt="A rear and side extension to a period house">
      <div class="case-body">
        <div class="case-tag">How we work</div>
        <h3>A conservation-area extension, start to finish</h3>
        <p>Take a four-bedroom period house in a conservation area, inside an Article 4 direction that has removed its permitted development rights. This is the kind of project our directors have delivered, and the way we run it at FADP.</p>
        <p>We start with feasibility and a pre-application to the borough, prepare the heritage and daylight assessments the officer will need, and design to secure approval first time. At tender we price the work across several contractors, then run the build to completion &#8212; with a director on it throughout.</p>
        <div class="case-facts">
          Approach: pre-application, then full application<br>
          Typical programme: 12 to 16 months, design to completion<br>
          Our role: full service, feasibility to completion
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-label"><span>The work we do</span></div>
    <div class="work-grid">
{project(IMG['p2'],'Milner Square','Islington &#183; Refurbishment, 2024')}
{project(IMG['p3'],'Kestrel Works','Shoreditch &#183; Commercial, 2024')}
{project(IMG['p4'],'Chepstow House','Notting Hill &#183; Interior, 2024')}
{project(IMG['p5'],'Cadogan Mews','Chelsea &#183; Extension, 2023')}
{project(IMG['p6'],'Barnsbury Terrace','Islington &#183; Private house, 2023')}
{project(IMG['p7'],'Elder Yard','Hackney &#183; New build, 2023')}
{project(IMG['p8'],'Rowan House','Highgate &#183; Extension, 2022')}
{project(IMG['p9'],'Fenwick Studios','Peckham &#183; Commercial, 2022')}
    </div>
  </div>
</section>
"""
projects = head('Projects &#183; FADP Architecture',
                'Residential, commercial and conservation architecture projects across London by FADP Architecture.') \
         + header('projects') + projects_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- SERVICES
SLUG = {'planning':'planning-applications','bim':'bim','site-analysis':'site-analysis',
        'feasibility':'feasibility-studies','listed':'listed-buildings',
        'conservation':'conservation-areas','principal-designer':'principal-designer'}
def svc(id_, kicker, title, paras, bullets, guide_href):
    ps = '\n'.join(f'      <p>{p}</p>' for p in paras)
    bs = '\n'.join(f'        <li>{b}</li>' for b in bullets)
    img = {'planning':IMG['draw'],'bim':IMG['model'],'site-analysis':IMG['site'],
           'feasibility':IMG['p7'],'listed':IMG['listed'],'conservation':IMG['p8'],
           'principal-designer':IMG['studio']}[id_]
    return f"""    <div class="svc-block" id="{id_}">
      <div class="svc-img"><img src="{img}" alt="{title}"></div>
      <div class="svc-copy">
        <div class="svc-kicker">{kicker}</div>
        <h2>{title}</h2>
{ps}
        <ul>
{bs}
        </ul>
        <div class="svc-links">
          <a class="link" href="services/{SLUG[id_]}.html">Learn more</a>
          <a class="link" href="index.html#quote">Get a fixed-fee quote</a>
        </div>
      </div>
    </div>"""

services_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Services</div>
    <h1>We know the regulations better than anyone.</h1>
    <p class="lede">Seven specialist services, each backed by a written guide and real approvals. Fixed fees for every stage, confirmed before work begins. If you're not sure which applies to your project, the free consultation is for working that out.</p>
  </div>
</div>

{councils()}

<section>
  <div class="wrap">
{svc('planning','01 &#183; Consents','Planning Applications',
  ["Householder, full, listed building and advertisement consents, prepared and submitted on your behalf. We read the local plan and the officers' recent decisions before we draw a line, which is why our applications are designed to be approved, not argued.",
   "Where the case is finely balanced we run a pre-application first, so you know the council's position before committing to a full submission."],
  ['Pre-application advice and strategy','Householder and full applications','Discharge of conditions and amendments','Appeals, where a refusal is wrong'],
  'blog/planning-permission-rear-extension.html')}
{svc('bim','02 &#183; Technical design','Building Information Modelling (BIM)',
  ['Every project is modelled in 3D, not drawn flat. A coordinated BIM model finds the clashes between structure, drainage and services on screen, where they cost nothing, instead of on site, where they cost thousands.',
   'The model also produces accurate quantities, which is why our tender returns price tightly and our clients rarely see a surprise variation.'],
  ['Fully coordinated 3D models','Clash detection before tender','Accurate quantities and schedules','Visualisations you can walk through'],
  'blog.html')}
{svc('site-analysis','03 &#183; Due diligence','Site Analysis',
  ['Before design begins we establish what the site will actually allow: orientation and daylight, overlooking and privacy, tree protection orders, flood risk, rights of light, boundary positions and ground conditions.',
   'An honest constraints report at the start prevents an expensive redesign later. It is the least glamorous work we do and some of the most valuable.'],
  ['Constraints and opportunities report','Daylight and overshadowing checks','TPO, flood and heritage screening','Measured surveys arranged and reviewed'],
  'blog.html')}
{svc('feasibility','04 &#183; Before you commit','Feasibility Studies',
  ['A short, fixed-fee study that answers the three questions every project starts with: what can be built, will it get planning, and roughly what will it cost.',
   'You receive drawn options, a planning risk assessment and cost banding, and you can stop there with no obligation to continue. Many clients use a feasibility study before they even purchase a property.'],
  ['Drawn options appraisal','Planning risk assessment','Build cost banding','Pre-purchase feasibility for buyers'],
  'blog.html')}
{svc('listed','05 &#183; Heritage','Listed Buildings',
  ["Listed building consent is a different discipline from ordinary planning: the test is harm to significance, and the officer's judgement is shaped by the quality of the heritage statement in front of them.",
   "We prepare the statement, the schedule of works and the justification together, and we deal with the conservation officer directly, in their language."],
  ['Listed building consent applications','Heritage statements and impact assessments','Schedules of works and repairs','Negotiation with conservation officers'],
  'blog.html')}
{svc('conservation','06 &#183; Heritage','Conservation Areas',
  ['Conservation areas remove or restrict permitted development, and many carry Article 4 directions that go further. Designing here means knowing exactly which rights survive on your street and what the council has recently approved two doors down.',
   'Our applications lead with that evidence, which is why sympathetic does not have to mean timid.'],
  ['Article 4 and PD rights checks','Design in context, evidenced by precedent','Conservation area consent','Street-scene and townscape drawings'],
  'blog.html')}
{svc('principal-designer','07 &#183; Duty holder','Principal Designer',
  ['Under CDM 2015 and the Building Safety Act 2022, most projects require a Principal Designer, a legal duty-holder responsible for planning, managing and monitoring design-phase safety and, for higher-risk buildings, compliance with building regulations.',
   'We take the appointment formally, keep the records the law requires, and make sure your project never trips on a duty nobody knew they held.'],
  ['Principal Designer under CDM 2015','Principal Designer under the Building Safety Act','Design risk registers and records','Higher-risk building gateway support'],
  'blog.html')}
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="sec-label"><span>Common questions</span></div>
    <div class="faq">
      <details open>
        <summary>How much does an architect cost? <span class="m">+</span></summary>
        <div class="a">It depends on the scope, but you'll know before you commit: we quote a fixed fee for each work stage in writing, after the free consultation. For a typical London extension, fees are set out as a defined percentage of build cost or a fixed sum. We'll set out both options and you choose.</div>
      </details>
      <details>
        <summary>Do I need planning permission? <span class="m">+</span></summary>
        <div class="a">Not always. Many extensions and loft conversions fall under permitted development. Assessing this is one of the first things we do, and it's covered in the free consultation. Where an application is needed, we prepare and submit it for you. <a class="link" href="blog/planning-permission-rear-extension.html">Read the full guide.</a></div>
      </details>
      <details>
        <summary>How long will my project take? <span class="m">+</span></summary>
        <div class="a">As a guide: design and planning typically take 3 to 5 months (councils have an 8-week statutory determination period), technical design 4 to 8 weeks, and construction from 3 months for an extension to a year or more for a new house. We'll give you a written programme for your specific project.</div>
      </details>
      <details>
        <summary>What if I only want drawings, not the full service? <span class="m">+</span></summary>
        <div class="a">That's fine. Because our appointments are broken into clear stages, you can engage us for planning drawings only, or up to tender, and stop at the end of any stage without penalty.</div>
      </details>
    </div>
  </div>
</section>
"""
services = head('Services &#183; FADP Architecture',
                'Planning applications, BIM, site analysis, feasibility studies, listed buildings, conservation areas and Principal Designer services in London.') \
         + header('services') + services_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- ABOUT
about_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; About</div>
    <h1>About the practice</h1>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="narrative">
      <div class="n-copy">
        <p>FADP is a new London practice, founded by two directors who have between them delivered projects of every scale and stage &#8212; from private houses and extensions to commercial and mixed-use schemes &#8212; inside larger firms. We started FADP around one conviction: that the difference between a good project and a painful one is rarely the design. It is certainty, about fees, about planning, about who is responsible for what.</p>
        <p class="stand">The experience is senior. The practice is new. You get both.</p>
        <p>The practice is built around that promise. Every appointment is broken into clear stages with fixed written fees, and every planning application is grounded in the local plan and the council's own recent decisions. FADP is led by its two directors, so the person you meet at the first consultation is a director of the practice, and stays your point of contact to completion.</p>
        <p>We work across residential, commercial and heritage projects in London and the South East, from feasibility studies for buyers to full services on listed buildings. Because we are small and director-led, the experience we built on larger schemes goes directly into your project, without being handed down a chain.</p>
        <p>We stay deliberately small. Small enough that nothing is handed down a chain, and senior people do the work you're paying senior fees for.</p>
        <p class="creds-line">Independent and director-led, with full professional indemnity insurance and fixed fees put in writing before every stage.</p>
      </div>
      <div class="n-img">
        <img src="{IMG['studio']}" alt="The FADP studio">
      </div>
    </div>
  </div>
</section>

{councils()}

<section id="team">
  <div class="wrap">
    <div class="sec-label"><span>The team</span></div>
    <div class="team-grid two">
      <div class="member">
        <img src="{IMG['team1']}" alt="Aun Naeem, Director" loading="lazy">
        <h3>Aun Naeem</h3>
        <div class="m-role">Director</div>
        <p class="m-bio">Co-founder of the practice. Leads design and client relationships, from the first consultation through planning to completion on site.</p>
      </div>
      <div class="member">
        <img src="{IMG['team2']}" alt="Fatima Shakeel, Director" loading="lazy">
        <h3>Fatima Shakeel</h3>
        <div class="m-role">Director</div>
        <p class="m-bio">Co-founder of the practice. Leads planning strategy and technical delivery, and is the point of contact through construction.</p>
      </div>
    </div>
  </div>
</section>
"""
about = head('About &#183; FADP Architecture',
             'FADP is an independent London architecture practice founded in 2014. Meet the team and see how we work.') \
      + header('about') + about_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- BLOG INDEX
blog_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="ph-row">
      <h1>Blog</h1>
      <span class="ph-count">6 articles</span>
    </div>
  </div>
</div>

<section class="posts-lg-wrap">
  <div class="wrap">
    <div class="posts-lg">
      <a class="post-lg" href="blog/planning-permission-rear-extension.html">
        <div class="pl-img"><img src="{IMG['p5']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Planning &#183; 7 min read</span>
          <h3>Do you need planning permission for a rear extension?</h3>
          <p>Often not, thanks to permitted development. But the exceptions catch people out every week. The rules, referenced to the legislation.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
      <a class="post-lg" href="blog/listed-building-consent.html">
        <div class="pl-img"><img src="{IMG['listed']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Heritage &#183; 8 min read</span>
          <h3>Listed building consent, explained</h3>
          <p>A separate regime with its own tests and, unusually, criminal liability. How the system actually works, and how consent is won.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
      <a class="post-lg" href="blog/principal-designer-explained.html">
        <div class="pl-img"><img src="{IMG['studio']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Regulations &#183; 8 min read</span>
          <h3>What does a Principal Designer actually do?</h3>
          <p>The law requires one on almost every project, and if nobody is appointed the duties land on you. Two roles, two Acts, untangled.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
      <a class="post-lg" href="blog/conservation-area-permitted-development.html">
        <div class="pl-img"><img src="{IMG['p8']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Heritage &#183; 7 min read</span>
          <h3>Permitted development in conservation areas</h3>
          <p>Which rights survive designation, which are removed automatically, and what an Article 4 direction takes away street by street.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
      <a class="post-lg" href="blog/how-bim-cuts-construction-costs.html">
        <div class="pl-img"><img src="{IMG['model']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Technical &#183; 7 min read</span>
          <h3>How BIM cuts construction costs: the evidence</h3>
          <p>Government measured it: benefits of 1.5 to 3 percent of whole-life cost. Where the money is saved, with the studies cited.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
      <a class="post-lg" href="blog/feasibility-studies-before-you-buy.html">
        <div class="pl-img"><img src="{IMG['p7']}" alt="" loading="lazy"></div>
        <div class="pl-body">
          <span class="pl-kicker">Before you buy &#183; 6 min read</span>
          <h3>Feasibility studies: what you learn before you spend</h3>
          <p>What can be built, will it get planning, and what will it cost. The cheapest decision on the whole project, made first.</p>
          <span class="pl-more">Read article</span>
        </div>
      </a>
    </div>
  </div>
</section>
"""
blog = head('Blog &#183; FADP Architecture',
            'Plain-English guides to planning permission, listed buildings, BIM and building regulations from FADP Architecture.') \
     + header('blog') + blog_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- EXAMPLE ARTICLE
article_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> &#183; <a href="../blog.html">Blog</a> &#183; Planning</div>
  </div>
</div>

<section style="padding-top:32px;">
  <div class="wrap">
    <article class="article">
      <h1>Do you need planning permission for a rear extension?</h1>
      <div class="a-meta">Planning &#183; 6 min read &#183; Reviewed July 2026</div>
      <figure class="a-lead"><img src="{IMG['p5']}" alt="Rear extension, Chelsea" loading="lazy"></figure>

      <p>Short answer: often not, thanks to permitted development. But the exceptions catch people out every week, and building without the right consent can mean an enforcement notice and, in the worst case, demolition. Here is how the rules actually work for a typical London house.</p>

      <h2>Permitted development: the basics</h2>
      <p>Permitted development (PD) rights let you extend a house without a planning application, provided the extension stays inside strict limits set out in the General Permitted Development Order. For a single-storey rear extension on a house (not a flat), the headline limits are:</p>
      <ul>
        <li>Up to 3 metres deep on an attached house, or 4 metres on a detached house, measured from the original rear wall</li>
        <li>Maximum height of 4 metres, and no higher than 3 metres at the eaves within 2 metres of a boundary</li>
        <li>No more than half the land around the original house covered by additions</li>
        <li>Materials of similar appearance to the existing house</li>
      </ul>
      <p>Under the larger home extension scheme, single-storey rear extensions can go further, to 6 metres on an attached house and 8 metres on a detached one, but only after a prior approval process in which your neighbours are consulted.</p>

      <div class="a-note">"Original house" means the house as first built, or as it stood on 1 July 1948. If a previous owner already extended, some or all of your PD allowance may be used up. This is the single most common mistake we see.</div>

      <h2>When permitted development does not apply</h2>
      <p>PD rights are removed or restricted in several situations common in London:</p>
      <ul>
        <li><strong>Flats and maisonettes</strong> have no householder PD rights at all. Any extension needs planning permission.</li>
        <li><strong>Conservation areas</strong> restrict side extensions, cladding and roof alterations, and many London conservation areas carry an Article 4 direction removing rear-extension rights too.</li>
        <li><strong>Listed buildings</strong> need listed building consent for almost any alteration, inside or out, regardless of PD.</li>
        <li><strong>Previous planning conditions</strong> sometimes remove PD rights from a specific property. This only shows up in a search of the planning history.</li>
      </ul>

      <h2>How to find out for certain</h2>
      <p>Three checks settle the question for any property:</p>
      <ol>
        <li>The council's planning history for the address, which reveals past extensions and any conditions removing PD rights</li>
        <li>The council's policy maps, which show conservation areas and Article 4 directions</li>
        <li>The listing register, for listed status</li>
      </ol>
      <p>Even where PD clearly applies, we recommend applying for a lawful development certificate. It costs a fraction of a planning application, and it is the document your solicitor and your buyer's solicitor will ask for when you sell.</p>

      <h2>If you do need permission</h2>
      <p>A householder application is determined within eight weeks of validation. The quality of the drawings and the planning statement decide most cases: an application grounded in the local plan and the council's own recent approvals on your street is designed to be approved rather than argued. That is the basis on which we prepare every application we submit.</p>

      <div class="a-cta">
        <h3>Not sure where your property stands?</h3>
        <p>We run the planning-history, Article 4 and listing checks as part of the free consultation, and tell you in writing whether you need an application at all.</p>
        <a class="btn" href="../index.html#quote">Request a free consultation</a>
      </div>
    </article>
  </div>
</section>
"""
article = head('Do you need planning permission for a rear extension? &#183; FADP Architecture',
               'Permitted development rules for rear extensions explained: size limits, conservation areas, Article 4 directions and lawful development certificates.', depth=1) \
        + header('blog', depth=1) + article_body + cta_band(depth=1) + '\n' + footer(depth=1)

# ---------------------------------------------------------------- write
import os
os.makedirs('blog', exist_ok=True)
open('index.html','w').write(home)
open('projects.html','w').write(projects)
open('services.html','w').write(services)
open('about.html','w').write(about)
open('blog.html','w').write(blog)
open('blog/planning-permission-rear-extension.html','w').write(article)
for f in ['index.html','projects.html','services.html','about.html','blog.html','blog/planning-permission-rear-extension.html']:
    print(f, os.path.getsize(f)//1024, 'KB')
