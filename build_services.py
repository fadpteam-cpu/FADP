# Deep service landing page generator. Run after build_pages.py.
# Each hub is 1,500-2,000 words, structured for search intent and E-E-A-T signals.
import os, sys
sys.path.insert(0, '.')
exec(open('build_pages.py').read().split("# ---------------------------------------------------------------- write")[0])

try:
    import servicemap as _smap
except Exception:
    _smap = None


def _crumbs(title):
    return (f'<a href="../index.html">Home</a> &#183; '
            f'<a href="../services.html">Services</a> &#183; {title}')


def _sub_services_grid(slug):
    """List of the sub-services parented to this hub, as a card grid."""
    if not _smap:
        return ''
    subs = [s for s, parent in _smap.PARENT.items() if parent == slug]
    if not subs:
        return ''
    cards = '\n'.join(
        f'''      <a class="sub-svc-card" href="{sub}.html">
        <h4>{_smap.TITLES.get(sub, sub)}</h4>
        <span class="sub-svc-go">View service &#8594;</span>
      </a>'''
        for sub in subs
    )
    return f'''
<section class="sub-services-section">
  <div class="wrap">
    <div class="sec-label"><span>Related services</span></div>
    <p class="sub-services-lede">Every project below is offered as a fixed-fee appointment, staged, with a director leading the work.</p>
    <div class="sub-svc-grid">
{cards}
    </div>
  </div>
</section>'''


def _related_hubs(current_slug):
    """Cross-links to the OTHER hubs at the bottom of each hub."""
    hubs = [
        ('planning-applications', 'Planning applications'),
        ('feasibility-studies', 'Feasibility studies'),
        ('site-analysis', 'Site analysis'),
        ('bim', 'Building Information Modelling'),
        ('masterplanning-urban-design', 'Masterplanning &amp; urban design'),
        ('listed-buildings', 'Listed buildings'),
        ('conservation-areas', 'Conservation areas'),
        ('principal-designer', 'Principal Designer'),
    ]
    others = [(s, t) for s, t in hubs if s != current_slug]
    cards = '\n'.join(
        f'      <a class="hub-card" href="{s}.html"><span>{t}</span><span class="hub-go">&#8594;</span></a>'
        for s, t in others
    )
    return f'''
<section class="related-hubs">
  <div class="wrap">
    <div class="sec-label"><span>Other services</span></div>
    <div class="hub-grid">
{cards}
    </div>
  </div>
</section>'''


def _service_schema(slug, title, description):
    """Structured data — Service schema for SEO rich results."""
    return f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{title}",
  "name": "{title} — FADP Architecture",
  "description": "{description}",
  "provider": {{
    "@type": "ProfessionalService",
    "name": "FADP Architecture",
    "legalName": "Fa Design Partners Limited",
    "url": "https://fadpteam-cpu.github.io/FADP/",
    "email": "design@fadp.co.uk",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "66 Paul Street",
      "addressLocality": "London",
      "postalCode": "EC2A 4NA",
      "addressCountry": "GB"
    }}
  }},
  "areaServed": {{
    "@type": "Country",
    "name": "United Kingdom"
  }},
  "url": "https://fadpteam-cpu.github.io/FADP/services/{slug}.html"
}}</script>'''


def _faq_schema(faqs):
    """FAQPage schema — rewarded with rich results in Google."""
    entities = ',\n    '.join(
        f'''{{
      "@type": "Question",
      "name": "{q.replace('"', chr(92) + chr(34))}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a.replace('"', chr(92) + chr(34))}"
      }}
    }}''' for q, a in faqs
    )
    return f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {entities}
  ]
}}</script>'''


def deep_service_page(slug, title, meta_desc, strap, intro_lead, sections, deliverables,
                 process, standards, faqs, closing):
    """Render a deep service landing page.

    slug          — url slug
    title         — page H1
    meta_desc     — <meta description> (155 chars max ideal)
    strap         — lede sentence under H1
    intro_lead    — 2-3 paragraph intro that answers 'what is this'
    sections      — list of dicts: {h2, body}. body is a list of paragraphs (strings).
    deliverables  — list of strings, what we actually produce
    process       — list of (stage_name, description) tuples
    standards     — dict {intro:str, items:list of (label, body) tuples}
    faqs          — list of (question, answer) tuples, 6-8 items
    closing       — closing paragraph before the CTA
    """

    # Build section blocks
    section_html = ''
    for s in sections:
        paras = '\n'.join(f'        <p>{p}</p>' for p in s['body'])
        section_html += f'''
      <section class="svc-section">
        <h2>{s['h2']}</h2>
{paras}
      </section>'''

    # Deliverables
    deliv_html = '\n'.join(f'          <li>{d}</li>' for d in deliverables)

    # Process
    proc_html = '\n'.join(
        f'''        <div class="svc-step">
          <div class="svc-step-num">0{i+1}</div>
          <div class="svc-step-body">
            <h3>{name}</h3>
            <p>{desc}</p>
          </div>
        </div>''' for i, (name, desc) in enumerate(process)
    )

    # Standards
    stds_items = '\n'.join(
        f'''          <div class="std-item">
            <div class="std-label">{lbl}</div>
            <p>{body}</p>
          </div>''' for lbl, body in standards.get('items', [])
    )

    # FAQs
    faq_html = '\n'.join(
        f'''        <details{" open" if i == 0 else ""}>
          <summary>{q} <span class="m">+</span></summary>
          <div class="a"><p>{a}</p></div>
        </details>''' for i, (q, a) in enumerate(faqs)
    )

    body = f'''
<div class="page-hero svc-hero">
  <div class="wrap">
    <div class="crumbs">{_crumbs(title)}</div>
    <h1>{title}</h1>
    <p class="lede">{strap}</p>
  </div>
</div>

<section class="svc-body">
  <div class="wrap">
    <div class="svc-deep-layout">

      <article class="svc-deep-main">

        <div class="svc-lead">
{chr(10).join(f'          <p>{p}</p>' for p in intro_lead)}
        </div>
{section_html}

        <section class="svc-section">
          <h2>What we deliver</h2>
          <ul class="svc-deliverables">
{deliv_html}
          </ul>
        </section>

        <section class="svc-section">
          <h2>How the process runs</h2>
          <div class="svc-process">
{proc_html}
          </div>
        </section>

        <section class="svc-section">
          <h2>Standards and regulations that apply</h2>
          <p class="svc-std-intro">{standards.get('intro', '')}</p>
          <div class="svc-standards">
{stds_items}
          </div>
        </section>

        <section class="svc-section svc-faqs" id="faqs">
          <h2>Common questions</h2>
          <div class="faq svc-faq-deep">
{faq_html}
          </div>
        </section>

        <section class="svc-closing">
          <p>{closing}</p>
          <div class="svc-closing-actions">
            <a class="btn" href="../index.html#quote">Get in touch</a>
            <a class="link" href="../projects.html">See our projects</a>
          </div>
        </section>

      </article>

      <aside class="svc-deep-aside">
        <div class="aside-card sticky">
          <div class="aside-kicker">Enquiries</div>
          <p class="aside-lead">First consultation is free. A director takes every enquiry.</p>
          <a class="btn full" href="../index.html#quote">Get in touch</a>
          <div class="aside-sep"></div>
          <div class="aside-contact-block">
            <div class="aside-cb-label">Direct to the studio</div>
            <a class="aside-email" href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
          </div>
          <div class="aside-sep"></div>
          <div class="aside-cb-label">Related pages</div>
          <ul class="aside-links-list">
            <li><a href="../journey.html">Your project, stage by stage</a></li>
            <li><a href="../about.html">About the practice</a></li>
            <li><a href="../projects.html">Selected projects</a></li>
          </ul>
        </div>
      </aside>

    </div>
  </div>
</section>
{_sub_services_grid(slug)}
{_related_hubs(slug)}
'''

    # Head extras (schema)
    head_extras = _service_schema(slug, title, meta_desc) + '\n' + _faq_schema(faqs)

    # Custom head with meta description
    head_html = head(f'{title} &#183; FADP Architecture', meta_desc, depth=1)
    # Inject schema before </head>
    head_html = head_html.replace('</head>', head_extras + '\n</head>')

    return (head_html
            + header('services', depth=1)
            + body
            + cta_band(depth=1) + '\n'
            + footer(depth=1))


# =========================================================
# DRIVER — generate all 8 hub pages
# =========================================================
if __name__ == '__main__':
    from service_content import HUBS
    os.makedirs('services', exist_ok=True)
    for hub in HUBS:
        path = f"services/{hub['slug']}.html"
        open(path, 'w').write(deep_service_page(**hub))
        # Also count real words
        rendered = open(path).read()
        import re
        text = re.sub(r'<[^>]+>', ' ', rendered)
        text = re.sub(r'<script[^>]*>.*?</script>', ' ', text, flags=re.DOTALL)
        words = len(text.split())
        print(f"  {path}  {os.path.getsize(path)//1024}KB  ~{words} words rendered")
