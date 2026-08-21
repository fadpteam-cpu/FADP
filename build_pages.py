#!/usr/bin/env python3
"""Generates the FADP multi-page site from shared templates. Run once; commit output."""
import re

# ---------------------------------------------------------------- shared
def head(title, desc, depth=0, body_class=''):
    p = '../' * depth
    bc = f' class="{body_class}"' if body_class else ''
    ldjson = ('{"@context":"https://schema.org","@type":"ProfessionalService",'
              '"name":"FADP Architecture",'
              '"legalName":"Fa Design Partners Limited",'
              '"url":"https://fadpteam-cpu.github.io/FADP/",'
              '"image":"https://fadpteam-cpu.github.io/FADP/assets/img/apple-touch-icon.png",'
              '"email":"design@fadp.co.uk",'
              '"description":"Architecture practice offering planning applications, feasibility studies, BIM, masterplanning, listed building consent and principal designer appointments across the United Kingdom.",'
              '"foundingDate":"2026-07-10",'
              '"address":{"@type":"PostalAddress","streetAddress":"66 Paul Street","addressLocality":"London","postalCode":"EC2A 4NA","addressCountry":"GB"},'
              '"geo":{"@type":"GeoCoordinates","latitude":51.5247,"longitude":-0.0857},'
              '"founder":[{"@type":"Person","name":"Aun Naeem","jobTitle":"Director","alumniOf":[{"@type":"CollegeOrUniversity","name":"Birmingham School of Architecture"},{"@type":"CollegeOrUniversity","name":"University of Sheffield"}]},'
              '{"@type":"Person","name":"Fatima Shakeel","jobTitle":"Director","alumniOf":[{"@type":"CollegeOrUniversity","name":"Birmingham School of Architecture"}]}],'
              '"areaServed":{"@type":"Country","name":"United Kingdom"},'
              '"hasOfferCatalog":{"@type":"OfferCatalog","name":"Architectural services","itemListElement":['
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Planning applications"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Feasibility studies"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Site analysis"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Building Information Modelling"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Masterplanning and urban design"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Listed building consent"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Conservation area applications"}},'
              '{"@type":"Offer","itemOffered":{"@type":"Service","name":"Principal Designer"}}]},'
              '"knowsAbout":["Architectural design","Planning applications","Feasibility studies","Masterplanning","Listed buildings","Conservation areas","BIM","CDM 2015","Building Safety Act 2022"]}')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="FADP Architecture">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://fadpteam-cpu.github.io/FADP/assets/img/hero-poster.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://fadpteam-cpu.github.io/FADP/assets/img/hero-poster.jpg">

<meta name="theme-color" content="#05308C">
<link rel="icon" href="{p}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{p}assets/img/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{p}assets/img/apple-touch-icon.png">

<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data: https://images.unsplash.com; style-src 'self' 'unsafe-inline'; font-src 'self'; script-src 'self'; frame-src https://www.openstreetmap.org; connect-src 'self'; base-uri 'self'; form-action 'self';">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta http-equiv="Permissions-Policy" content="geolocation=(), microphone=(), camera=()">

<link rel="preload" href="{p}assets/fonts/manrope-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/manrope-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}css/styles.css">

<script type="application/ld+json">{ldjson}</script>
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
      {a('journey.html','Your project','journey')}
      <div class="has-mega">
        <button type="button" class="mega-btn{' current' if active=='services' else ''}" aria-haspopup="true">Services</button>
        <div class="mega" aria-label="Services menu">
          <div class="mega-inner">
            <div class="mega-col">
              <h5>Architectural Design &amp; Planning</h5>
              <a href="{p}services/planning-applications.html">Planning Permission</a>
              <a href="{p}services/feasibility-studies.html">Feasibility Studies</a>
          <a href="{p}services/masterplanning-urban-design.html">Masterplanning &amp; Urban Design</a>
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
              <a href="{p}index.html#quote">Get in touch</a>
            </div>
          </div>
        </div>
      </div>
      {a('about.html','About','about')}
      {a('blog.html','Blog','blog')}
    </nav>
    <div class="header-right">
      <a class="btn header-btn" href="{p}index.html#quote">Get a quote</a>
      <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobileNav">
        <span class="mb-bars"><i></i><i></i></span>
      </button>
    </div>
  </div>
</header>

<div class="mobile-nav" id="mobileNav" hidden>
  <div class="mn-inner">
    <nav class="mn-primary">
      <a href="{p}index.html">Home</a>
      <a href="{p}projects.html">Projects</a>
      <a href="{p}journey.html">Your project</a>
      <a href="{p}about.html">About</a>
      <a href="{p}careers.html">Careers</a>
      <a href="{p}contact.html">Contact</a>
      <a href="{p}blog.html">Blog</a>
    </nav>
    <div class="mn-services">
      <h5>Services</h5>
      <a href="{p}services/planning-applications.html">Planning Permission</a>
      <a href="{p}services/feasibility-studies.html">Feasibility Studies</a>
      <a href="{p}services/rear-extension.html">Extensions</a>
      <a href="{p}services/loft-conversion.html">Loft Conversions</a>
      <a href="{p}services/basement-conversion.html">Basement Conversions</a>
      <a href="{p}services/listed-buildings.html">Listed Buildings</a>
      <a href="{p}services/principal-designer.html">Principal Designer</a>
      <a class="mn-all" href="{p}services.html">All services</a>
    </div>
    <div class="mn-foot">
      <a class="btn" href="{p}index.html#quote">Get in touch</a>
      <a class="mn-contact" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
    </div>
  </div>
</div>
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
      <h2>Start your project</h2>
      <p>A written, fixed-fee quote. No obligation.</p>
    </div>
    <a class="btn" href="{p}index.html#quote">Get in touch</a>
  </div>
</div>
"""

def footer(depth=0):
    p = '../' * depth
    return f"""<footer>
  <div class="footer-grid">
    <div class="footer-logo">
      <div class="f-mark">FADP</div>
      <div class="f-sub">Architecture</div>
    </div>
    <div class="footer-col">
      <h5>Studio</h5>
      <address>
        66 Paul Street<br>
        London EC2A 4NA
      </address>
      <a class="f-tel" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
    </div>
    <div class="footer-col">
      <h5>Services</h5>
      <a class="f-link" href="{p}services/planning-applications.html">Planning Applications</a>
      <a class="f-link" href="{p}services/bim.html">BIM</a>
      <a class="f-link" href="{p}services/feasibility-studies.html">Feasibility Studies</a>
      <a class="f-link" href="{p}services/masterplanning-urban-design.html">Masterplanning</a>
      <a class="f-link" href="{p}services/listed-buildings.html">Listed Buildings</a>
      <a class="f-link" href="{p}services/principal-designer.html">Principal Designer</a>
    </div>
    <div class="footer-col">
      <h5>Information</h5>
      <a class="f-link" href="{p}projects.html">Projects</a>
      <a class="f-link" href="{p}about.html">About</a>
      <a class="f-link" href="{p}careers.html">Careers</a>
      <a class="f-link" href="{p}contact.html">Contact</a>
      <a class="f-link" href="{p}blog.html">Blog</a>
      <a class="f-link" href="{p}index.html#quote">Get a quote</a>
      <a class="f-link" href="{p}terms.html">Terms</a>
      <a class="f-link" href="{p}privacy.html">Privacy</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">&#169; 2026 FADP Architecture</span>
    <div class="socials">
      <a href="https://www.instagram.com/fadpworks/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.5" fill="#FFFFFF"/></svg></a>
      <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24"><path d="M6.5 10v10 M6.5 5.8v.01 M11.5 20V13.8c0-1.9 1.4-3.3 3.2-3.3s3.3 1.4 3.3 3.3V20 M11.5 10v10"/></svg></a>
      <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M15.5 4.5h-2.2c-2 0-3.3 1.3-3.3 3.4v2.3H7.5v3.1H10v7.2h3.2v-7.2h2.6l.5-3.1h-3.1V8.3c0-.6.3-.9 1-.9h2.3z"/></svg></a>
      <a href="#" aria-label="Houzz"><svg viewBox="0 0 24 24"><path d="M5 21V10.5L12 6l7 4.5V21h-5v-6h-4v6z"/></svg></a>
    </div>
  </div>
</footer>
<div class="mobile-bar">
  <a href="mailto:design@fadp.co.uk">Email the studio</a>
  <a class="mb-primary" href="{p}index.html#quote">Get in touch</a>
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
    'hero':    'assets/img/hero-poster.jpg',  # modern kitchen interior with breakfast bar and pendant lights

    # -------- Projects: verified photos mapped by CONTENT, not by slot --------
    # p1-p4 feed the Recent Work section. p5-p8 feed the service panels.
    # Every image matches what its label describes.
    'p1':      U+'photo-1509732499382-20be2145852e?w=1200&q=90',  # Kensington doorway → Private house (Hampstead)
    'p2':      U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # white kitchen → Refurbishment (Islington)
    'p3':      U+'photo-1600607687939-ce8a6c25118c?w=1200&q=90',  # finished kitchen → Extension (Chelsea)
    'p4':      U+'photo-1683619589011-a0a8c7260029?w=1200&q=90',  # Clapham brick → Commercial (Shoreditch)
    'p5':      U+'photo-1600607687939-ce8a6c25118c?w=1200&q=90',  # finished kitchen → Extensions panel
    'p6':      U+'photo-1503387762-592deb58ef4e?w=1200&q=90',    # studio/skylit space → Loft conversions panel
    'p7':      U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # white kitchen → Refurbishment panel
    'p8':      U+'photo-1512359953714-f0c9a632ab85?w=1200&q=90',  # Portobello terrace → New homes panel (Georgian, aspirational)
    'p9':      U+'photo-1683619589011-a0a8c7260029?w=1200&q=90',  # Clapham brick (not on home)

    # -------- Real FADP project photography --------
    'project_wide':   'assets/img/project-industrial-wide.jpg',    # industrial building, wide shot
    'project_close':  'assets/img/project-industrial-close.jpg',   # industrial building, close
    'studio_working': 'assets/img/studio-aun-working.jpg',         # Aun sketching at studio
    'studio_sketch':  'assets/img/studio-sketching.jpg',           # hand sketching close-up
    'directors_desk': 'assets/img/blog-hero-directors.jpg',        # both directors at drawing table

    # -------- Contextual images (studio/technical/heritage) --------
    'studio':  U+'photo-1503387762-592deb58ef4e?w=1200&q=90',  # architectural desk / studio interior
    'draw':    U+'photo-1581092160562-40aa08e78837?w=1200&q=90',  # architectural drawings
    'model':   U+'photo-1503389152951-9f343605f61e?w=1200&q=90',  # 3D model / drawings
    'site':    U+'photo-1502005097973-6a7082348e28?w=1200&q=90',  # finished kitchen (was construction — now shows finished work)
    'listed':  U+'photo-1509732499382-20be2145852e?w=1200&q=90',  # Kensington heritage doorway (Bruno Martins)

    # -------- Team headshots (neutral professional) --------
    'team1':   'assets/img/aun-naeem.jpg',
    'team2':   'assets/img/fatima-shakeel.jpg',
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
  <video class="hero-bg" autoplay muted loop playsinline preload="auto"
         poster="assets/img/hero-poster.jpg" aria-hidden="true">
    <source src="assets/video/hero.mp4" type="video/mp4">
  </video>
  <div class="hero-content wrap">
    <h1>Architecture. Houses, extensions and commercial buildings.</h1>
    <div class="hero-ctas">
      <a class="btn btn-light" href="#quote">Get a free quote</a>
    </div>
  </div>
</div>

<section id="approach">
  <div class="wrap">
    <p class="approach-lead">We believe good architecture is quiet.</p>
    <p class="approach-body">Considered, not decorated. We take few projects and lead every one ourselves, from first sketch to final detail.</p>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="sec-label"><span>Recent work</span><a class="link" href="projects.html">All projects</a></div>
    <div class="work-grid">
{project(IMG['p3'],'Private house','Hampstead &#183; 2025')}
{project(IMG['p2'],'Refurbishment','Islington &#183; 2024')}
{project(IMG['p1'],'Extension','Chelsea &#183; 2023')}
{project(IMG['project_wide'],'Commercial','2024')}
    </div>
  </div>
</section>

<section id="reviews" class="stat-band">
  <div class="wrap">
    <div class="stat-head">
      <div class="sec-label"><span>The practice</span></div>
      <h2 class="stat-heading">Every project runs the same way. Director-led, fixed fee, on the record.</h2>
    </div>
    <div class="stat-grid">
      <div class="stat">
        <div class="stat-fig">2</div>
        <div class="stat-lbl">Directors</div>
        <div class="stat-note">Both take every meeting. No account managers, no handovers.</div>
      </div>
      <div class="stat">
        <div class="stat-fig">10<span class="stat-plus">+</span></div>
        <div class="stat-lbl">Years combined practice</div>
        <div class="stat-note">Delivered inside established practices before founding FADP.</div>
      </div>
      <div class="stat">
        <div class="stat-fig">6</div>
        <div class="stat-lbl">Sectors we work in</div>
        <div class="stat-note">Residential, commercial, cultural, religious, heritage and retrofit.</div>
      </div>
      <div class="stat">
        <div class="stat-fig">2026</div>
        <div class="stat-lbl">Founded</div>
        <div class="stat-note">Built from day one around fixed fees and director-led delivery.</div>
      </div>
    </div>
  </div>
</section>

<section id="services-panels">
  <div class="wrap">
    <div class="sec-label"><span>What do you want to build?</span><a class="link" href="services.html">All services</a></div>
    <div class="svc-panels">
      <a class="panel" href="#quote" data-project="Extension">
        <img src="{IMG['p5']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Extensions</h3><span class="panel-cta">Learn more</span></div>
      </a>
      <a class="panel" href="#quote" data-project="Loft conversion">
        <img src="{IMG['p6']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Loft conversions</h3><span class="panel-cta">Learn more</span></div>
      </a>
      <a class="panel" href="#quote" data-project="Refurbishment">
        <img src="{IMG['p7']}" alt="" loading="lazy">
        <div class="panel-body"><h3>Refurbishment</h3><span class="panel-cta">Learn more</span></div>
      </a>
      <a class="panel" href="#quote" data-project="New build">
        <img src="{IMG['p8']}" alt="" loading="lazy">
        <div class="panel-body"><h3>New homes</h3><span class="panel-cta">Learn more</span></div>
      </a>

    </div>
  </div>
</section>

<section id="directors">
  <div class="wrap">
    <div class="sec-label"><span>Studio leads</span><em class="sec-sub">Two directors. Every project.</em><a class="link" href="about.html">More about the practice</a></div>
    <div class="directors-strip">
      <div class="director">
        <img src="{IMG['team1']}" alt="Aun Naeem, Director" loading="lazy">
        <div class="d-body">
          <h3>Aun Naeem</h3>
          <div class="d-role">Director &#183; Leads design and masterplanning</div>
        </div>
      </div>
      <div class="director">
        <img src="{IMG['team2']}" alt="Fatima Shakeel, Director" loading="lazy">
        <div class="d-body">
          <h3>Fatima Shakeel</h3>
          <div class="d-role">Director &#183; Leads planning strategy</div>
        </div>
      </div>
    </div>
    <p class="founding-note brand-copy">Between them, the directors have delivered projects of every scale within established practices.</p>
  </div>
</section>


"""

# ---------------------------------------------------------------- read the wizard + partners from current index
cur = open('index.html').read()
wiz = re.search(r'(<!-- QUOTE WIZARD -->.*?</section>)', cur, re.S).group(1)
partners = re.search(r'(<!-- PARTNERS -->.*?</section>)', cur, re.S).group(1)

home = head('FADP Architecture',
            'FADP is an independent architecture practice in London. Planning, design and delivery with fixed written fees. Free consultation.', body_class='overlay-hero') \
     + header('home') + home_body + '\n' + wiz + '\n' + partners + '\n' + footer()

# ---------------------------------------------------------------- PROJECTS
projects_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Projects</div>
    <h1>Projects</h1>
    <p class="lede">Selected residential and conservation work.</p>
  </div>
</div>

<section>
  <div class="wrap">
    <a class="case" href="projects/englehurst.html">
      <img src="assets/img/projects/englehurst-front.jpg" alt="Englehurst — front elevation at dusk">
      <div class="case-body">
        <div class="case-tag">Featured &#183; Residential extension</div>
        <h3>Englehurst</h3>
        <p>A three-storey side and rear extension to a suburban house &mdash; brick base, painted timber cladding above, and a slate-clad dormer to the roof.</p>
        <div class="case-facts">
          Sector: Residential<br>
          Approach: Full extension and rear return<br>
          Status: In design
        </div>
      </div>
    </a>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-label"><span>Selected work</span></div>
    <div class="work-grid">
      <a class="project" href="projects/englehurst.html">
        <img src="assets/img/projects/englehurst-rear.jpg" alt="Englehurst rear elevation" loading="lazy">
        <div class="p-cap">
          <div class="p-name">Englehurst</div>
          <div class="p-loc">Residential extension</div>
        </div>
      </a>
{project(IMG['project_wide'],'Industrial','Commercial')}
{project(IMG['p2'],'Milner Square','Refurbishment')}
{project(IMG['p3'],'Kestrel Works','Commercial')}
    </div>
  </div>
</section>
"""
projects = head('Projects &#183; FADP Architecture',
                'Residential, commercial and conservation architecture projects by FADP Architecture.') \
         + header('projects') + projects_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- SERVICES
SLUG = {'planning':'planning-applications','bim':'bim','site-analysis':'site-analysis',
        'feasibility':'feasibility-studies','listed':'listed-buildings',
        'conservation':'conservation-areas','principal-designer':'principal-designer',
        'masterplanning':'masterplanning-urban-design'}
def svc(id_, kicker, title, paras, bullets, guide_href):
    ps = '\n'.join(f'      <p>{p}</p>' for p in paras)
    bs = '\n'.join(f'        <li>{b}</li>' for b in bullets)
    img = {'planning':IMG['draw'],'bim':IMG['model'],'site-analysis':IMG['site'],
           'feasibility':IMG['p7'],'listed':IMG['listed'],'conservation':IMG['p8'],
           'principal-designer':IMG['studio'],'masterplanning':IMG['p8']}[id_]
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
          <a class="link" href="index.html#quote">Enquire</a>
        </div>
      </div>
    </div>"""

services_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Services</div>
    <h1>Services</h1>
    <p class="lede">From a single planning application to a full service, feasibility to completion. Fixed fees, agreed in writing before each stage.</p>
  </div>
</div>


<section>
  <div class="wrap">
{svc('planning','01 &#183; Consents','Planning Applications',
  ["Householder, full, listed building and advertisement consents, prepared and submitted on your behalf. We read the local plan and the officers' recent decisions before we draw a line. "],
  ['Pre-application advice and strategy','Householder and full applications','Discharge of conditions and amendments','Appeals, where a refusal is wrong'],
  'blog/how-much-does-an-architect-cost-uk-2026.html')}
{svc('bim','02 &#183; Technical design','Building Information Modelling (BIM)',
  ['Every project is modelled in 3D, not drawn flat. A coordinated BIM model finds clashes between structure, drainage and services before they reach site.'],
  ['Fully coordinated 3D models','Clash detection before tender','Accurate quantities and schedules','Visualisations you can walk through'],
  'blog.html')}
{svc('site-analysis','03 &#183; Due diligence','Site Analysis',
  ['Before design begins we establish what the site will actually allow: orientation and daylight, overlooking and privacy, tree protection orders, flood risk, rights of light, boundary positions and ground conditions.'],
  ['Constraints and opportunities report','Daylight and overshadowing checks','TPO, flood and heritage screening','Measured surveys arranged and reviewed'],
  'blog.html')}
{svc('feasibility','04 &#183; Before you commit','Feasibility Studies',
  ['A short, fixed-fee study that answers the three questions every project starts with: what can be built, will it get planning, and roughly what will it cost.'],
  ['Drawn options appraisal','Planning risk assessment','Build cost banding','Pre-purchase feasibility for buyers'],
  'blog.html')}
{svc('listed','05 &#183; Heritage','Listed Buildings',
  ["Listed building consent is a different discipline from ordinary planning: the test is harm to significance, and the officer's judgement is shaped by the quality of the heritage statement in front of them."],
  ['Listed building consent applications','Heritage statements and impact assessments','Schedules of works and repairs','Negotiation with conservation officers'],
  'blog.html')}
{svc('conservation','06 &#183; Heritage','Conservation Areas',
  [
   'In a conservation area, what you build has to respond to what is already there. We evidence that with precedent and townscape analysis, so an application reads as considered rather than intrusive.'],
  ['Article 4 and PD rights checks','Design in context, evidenced by precedent','Conservation area consent','Street-scene and townscape drawings'],
  'blog.html')}
{svc('masterplanning','07 &#183; Strategic scale','Masterplanning &amp; Urban Design',
  ['The scale above a building: how a site is divided, where movement runs, what density it genuinely supports, and how the space between the buildings works. Led by Aun Naeem, whose experience spans sites of every scale and programme.'],
  ['Site capacity and development frameworks','Density, massing and typology testing','Movement, access and public realm strategy','Design codes and character guidance','Outline applications and phasing strategy'],
  'blog.html')}
{svc('principal-designer','08 &#183; Duty holder','Principal Designer',
  ['Under CDM 2015 and the Building Safety Act 2022, most projects require a Principal Designer, a legal duty-holder responsible for planning, managing and monitoring design-phase safety and, for higher-risk buildings, compliance with building regulations.'],
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
        <div class="a">Not always. Many extensions and loft conversions fall under permitted development. Assessing this is one of the first things we do, and it's covered in the free consultation. Where an application is needed, we prepare and submit it for you. <a class="link" href="blog/how-much-does-an-architect-cost-uk-2026.html">Read the full guide.</a></div>
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
<div class="page-hero about-hero">
  <div class="wrap">
    <h1>About</h1>
    <p class="lede">A design-led practice working across residential, commercial and heritage projects.</p>
  </div>
</div>

<section class="about-intro">
  <div class="wrap">
    <div class="about-statement">
      <p>FADP was founded on a straightforward premise: the difference between a good project and a difficult one is rarely the design. It is certainty &#8212; about cost, about programme, about who is responsible for what.</p>
      <p>We work in a small number of projects at a time. Each is led by a director from first brief to final inspection, which means the person who understands your project is the person doing the work.</p>
    </div>
  </div>
</section>

<section class="values">
  <div class="wrap">
    <div class="sec-label"><span>How we work</span></div>
    <div class="values-grid">
      <div class="value">
        <h3>Simplicity, without compromise</h3>
        <p>Restraint is a discipline, not a shortcut. We resolve a project until nothing is left that does not need to be there.</p>
      </div>
      <div class="value">
        <h3>Time, used well</h3>
        <p>An efficient design process is not a rushed one. It is one where decisions are made in the right order, so work is not repeated.</p>
      </div>
      <div class="value">
        <h3>Clear communication</h3>
        <p>You are updated at every stage, in plain language. No jargon, no silence, no wondering where a project stands.</p>
      </div>
      <div class="value">
        <h3>The client first</h3>
        <p>Every decision is tested against the brief and the budget, not against what would photograph well.</p>
      </div>
      <div class="value">
        <h3>Consistency</h3>
        <p>The same standard on a rear extension as on a mixed-use scheme. Fees fixed in writing, stages defined, nothing dropped.</p>
      </div>
      <div class="value">
        <h3>Continuous improvement</h3>
        <p>Every project teaches the practice something. We build that back into how the next one is run.</p>
      </div>
    </div>
  </div>
</section>

<section id="team" class="about-team">
  <div class="wrap">
    <div class="sec-label"><span>Directors</span></div>
    <div class="team-grid two">
      <div class="member">
        <img src="{IMG['team1']}" alt="Aun Naeem, Director" loading="lazy">
        <h3>Aun Naeem</h3>
        <div class="m-role">Director</div>
        <p class="m-bio">Leads design and masterplanning. Educated at Birmingham School of Architecture and the University of Sheffield (MArch). Experience spans cultural, educational and retrofit work, alongside international research and design projects.</p>
      </div>
      <div class="member">
        <img src="{IMG['team2']}" alt="Fatima Shakeel, Director" loading="lazy">
        <h3>Fatima Shakeel</h3>
        <div class="m-role">Director</div>
        <p class="m-bio">Leads planning strategy and technical delivery. Educated at Birmingham School of Architecture. Experience covers cultural, religious, commercial and residential schemes, alongside international research and design projects.</p>
      </div>
    </div>
  </div>
</section>

<section class="about-trust">
  <div class="wrap">
    <div class="trust-line">
      <span>Professional indemnity insurance</span>
      <span>Fixed fees, agreed in writing</span>
      <span>Director-led throughout</span>
    </div>
  </div>
</section>
"""

about = head('About &#183; FADP Architecture',
             'FADP is an independent London architecture practice founded in 2014. Meet the team and see how we work.') \
      + header('about') + about_body + cta_band() + '\n' + footer()



# ---------------------------------------------------------------- CONTACT
contact_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Contact</div>
    <h1>Contact</h1>
    <p class="lede">For enquiries, project proposals, press or careers.</p>
  </div>
</div>

<section class="contact-main">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-block">
        <div class="ci-label">Studio</div>
        <address>
          66 Paul Street<br>
          London EC2A 4NA
        </address>
        <p class="contact-note">Studio visits by appointment. Please email first.</p>
      </div>
      <div class="contact-block">
        <div class="ci-label">Enquiries</div>
        <a class="contact-mail" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
        <p class="contact-note">A director will respond within one working day.</p>
      </div>
      <div class="contact-block">
        <div class="ci-label">Fee proposals</div>
        <p class="contact-note">For a written quote, use the enquiry form.</p>
        <a class="link" href="index.html#quote">Start an enquiry &#8594;</a>
      </div>
      <div class="contact-block">
        <div class="ci-label">Press &amp; media</div>
        <a class="contact-mail" href="mailto:design@fadp.co.uk?subject=Press%20enquiry">design@fadp.co.uk</a>
        <p class="contact-note">Please put &lsquo;Press&rsquo; in the subject line.</p>
      </div>
      <div class="contact-block">
        <div class="ci-label">Careers</div>
        <p class="contact-note">Current openings and how to apply.</p>
        <a class="link" href="careers.html">See open roles &#8594;</a>
      </div>
      <div class="contact-block">
        <div class="ci-label">Follow</div>
        <p class="contact-note"><a class="link" href="https://www.instagram.com/fadpworks/" target="_blank" rel="noopener">@fadpworks on Instagram</a></p>
      </div>
    </div>
  </div>
</section>

<section class="contact-map">
  <div class="wrap">
    <div class="map-embed">
      <iframe
        src="https://www.openstreetmap.org/export/embed.html?bbox=-0.0870%2C51.5225%2C-0.0790%2C51.5265&amp;layer=mapnik&amp;marker=51.5245%2C-0.0830"
        title="66 Paul Street, London EC2A 4NA"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="map-caption">66 Paul Street, London EC2A 4NA &#183; <a class="link" href="https://www.openstreetmap.org/?mlat=51.5245&amp;mlon=-0.0830#map=17/51.5245/-0.0830" target="_blank" rel="noopener">View larger map</a></p>
  </div>
</section>
"""
contact = head('Contact &#183; FADP Architecture',
               'Contact FADP Architecture in London. Studio at 66 Paul Street EC2A 4NA. Enquiries, press and careers.') \
        + header('contact') + contact_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- CAREERS
ROLES = [
 ("Building Control Consultant", "Full time or consultancy",
  "Approved Inspector or local authority background. You would keep our projects compliant from first sketch to sign-off, and hold our building control relationships."),
 ("RICS Qualified Surveyor", "Full time or consultancy",
  "MRICS or FRICS, leading surveys, condition reports and party wall matters. Reports written to withstand scrutiny."),
 ("Structural Engineer", "Full time or consultancy",
  "Chartered or close to it. Calculations, steel and foundations for existing building stock, engaged early rather than after the design is fixed."),
 ("Interior Designer", "Full time",
  "Concepts through to joinery details. Equally comfortable setting a material palette and detailing it for construction."),
 ("Architectural Assistant", "Part 1 or Part 2",
  "Project work from the first week, working directly with a director. We support logbooks and the route to qualification."),
]

def role_row(t, kind, body):
    return f"""      <div class="role">
        <div class="role-head">
          <h3>{t}</h3>
          <span class="role-type">{kind}</span>
        </div>
        <p>{body}</p>
      </div>"""

careers_body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; Careers</div>
    <h1>Build the practice with us.</h1>
    <p class="lede">We are recruiting across disciplines to bring expertise in house.</p>
  </div>
</div>

<section class="roles-wrap">
  <div class="wrap">
    <div class="roles">
{chr(10).join(role_row(*r) for r in ROLES)}
    </div>
    <div class="careers-foot">
      <p>Send a CV and something you have made to <a class="link" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>. </p>
      <p class="careers-eo">We are an equal opportunities employer and will make reasonable adjustments at any stage &#8212; just tell us what you need. Applicants must have the right to work in the UK.</p>
    </div>
  </div>
</section>
"""
careers = head('Careers &#183; FADP Architecture',
               'Open roles at FADP Architecture in London: building control, surveying, structural engineering, interior design and architectural assistants.') \
        + header('careers') + careers_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- BLOG INDEX
blog_body = f"""
<div class="news-head">
  <div class="wrap">
    <div class="nh-row">
      <h1>Blog</h1>
      <span class="nh-count"><span id="artCount">2</span> published &#183; <span>1</span> coming soon</span>
    </div>
  </div>
</div>

<div class="news-filters">
  <div class="wrap">
    <div class="nf-row">
        <button class="filter-pill active" data-filter="All">All</button>
        <button class="filter-pill" data-filter="Practice">Practice</button>
        <button class="filter-pill" data-filter="Before you buy">Before you buy</button>
        <button class="filter-pill" data-filter="Planning">Planning</button>
        <button class="filter-pill" data-filter="Heritage">Heritage</button>
    </div>
  </div>
</div>

<section class="news-list-wrap">
  <div class="wrap">
    <div class="news-list">
      <article class="news-row" data-cat="Before you buy">
        <a class="nr-img" href="blog/how-much-does-an-architect-cost-uk-2026.html"><img src="assets/img/blog-hero-house.jpg" alt="" loading="lazy"></a>
        <div class="nr-body">
          <a class="nr-title" href="blog/how-much-does-an-architect-cost-uk-2026.html"><h3>How much does an architect cost in the United Kingdom in 2026?</h3></a>
          <div class="nr-meta">Before you buy &#183; 9 min read</div>
          <p>How fees are structured, what a fee typically includes, how the RIBA Plan of Work relates to the design process, and what other costs to budget for.</p>
          <a class="pill-btn" href="blog/how-much-does-an-architect-cost-uk-2026.html">Read article</a>
        </div>
      </article>
      <article class="news-row" data-cat="Practice">
        <a class="nr-img" href="blog/what-does-an-architecture-studio-do.html"><img src="assets/img/blog-hero-directors.jpg" alt="" loading="lazy"></a>
        <div class="nr-body">
          <a class="nr-title" href="blog/what-does-an-architecture-studio-do.html"><h3>What does an architecture studio actually do?</h3></a>
          <div class="nr-meta">Practice &#183; 8 min read</div>
          <p>A plain-English guide to the whole process, from first conversation to completion on site. Written for anyone considering a project and wondering where architecture actually fits in.</p>
          <a class="pill-btn" href="blog/what-does-an-architecture-studio-do.html">Read article</a>
        </div>
      </article>
      <article class="news-row soon" data-cat="Heritage">
        <a class="nr-img" href="blog/listed-building-consent.html"><span class="soon-tag">Coming soon</span></a>
        <div class="nr-body">
          <a class="nr-title" href="blog/listed-building-consent.html"><h3>Listed building consent, explained</h3></a>
          <div class="nr-meta">Heritage &#183; Coming soon</div>
          <p>A separate regime with its own tests and, unusually in planning law, criminal liability. How consent is won.</p>
          <a class="pill-btn ghost" href="blog/listed-building-consent.html">Notify me</a>
        </div>
      </article>
      </div>
    <p class="news-empty" hidden>No articles in that category yet.</p>
  </div>
</section>
"""
blog = head('Blog &#183; FADP Architecture',
            'Plain-English guides to planning permission, listed buildings, BIM and building regulations from FADP Architecture.') \
     + header('blog') + blog_body + cta_band() + '\n' + footer()

# ---------------------------------------------------------------- write
import os
os.makedirs('blog', exist_ok=True)
open('index.html','w').write(home)
open('projects.html','w').write(projects)
open('services.html','w').write(services)
open('about.html','w').write(about)
open('contact.html','w').write(contact)
open('careers.html','w').write(careers)
open('blog.html','w').write(blog)
for f in ['index.html','projects.html','services.html','about.html','blog.html']:
    print(f, os.path.getsize(f)//1024, 'KB')
