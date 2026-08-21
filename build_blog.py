# FADP blog. Run after build_pages.py.
import os
exec(open('build_pages.py').read().split("# ---------------------------------------------------------------- write")[0])


def article_page(slug, title, kicker, mins, img, img_alt, body_html, cta_h, cta_p, cta_param=None):
    quote_href = f"../index.html?project={cta_param}#quote" if cta_param else "../index.html#quote"
    body = f'''
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> &#183; <a href="../blog.html">Blog</a> &#183; {kicker}</div>
  </div>
</div>

<section style="padding-top:32px;">
  <div class="wrap">
    <article class="article">
      <h1>{title}</h1>
      <div class="a-meta">{kicker} &#183; {mins} min read &#183; Published August 2026</div>
      <figure class="a-lead"><img src="{img}" alt="{img_alt}" loading="lazy"></figure>
{body_html}
      <div class="a-cta">
        <h3>{cta_h}</h3>
        <p>{cta_p}</p>
        <a class="btn" href="{quote_href}">Get in touch</a>
      </div>
    </article>
  </div>
</section>
'''
    return (head(f'{title} &#183; FADP Architecture', title, depth=1)
            + header('blog', depth=1) + body + cta_band(depth=1) + '\n' + footer(depth=1))


def coming_soon_page(slug, title, kicker):
    body = f'''
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> &#183; <a href="../blog.html">Blog</a> &#183; {kicker}</div>
  </div>
</div>

<section class="soon-wrap">
  <div class="wrap">
    <div class="soon-card">
      <div class="soon-label">Coming soon</div>
      <h1>{title}</h1>
      <p>This article is being prepared. In the meantime, browse the other articles or get in touch about your project.</p>
      <div class="soon-actions">
        <a class="btn" href="../blog.html">Back to the blog</a>
        <a class="link" href="../contact.html">Contact the studio</a>
      </div>
    </div>
  </div>
</section>
'''
    return (head(f'{title} &#183; FADP Architecture', f'{title} — coming soon from FADP Architecture.', depth=1)
            + header('blog', depth=1) + body + cta_band(depth=1) + '\n' + footer(depth=1))


FLAGSHIP = dict(
 slug='what-does-an-architecture-studio-do',
 title='What does an architecture studio actually do?',
 kicker='Practice', mins=8,
 img='../assets/img/blog-hero-directors.jpg',
 img_alt='FADP directors at the drawing table',
 cta_param='',
 body_html='''
      <p class="a-lead-text">Whether you are planning a home extension, renovating a property or developing a commercial space, understanding what an architecture studio actually does helps you make better decisions from the start.</p>

      <p>Most people think architects draw plans. Drawings are part of what we do, but they are one output of a much larger process. A successful project takes careful planning, technical resolution, creative problem-solving, and the confidence to navigate a set of regulations that can feel opaque from the outside.</p>

      <p>At FADP Architecture we believe the role extends well beyond producing drawings. We help clients turn ideas into buildable, well-considered spaces, and we make the journey clear along the way.</p>

      <h2>Architecture is problem-solving</h2>

      <p>Every project starts with a situation. A family has outgrown its home. A business needs a workspace that matches its ambitions. A building has potential, but nobody is sure where to begin.</p>

      <p>Architecture is the discipline that answers those situations. It is the balance between creativity and practicality: a good building looks well made and also improves the way its occupants live and work. It maximises natural light, uses space efficiently, meets the regulations, holds its value, and stays functional over time.</p>

      <p>Every decision influences the next. That is why good architecture begins long before the first drawing.</p>

      <h2>What a studio actually delivers</h2>

      <p>A modern architecture studio manages every stage of a project&rsquo;s development. Beyond drawings, we coordinate the whole design and construction journey, working closely with the client so decisions are informed at every point.</p>

      <p>Our work typically includes initial consultations and feasibility studies; architectural design; planning applications; building regulations and technical drawings; structural coordination; home extensions; loft, garage and basement conversions; renovations and refurbishments; new-build homes; commercial architecture; listed building and conservation guidance; principal designer services; and BIM and masterplanning where appropriate. Each service is a connected part of the same process, turning an initial idea into a completed project.</p>

      <figure class="a-inline"><img src="../assets/img/studio-sketching.jpg" alt="Sketch design in progress"><figcaption>Sketch design in progress</figcaption></figure>

      <h2>Every project begins with a conversation</h2>

      <p>Starting a project can be intimidating. Questions about planning permission, budget, timelines and regulations tend to arrive before any design work does. That is why every project starts with a free consultation.</p>

      <p>The meeting is a conversation. We take the time to understand the goals, discuss the property, listen to concerns and explain the most sensible route. We give an honest first read on planning potential, realistic timescales and likely cost. There is no obligation to proceed. Afterwards, a written summary and a fixed fee for the next stage arrive, so the decision can be made in the client&rsquo;s own time.</p>

      <h2>Your project, step by step</h2>

      <p>The most common frustration in construction is uncertainty. Clients do not know what happens next. We design the process to remove that uncertainty, one clear stage at a time.</p>

      <h3>Stage 1 &mdash; Free consultation</h3>
      <p>We begin by understanding the vision. It is the client&rsquo;s opportunity to describe what they want, share existing drawings or surveys, discuss budget and ask questions. Whether we meet at the studio, on site or by video call, the client leaves with a clear understanding of the options.</p>

      <h3>Stage 2 &mdash; Feasibility and design</h3>
      <p>Ideas become architecture. We assess the opportunities and constraints of the property, then develop a design that balances aesthetics, practicality and planning policy &mdash; considering site constraints, natural light, internal layouts, structural requirements, planning policy, budget and long-term functionality. Every design is tailored to the property and the way the client wants to use it.</p>

      <h3>Stage 3 &mdash; Planning and approvals</h3>
      <p>Planning permission is the stage that homeowners tend to worry about most. Our role is to simplify it. We prepare and submit the application, coordinate the required documentation, communicate with the local authority and monitor progress through the review. We keep the client informed at every step.</p>

      <h3>Stage 4 &mdash; Technical design</h3>
      <p>Planning approval is not the end. Before construction, contractors need detailed technical information setting out exactly how the building is to be built. We prepare comprehensive drawing packages and coordinate with structural engineers and other consultants so the project is ready for site.</p>

      <h3>Stage 5 &mdash; Construction and completion</h3>
      <p>As construction progresses we remain available to answer technical questions and support the project where required. The aim is straightforward: the completed building should reflect the original design intent, and its quality should hold from first drawing to final inspection.</p>

      <h2>The questions we answer every day</h2>

      <p>Architecture arrives with unfamiliar terminology. Clients regularly ask us: do I need planning permission? How far can I extend? What is a party wall? What happens after an application is submitted? How long will it take?</p>

      <p>Rather than answering in code, we explain each stage in plain terms, so the client understands what is happening and why. Informed clients make better decisions.</p>

      <h2>Why good architecture adds value</h2>

      <p>A well-designed project delivers more than additional floor area. It improves how a building functions, increases natural light and comfort, adds property value, makes better use of underused space, improves energy performance, supports future changes of use, and creates places that are enjoyable to occupy. Good architecture is not about making buildings larger. It is about making them better.</p>

      <h2>Why FADP</h2>

      <p>Every practice has an approach. Ours is built around clarity, collaboration and trust. Working with FADP means a free, no-obligation initial consultation; fixed-fee quotations; honest advice from the outset; direct communication throughout; clear explanations without unnecessary jargon; and support from concept through planning, technical design and construction.</p>

      <p>Projects are significant investments. Clients deserve transparency at every stage.</p>

      <h2>Looking ahead</h2>

      <p>Every successful project begins with a conversation. Whether the brief is an extension, a loft conversion, a renovation, a commercial development or a new building, involving an architectural designer early uncovers opportunities, resolves problems before they arise, and creates a smoother path from concept to completion.</p>

      <p>Our role is not simply to draw. It is to guide clients through every stage with confidence, clarity and expertise.</p>
''',
 cta_h='Ready to talk about your project?',
 cta_p='Book a free consultation and see how we can help. A director takes every first meeting.',
)

FLAGSHIP2 = dict(
 slug='how-much-does-an-architect-cost-uk-2026',
 title='How much does an architect cost in the United Kingdom in 2026?',
 kicker='Before you buy', mins=9,
 img='../assets/img/blog-hero-house.jpg',
 img_alt='Modern residential house exterior at dusk',
 cta_param='',
 body_html='''
      <p class="a-lead-text">Planning an extension, renovation, loft conversion or new home? Understanding architectural fees is one of the first steps towards setting a realistic budget.</p>

      <p>One of the first questions homeowners ask is: how much does an architect cost in the United Kingdom? The honest answer is that there is no single figure. Fees vary with the size and complexity of the project, the existing property, planning requirements, the level of design required, and how far you want the practice to take the work.</p>

      <p>At FADP, we believe architectural fees should be clear, proportionate, and related to what your project actually needs. This guide sets out how fees are calculated, what they typically include, how the RIBA Plan of Work relates to the design process, and what other costs to budget for.</p>

      <h2>How fees are structured</h2>

      <p>There is no universal fee that applies to every residential project. The Architects Registration Board confirms there is no standard tariff, because costs vary from project to project.</p>

      <p>Architectural fees may be structured as fixed or lump-sum fees, percentage-based fees, time-based fees, stage-by-stage fees, or a combination. The right structure depends on the project and the scope of services required.</p>

      <p>Factors that influence the fee include project size, project complexity, existing building condition, planning constraints, level of design development, technical requirements, number of project stages, and consultant coordination.</p>

      <p>For example, one client may appoint us for feasibility and planning only. Another may want the whole appointment through technical design, tender information, and construction-stage services. These are substantially different pieces of work.</p>

      <p>When comparing fees, do not look at the headline figure alone. Consider how the fee is calculated, what additional costs may arise, and what work is included within the appointment. The right question is not <em>how much</em> but <em>what exactly am I getting for the fee?</em></p>

      <h2>What a fee typically includes</h2>

      <p>Depending on the project and the agreed scope, architectural services can include: initial consultation, preparation and briefing, feasibility studies, existing building assessment, concept design, planning drawings, planning applications, design development, spatial coordination, Building Regulations information, technical drawings, consultant coordination, tender information, and construction-stage services.</p>

      <p>Not every project needs every stage. The scope should be agreed before work begins, so you understand which stages are included, what will be delivered, and what may fall outside as additional work.</p>

      <h2>The RIBA Plan of Work</h2>

      <p>The RIBA Plan of Work is the recognised industry framework for organising the briefing, design, construction, and use of a building. The full plan is organised into eight stages, from Stage 0 to Stage 7. FADP&rsquo;s services can be structured around the stages most relevant to your project, with particular focus on Stages 1&ndash;4.</p>

      <h3>Stage 1 &mdash; Preparation and briefing</h3>
      <p>The project is defined in greater detail. This can involve understanding the property, establishing the brief, identifying site information, considering feasibility, establishing budget parameters, considering programme, and identifying planning constraints. The objective is to know what the project needs to achieve before the design develops further.</p>

      <h3>Stage 2 &mdash; Concept design</h3>
      <p>The brief becomes an architectural concept. The design can explore floor plans, massing, form, natural light, circulation, materials, spatial relationships, and initial structural considerations. The objective is to establish the overall design approach in response to the brief.</p>

      <h3>Stage 3 &mdash; Spatial coordination</h3>
      <p>The concept develops into a more coordinated proposal. Plans, sections, and elevations are developed alongside relevant engineering and specialist information. Planning requirements are addressed at this stage. Under the RIBA framework, planning applications are typically submitted towards the end of Stage 3.</p>

      <p>An important distinction: planning approval is not the end of design. It is one part of the wider process.</p>

      <h3>Stage 4 &mdash; Technical design</h3>
      <p>The project moves from &ldquo;what should we design?&rdquo; to &ldquo;how will it be built?&rdquo; Technical design may include construction drawings, construction details, specifications, building systems, structural coordination, Building Regulations information, and specialist consultant information. RIBA identifies Stage 4 as the stage in which the design information required to manufacture and construct the project is completed.</p>

      <p>This is why a planning-only service is very different from a full design and technical appointment.</p>

      <h2>What other costs should you budget for?</h2>

      <p>Your architectural fee is only part of the overall project budget. Depending on the project, you may also need to allow for:</p>

      <p><strong>Planning fees.</strong> Statutory fees paid to the local planning authority.</p>

      <p><strong>Building Control.</strong> Separate fees associated with Building Regulations approval.</p>

      <p><strong>Structural engineering.</strong> Often required for extensions, structural alterations, and new structural elements.</p>

      <p><strong>Surveys.</strong> Depending on the property and scope, this may include measured building surveys, topographical surveys, structural surveys, drainage surveys, and specialist surveys.</p>

      <p><strong>Party Wall services.</strong> Where the Party Wall etc. Act 1996 applies, you may need to appoint a Party Wall surveyor.</p>

      <p><strong>Specialist consultants.</strong> Depending on the project, additional specialist advice or reports may be required.</p>

      <p><strong>Construction and contingency.</strong> The construction cost itself will form the largest part of the overall budget, alongside a sensible contingency for unforeseen costs.</p>

      <p>These are not automatically included within an architectural fee. Your appointment should clearly identify what is included, what is excluded, and which costs are payable separately.</p>

      <h2>How FADP approaches fees</h2>

      <p>We begin by understanding the project before proposing an appropriate scope of services. Five things shape the fee.</p>

      <p><strong>Your property.</strong> What exists today? Understanding the existing building, site conditions, and constraints provides the foundation for design.</p>

      <p><strong>Your brief.</strong> What do you want to achieve? We establish your requirements, priorities, and aspirations.</p>

      <p><strong>Your budget.</strong> What level of investment is realistic? Understanding the available budget helps shape the scope.</p>

      <p><strong>Your planning context.</strong> What constraints and opportunities affect the property? Planning considerations have a significant influence on what may be achievable.</p>

      <p><strong>Your ambitions.</strong> What should the finished project achieve? The design should respond not only to the practical brief but to the character and long-term objectives of the project.</p>

      <p>We then propose a scope and a clear fee. Depending on the project, this may run: preparation and briefing &rarr; concept design &rarr; spatial coordination &rarr; technical design &rarr; construction. The exact scope is tailored to the requirements of the individual project.</p>

      <h2>What to ask before appointing anyone</h2>

      <p>Before you commit, ask the following.</p>

      <p><strong>What stages are included?</strong> Understand whether the appointment covers feasibility, design, planning, technical design, and/or construction.</p>

      <p><strong>What will I receive?</strong> Ask what drawings, documents, and deliverables are included.</p>

      <p><strong>What is excluded?</strong> Understand whether surveys, structural engineering, planning fees, Building Control, and other consultants are separate.</p>

      <p><strong>How are changes handled?</strong> Ask what happens if the brief changes or extra work becomes necessary.</p>

      <p><strong>Who will manage the project?</strong> Understand who your main point of contact will be and who will coordinate the design team.</p>

      <p><strong>How is the fee calculated?</strong> Establish whether the fee is fixed, percentage-based, time-based, or by stage.</p>

      <p><strong>Will it be in writing?</strong> Terms of engagement should clearly set out the work to be done, the fee or method of calculation, responsibilities, and any limitations. ARB recommends clients understand the contract, fees, scope, and potential additional costs before work begins.</p>

      <h2>The right service depends on your project</h2>

      <p>There is no single service that is right for every homeowner. A straightforward planning application may require a different level of involvement from a complex extension, whole-house refurbishment, or new build. The important thing is to understand what you need, what each stage achieves, what your fee covers, and what other costs to allow for.</p>

      <p>The RIBA Plan of Work provides a useful framework for the progression of a project. The actual scope of services should be tailored to what your project needs.</p>

      <h2>Common questions</h2>

      <h3>How much does an architect cost in the United Kingdom?</h3>
      <p>There is no single standard fee. Fees depend on the project&rsquo;s size, complexity, scope, and stages of service. They may be fixed, percentage-based, time-based, or by stage. ARB confirms there is no standard tariff.</p>

      <h3>What is included in a fee?</h3>
      <p>This depends on the agreed scope. Services can range from preparation and feasibility through concept, planning, spatial coordination, and technical design. Always check which stages, drawings, and deliverables are included in your fee proposal.</p>

      <h3>Do fees include planning permission?</h3>
      <p>Not necessarily. The practice may prepare and submit a planning application, but the statutory application fee is a separate cost.</p>

      <h3>Do fees include Building Regulations?</h3>
      <p>It depends on the appointment. Where technical design forms part of the service, we may prepare Building Regulations information and coordinate relevant technical requirements. Confirm in the fee proposal.</p>

      <h3>What are the four RIBA stages FADP works through?</h3>
      <p>For the services described in this guide, FADP focuses on RIBA Stages 1&ndash;4: preparation and briefing (Stage 1), concept design (Stage 2), spatial coordination (Stage 3), and technical design (Stage 4). The full RIBA Plan of Work contains eight stages, from Stage 0 to Stage 7. The four above represent the principal design and technical stages.</p>

      <h3>Do I need an architect for a house extension?</h3>
      <p>Not every project legally requires one. However, professional architectural input helps with design development, planning considerations, spatial coordination, and technical information. The right level of service depends on the project.</p>

      <h3>Do I need a survey for my project?</h3>
      <p>Depending on the property and scope, you may need a measured building, topographical, structural, drainage, or other specialist survey. The right survey should be carried out by a suitably qualified professional.</p>

      <h3>Does planning permission mean I can start building?</h3>
      <p>No. Planning permission and Building Regulations are separate matters. A project may require planning approval as well as compliance with Building Regulations and any other applicable requirements before construction proceeds.</p>

      <h3>Should I hire before speaking to a builder?</h3>
      <p>For many projects, obtaining architectural advice early helps establish the scope, design, planning requirements, and technical needs before construction pricing is sought.</p>
''',
 cta_h='Ready to understand your project?',
 cta_p='Tell us about your property, what you want to change, and what you hope to achieve. A director takes every first meeting.',
)


COMING = [
 dict(slug='listed-building-consent',
      title='Listed building consent, explained', kicker='Heritage'),
]

open(f"blog/{FLAGSHIP['slug']}.html", 'w').write(article_page(**FLAGSHIP))
print(f"blog/{FLAGSHIP['slug']}.html", os.path.getsize(f"blog/{FLAGSHIP['slug']}.html") // 1024, 'KB')

open(f"blog/{FLAGSHIP2['slug']}.html", 'w').write(article_page(**FLAGSHIP2))
print(f"blog/{FLAGSHIP2['slug']}.html", os.path.getsize(f"blog/{FLAGSHIP2['slug']}.html") // 1024, 'KB')

for c in COMING:
    open(f"blog/{c['slug']}.html", 'w').write(coming_soon_page(**c))
    print(f"blog/{c['slug']}.html (coming soon)")

old = 'blog/how-bim-cuts-construction-costs.html'
if os.path.exists(old):
    os.remove(old); print(f"removed {old}")
