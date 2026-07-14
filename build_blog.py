# Harvard-referenced blog articles. Run after build_pages.py.
import os
exec(open('build_pages.py').read().split("# ---------------------------------------------------------------- write")[0])

def article_page(slug, title, kicker, mins, img, img_alt, body_html, refs, cta_h, cta_p, cta_param=None):
    ref_items = '\n'.join(f'        <li>{r}</li>' for r in refs)
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
      <div class="a-meta">{kicker} &#183; {mins} min read &#183; Reviewed July 2026 &#183; Referenced to primary sources</div>
      <figure class="a-lead"><img src="{img}" alt="{img_alt}" loading="lazy"></figure>
{body_html}
      <div class="a-cta">
        <h3>{cta_h}</h3>
        <p>{cta_p}</p>
        <a class="btn" href="{quote_href}">Get a fixed-fee quote</a>
      </div>
      <section class="refs">
        <h2>References</h2>
        <ul>
{ref_items}
        </ul>
      </section>
    </article>
  </div>
</section>
'''
    return (head(f'{title} &#183; FADP Architecture', title, depth=1)
            + header('blog', depth=1) + body + cta_band(depth=1) + '\n' + footer(depth=1))

ARTICLES = []

# ============================================================ 1. REAR EXTENSION (upgraded with references)
ARTICLES.append(dict(
 slug='planning-permission-rear-extension',
 title='Do you need planning permission for a rear extension?',
 kicker='Planning', mins=7, img=IMG['p5'], img_alt='Rear extension, Chelsea', cta_param='Extension',
 body_html='''
      <p>Short answer: often not, thanks to permitted development. But the exceptions catch people out every week, and building without the right consent risks enforcement action for up to ten years after the works are substantially completed (Town and Country Planning Act 1990, s.171B, as amended by the Levelling-up and Regeneration Act 2023). Here is how the rules actually work for a typical London house, with the sources you can check yourself.</p>

      <h2>Permitted development: the legal basis</h2>
      <p>Permitted development (PD) rights come from Schedule 2, Part 1, Class A of the General Permitted Development Order (GPDO 2015). They grant a deemed planning permission for house extensions that stay inside strict limits, so no application is needed. For a single-storey rear extension on a house (not a flat), the headline limits are:</p>
      <ul>
        <li>Up to 3 metres deep on an attached house, or 4 metres on a detached house, measured from the original rear wall (GPDO 2015, Sch. 2, Pt 1, Class A)</li>
        <li>Maximum height of 4 metres, and eaves no higher than 3 metres within 2 metres of a boundary</li>
        <li>No more than half the land around the original house covered by additions</li>
        <li>Materials of similar appearance to the existing house</li>
      </ul>
      <p>Under the larger home extension provisions of the same Class, single-storey rear extensions can reach 6 metres on an attached house and 8 metres on a detached one, but only through the prior approval procedure, in which the council notifies your adjoining neighbours and weighs any objections (GPDO 2015, Sch. 2, Pt 1, Class A.1(g)).</p>

      <div class="a-note">"Original house" means the house as first built, or as it stood on 1 July 1948 (MHCLG, 2019). If a previous owner already extended, some or all of your PD allowance may be used up. This is the single most common mistake we see in practice.</div>

      <h2>When permitted development does not apply</h2>
      <p>PD rights are removed or restricted in several situations common in London:</p>
      <ul>
        <li><strong>Flats and maisonettes</strong> have no householder PD rights at all: Class A applies to dwellinghouses only (GPDO 2015, Sch. 2, Pt 1). Any extension to a flat needs planning permission.</li>
        <li><strong>Article 2(3) land</strong>, which includes conservation areas, restricts side extensions, cladding and other classes, and many London conservation areas carry an additional Article 4 direction removing rear-extension rights street by street (GPDO 2015, art. 4).</li>
        <li><strong>Listed buildings</strong> need listed building consent for almost any alteration affecting their character, inside or out, under a separate regime entirely (Planning (Listed Buildings and Conservation Areas) Act 1990, ss. 7 to 9).</li>
        <li><strong>Previous planning conditions</strong> sometimes remove PD rights from a specific property. This only shows up in a search of the planning history.</li>
      </ul>

      <h2>How to find out for certain</h2>
      <p>Three checks settle the question for any property: the council's planning history for the address, which reveals past extensions and any conditions removing PD rights; the council's policy maps, which show conservation areas and Article 4 directions; and the National Heritage List for listed status (Historic England, 2026).</p>
      <p>Even where PD clearly applies, we recommend applying for a lawful development certificate under s.192 of the 1990 Act. It costs half the fee of a planning application, and it is the document your solicitor, and your buyer's solicitor, will ask for when you sell.</p>

      <h2>If you do need permission</h2>
      <p>A householder application is determined within eight weeks of validation (Town and Country Planning (Development Management Procedure) (England) Order 2015). The quality of the drawings and the planning case decide most outcomes: an application grounded in the local plan and the council's own recent approvals on your street is designed to be approved rather than argued. That is the basis on which we prepare every application we submit.</p>
''',
 refs=[
  "Historic England (2026) <em>The National Heritage List for England</em>. Swindon: Historic England. Available at: https://historicengland.org.uk/listing/the-list/",
  "Levelling-up and Regeneration Act 2023, c. 55. London: The Stationery Office.",
  "Ministry of Housing, Communities and Local Government (2019) <em>Permitted development rights for householders: technical guidance</em>. London: MHCLG.",
  "Planning (Listed Buildings and Conservation Areas) Act 1990, c. 9. London: HMSO.",
  "Town and Country Planning Act 1990, c. 8. London: HMSO.",
  "Town and Country Planning (Development Management Procedure) (England) Order 2015 (SI 2015/595). London: The Stationery Office.",
  "Town and Country Planning (General Permitted Development) (England) Order 2015 (SI 2015/596). London: The Stationery Office.",
 ],
 cta_h='Not sure where your property stands?',
 cta_p='We run the planning-history, Article 4 and listing checks as part of the free consultation, and tell you in writing whether you need an application at all.'))

# ============================================================ 2. LISTED BUILDING CONSENT
ARTICLES.append(dict(
 slug='listed-building-consent',
 title='Listed building consent, explained',
 kicker='Heritage', mins=8, img=IMG['listed'], img_alt='Listed building facade',
 body_html='''
      <p>Around 400,000 buildings in England are listed, and owning one changes the legal ground beneath every alteration you might make. Listed building consent is a separate regime from planning permission, with its own tests, its own paperwork and, unusually in planning law, criminal liability for getting it wrong. This guide explains how the system actually works.</p>

      <h2>The legal framework</h2>
      <p>Listing is made under s.1 of the Planning (Listed Buildings and Conservation Areas) Act 1990, and its consequences flow from s.7: no person may execute works for the demolition, alteration or extension of a listed building in any manner which would affect its character as a building of special architectural or historic interest, unless the works are authorised. Authorisation means listed building consent under s.8. Carrying out unauthorised works is an offence under s.9, and it is a strict one: intent is not required, and ignorance of the listing is no defence.</p>
      <p>Two points surprise most owners. First, listing covers the whole building, interior included, and can extend to curtilage structures such as boundary walls and outbuildings predating 1948 (Historic England, 2018). Second, there is no time limit: enforcement against unauthorised works to a listed building can arrive decades later, and the obligation to reverse them travels with the property to future owners.</p>

      <h2>The test: harm to significance</h2>
      <p>Decisions on consent are governed by s.16(2) of the 1990 Act, which requires the authority to have special regard to the desirability of preserving the building, its setting, and its features of special interest. National policy translates this into the language of significance: the National Planning Policy Framework directs decision-makers to weigh any harm to a heritage asset's significance against the public benefits of the proposal, with great weight given to conservation (MHCLG, 2024, ch. 16).</p>
      <p>Practically, this means the conservation officer's judgement is shaped almost entirely by the heritage statement submitted with the application. Historic England's Advice Note 12 sets out what a proper statement of heritage significance contains: an understanding of what makes the building special, an assessment of how the proposals affect it, and a justification for any harm (Historic England, 2019). A thin statement invites a refusal; a rigorous one often turns the application into a design conversation rather than a contest.</p>

      <div class="a-note">The application itself is free: no fee is payable for listed building consent, unlike planning permission. The real costs are the research, drawings and heritage statement, which is why they should be done once, well.</div>

      <h2>What needs consent, and what does not</h2>
      <p>The trigger is effect on character, not size of works. Replacing a plastic bathroom suite usually does not need consent; removing a wall, replacing windows, stripping plaster or altering a staircase usually does. Like-for-like repair sits in a grey area that depends on materials and extent. The safe route on any listed building is to establish the position in writing with the council's conservation team before works, which is a service we provide at the start of every listed project.</p>

      <h2>How we approach listed applications</h2>
      <p>Our listed building work starts with the significance research, because everything else depends on it: where significance is lowest is where change is easiest to justify. We then design the proposals and write the heritage statement as a single argument, deal with the conservation officer in their own terms, and specify materials and methods appropriate to the building's construction. The statutory determination period is eight weeks, but pre-application engagement usually shortens the whole journey.</p>
''',
 refs=[
  "Historic England (2018) <em>Listed Buildings and Curtilage: Historic England Advice Note 10</em>. Swindon: Historic England.",
  "Historic England (2019) <em>Statements of Heritage Significance: Analysing Significance in Heritage Assets. Historic England Advice Note 12</em>. Swindon: Historic England.",
  "Ministry of Housing, Communities and Local Government (2024) <em>National Planning Policy Framework</em>. London: MHCLG.",
  "Planning (Listed Buildings and Conservation Areas) Act 1990, c. 9. London: HMSO.",
 ],
 cta_h='Planning work to a listed building?',
 cta_p='We prepare the significance research, heritage statement and consent application as one coherent argument, and deal with the conservation officer for you.'))

# ============================================================ 3. PRINCIPAL DESIGNER
ARTICLES.append(dict(
 slug='principal-designer-explained',
 title='What does a Principal Designer actually do?',
 kicker='Regulations', mins=8, img=IMG['studio'], img_alt='Design coordination in the studio',
 body_html='''
      <p>Most homeowners commissioning building work have never heard of the Principal Designer, and yet the law requires one on almost every project, and if nobody is appointed, the legal duties land on the client personally. Since 2023 the role has doubled: there are now two distinct Principal Designer duties under two different pieces of legislation. This guide untangles them.</p>

      <h2>The CDM 2015 role: design-phase safety</h2>
      <p>The Construction (Design and Management) Regulations 2015 apply to all construction work, domestic projects included. Where a project involves, or is likely to involve, more than one contractor, the client must appoint a Principal Designer in writing to plan, manage, monitor and coordinate health and safety in the pre-construction phase (CDM 2015, regs. 5 and 11 to 12). Practically, that means identifying foreseeable risks in the design, designing them out where possible, and passing coherent pre-construction information to the contractors who will price and build the work (HSE, 2015).</p>
      <p>The regulation domestic clients most need to know is regulation 7: on a domestic project, if the client fails to make the appointments, the duties default to others in the project team, and in defined circumstances responsibilities that would otherwise be the client's transfer automatically. Relying on defaults is a poor position to discover you were in after an accident; appointing formally costs a line in a letter.</p>

      <h2>The Building Safety Act role: regulatory compliance</h2>
      <p>The Building Safety Act 2022, enacted after the Grenfell Tower fire and the Hackitt review (Hackitt, 2018), created a second, distinct Principal Designer duty. Through the Building Regulations etc. (Amendment) (England) Regulations 2023, which took effect on 1 October 2023, every project where building regulations apply and more than one designer is involved must have a Principal Designer responsible for planning, managing and monitoring the design work so that, if built as designed, the building would comply with building regulations (SI 2023/911).</p>
      <p>This is not a safety-file formality: it is accountability for regulatory compliance of the design itself, with the Building Safety Regulator able to act against dutyholders who fail. For higher-risk buildings, defined as those at least 18 metres or seven storeys high containing two or more residential units (Building Safety Act 2022, s. 65; SI 2023/275), the regime adds gateway approvals at design and completion stages that the project cannot lawfully pass without.</p>

      <div class="a-note">Same title, two jobs: the CDM 2015 Principal Designer manages design-phase health and safety; the 2023 building regulations Principal Designer manages design compliance with building regulations. On most projects one competent professional holds both appointments, but they must each be made, in writing.</div>

      <h2>What this means on your project</h2>
      <p>For a typical extension or refurbishment with a builder and their subcontractors, the more-than-one-contractor test is met, so a CDM Principal Designer is required, and because building regulations apply and multiple designers contribute, the building regulations Principal Designer duty arises too. On our full appointments we take both roles as standard: risk registers kept, pre-construction information issued, design compliance planned and recorded, and the health and safety file handed to you at completion, which the next owner's solicitor will one day ask to see.</p>
''',
 refs=[
  "Building Safety Act 2022, c. 30. London: The Stationery Office.",
  "Construction (Design and Management) Regulations 2015 (SI 2015/51). London: The Stationery Office.",
  "Hackitt, J. (2018) <em>Building a Safer Future: Independent Review of Building Regulations and Fire Safety, Final Report</em>. Cm 9607. London: The Stationery Office.",
  "Health and Safety Executive (2015) <em>Managing Health and Safety in Construction. Construction (Design and Management) Regulations 2015: Guidance on Regulations, L153</em>. Bootle: HSE.",
  "Higher-Risk Buildings (Descriptions and Supplementary Provisions) Regulations 2023 (SI 2023/275). London: The Stationery Office.",
  "Building Regulations etc. (Amendment) (England) Regulations 2023 (SI 2023/911). London: The Stationery Office.",
 ],
 cta_h='Does your project have its dutyholders in place?',
 cta_p='We take both Principal Designer appointments as standard on full projects, and accept standalone appointments on projects designed by others.'))

# ============================================================ 4. CONSERVATION AREA PD
ARTICLES.append(dict(
 slug='conservation-area-permitted-development',
 title='Permitted development in conservation areas',
 kicker='Heritage', mins=7, img=IMG['p8'], img_alt='Conservation area street, north London',
 body_html='''
      <p>England has over 10,000 conservation areas, and London boroughs alone contain more than a thousand of them. Buying or improving a house in one changes what you can build without permission, sometimes drastically, and the changes are invisible until you check. This guide sets out exactly which permitted development rights survive inside a conservation area, and which do not.</p>

      <h2>What a conservation area is, legally</h2>
      <p>Councils designate conservation areas under s.69 of the Planning (Listed Buildings and Conservation Areas) Act 1990, as areas of special architectural or historic interest whose character or appearance it is desirable to preserve or enhance. Designation triggers the s.72 duty: in exercising planning functions in the area, the authority must pay special attention to preserving or enhancing that character. It is a designation of the area's character, not of individual buildings; your house need not be special for the street to be protected.</p>

      <h2>What changes automatically on designation</h2>
      <p>Conservation areas are "article 2(3) land" under the General Permitted Development Order, and several householder rights are cut back on such land automatically (GPDO 2015, Sch. 2, Pt 1):</p>
      <ul>
        <li>Side extensions are not permitted development at all</li>
        <li>Rear extensions of more than one storey are excluded, and the larger home extension route is unavailable</li>
        <li>Cladding the exterior in stone, render, timber or tiles is excluded</li>
        <li>Roof enlargements such as dormers are excluded, which removes most loft-conversion PD</li>
        <li>Outbuildings to the side of the house are excluded, and chimneys and some other alterations face tighter rules</li>
      </ul>
      <p>Demolition is also controlled: substantial demolition of an unlisted building in a conservation area requires planning permission, an offence-backed control inserted by the Enterprise and Regulatory Reform Act 2013 into s.196D of the Town and Country Planning Act 1990.</p>

      <h2>Article 4 directions: the second cut</h2>
      <p>On top of the automatic restrictions, councils can make Article 4 directions withdrawing further specified PD rights in defined areas (GPDO 2015, art. 4). In London these commonly remove rights for front elevation alterations, windows, front gardens and sometimes single-storey rear extensions, precisely the works the automatic rules still allow. Article 4 directions are mapped street by street; two identical houses one road apart can have different rights. Historic England's guidance encourages councils to pair designation with a character appraisal and management plan identifying what the area's significance actually rests on (Historic England, 2019).</p>

      <div class="a-note">The sequence for any conservation-area project is therefore: confirm designation, check for Article 4 directions at the address, then read the character appraisal. Only after those three do you know what can be built without an application. We run all three checks as part of the free consultation.</div>

      <h2>Getting approval where an application is needed</h2>
      <p>Losing PD rights does not mean losing the project; it means winning it by application. The s.72 test is preserve or enhance, and the strongest evidence that a proposal does so is precedent: what the council has approved nearby, and the reasoning in those decisions. Our conservation-area applications lead with the character appraisal and local precedent, supported by street scene drawings that show the proposal in its context, because that is the evidence the committee report will be written from.</p>
''',
 refs=[
  "Enterprise and Regulatory Reform Act 2013, c. 24. London: The Stationery Office.",
  "Historic England (2019) <em>Conservation Area Appraisal, Designation and Management: Historic England Advice Note 1</em>. 2nd edn. Swindon: Historic England.",
  "Ministry of Housing, Communities and Local Government (2024) <em>National Planning Policy Framework</em>. London: MHCLG.",
  "Planning (Listed Buildings and Conservation Areas) Act 1990, c. 9. London: HMSO.",
  "Town and Country Planning Act 1990, c. 8. London: HMSO.",
  "Town and Country Planning (General Permitted Development) (England) Order 2015 (SI 2015/596). London: The Stationery Office.",
 ],
 cta_h='In a conservation area and planning work?',
 cta_p='We confirm your designation, Article 4 position and realistic options in writing, before you spend anything on design.'))

# ============================================================ 5. BIM CUTS COSTS
ARTICLES.append(dict(
 slug='how-bim-cuts-construction-costs',
 title='How BIM cuts construction costs: the evidence',
 kicker='Technical', mins=7, img=IMG['model'], img_alt='Coordinated building information model',
 body_html='''
      <p>Building Information Modelling is often sold as software and dismissed as jargon. It is neither: it is a working method whose cost effects have been measured, by government, repeatedly, because the UK public sector mandated it on central projects and then commissioned studies to see whether it paid. The evidence says it does, and the mechanisms that produce the savings on a hospital produce them on a house extension too.</p>

      <h2>What BIM actually is</h2>
      <p>BIM means designing in a shared, structured 3D model that holds the building's geometry and information together, so that structure, drainage and services are coordinated in one place rather than on separate flat drawings. The international standard governing the method, ISO 19650, defines it as the use of a shared digital representation of a built asset to facilitate design, construction and operation, and to form a reliable basis for decisions (BSI, 2019). Drawings, schedules and quantities are outputs generated from the model, which is why they agree with each other.</p>

      <h2>The measured evidence</h2>
      <p>When the UK Government mandated BIM Level 2 on centrally procured projects from 2016, the Cabinet Office reported £3 billion of efficiency savings in construction procurement over the 2011 to 2015 parliament, with BIM identified as a key contributor (Cabinet Office, 2016). To test the benefits with more rigour, the Centre for Digital Built Britain commissioned PwC to build and apply a benefits measurement methodology on live public assets. PwC's application report quantified gross benefits equivalent to roughly 1.5% to 3% of whole-life cost on the assets studied, and estimated that comparable adoption across in-scope public construction implied annual savings in the order of £226 million to £429 million, with time savings in design activity of around 5% of design cost among the contributing mechanisms (PwC, 2018).</p>

      <h2>Where the money is saved</h2>
      <p>The savings have identifiable mechanisms, each of which scales down to domestic work:</p>
      <ul>
        <li><strong>Clash detection.</strong> The beam that meets the soil pipe is found in the model during design, where moving it costs nothing, instead of on site, where it becomes an uncompeted variation and a delay.</li>
        <li><strong>Accurate quantities.</strong> Because quantities are measured from the model rather than estimated from drawings, tender prices come back tighter and closer together, and contractors carry less risk pricing, which you would otherwise pay for.</li>
        <li><strong>Consistent information.</strong> Plans, sections and schedules generated from one model cannot contradict each other, which removes the site queries and re-pricing that contradictions cause.</li>
        <li><strong>Fewer variations.</strong> Industry analysis of rework consistently attributes a material share of construction cost overrun to design information problems, which coordinated models exist to remove (Egan, 1998).</li>
      </ul>

      <div class="a-note">On a traditionally drawn project, the contractor discovers the coordination problems, and every discovery is priced without competition. BIM moves that discovery into design time, where resolving it is the designer's job at no extra cost to the client.</div>

      <h2>What this means for your project</h2>
      <p>We model every project in 3D as standard: the survey, the existing building and the proposal. Clients see their project as a walkthrough rather than a plan, decisions get easier, and the tender package that goes to builders is measured, coordinated and consistent. The modelling effort sits inside our fixed design fee, and on the evidence above, it is the part of the fee most likely to pay for itself.</p>
''',
 refs=[
  "British Standards Institution (2019) <em>BS EN ISO 19650-1:2018. Organization and digitization of information about buildings and civil engineering works, including building information modelling: Concepts and principles</em>. London: BSI.",
  "Cabinet Office (2016) <em>Government Construction Strategy 2016-20</em>. London: Cabinet Office.",
  "Egan, J. (1998) <em>Rethinking Construction: The Report of the Construction Task Force</em>. London: Department of the Environment, Transport and the Regions.",
  "PwC (2018) <em>BIM Level 2 Benefits Measurement: Application of PwC's BIM Level 2 Benefits Measurement Methodology to Public Sector Capital Assets</em>. Cambridge: Centre for Digital Built Britain.",
 ],
 cta_h='Want a project priced from a coordinated model?',
 cta_p='Every FADP project is modelled in 3D as standard, inside the fixed design fee. Tell us about yours and we will quote it in writing.'))

# ============================================================ 6. FEASIBILITY BEFORE YOU BUY
ARTICLES.append(dict(
 slug='feasibility-studies-before-you-buy',
 title='Feasibility studies: what you learn before you spend',
 kicker='Before you buy', mins=6, img=IMG['p7'], img_alt='Feasibility options on the drawing board',
 body_html='''
      <p>The most expensive drawings in architecture are the ones produced for a project that was never possible: the loft without head height, the extension the council was never going to allow, the budget that was fiction from the first meeting. A feasibility study exists to spend a small, fixed amount answering the three questions everything else depends on, before anything else is spent.</p>

      <h2>The three questions</h2>
      <p>Every study answers the same triad. First, what can physically be built: measured constraints, structure, daylight, drainage and access. Second, what is likely to get consent: the property's permitted development position under the General Permitted Development Order, the planning history, any conservation designation, and how the council has decided comparable proposals (GPDO 2015; MHCLG, 2024). Third, what it will roughly cost: option-by-option cost banding, so ambition and budget meet each other before the design does.</p>
      <p>This is the work the RIBA Plan of Work locates at Stages 0 and 1, strategic definition and preparation, precisely because the industry's collective experience is that projects which skip it pay for the omission later (RIBA, 2020).</p>

      <h2>The pre-purchase case</h2>
      <p>The highest-value studies happen before a property is bought. A buyer weighing two houses is really weighing two sets of possibilities, and those possibilities are checkable facts: whether the side return can be enclosed, whether the loft has the volume allowance left, whether an Article 4 direction has quietly removed the rights the estate agent's brochure assumes. Where certainty matters, the position can be made formal with a lawful development certificate application under s.192 of the Town and Country Planning Act 1990, which establishes in law that a proposed use or development would be lawful.</p>

      <div class="a-note">A feasibility study typically costs a fraction of one percent of a London property transaction, and it prices the thing the purchase is actually being made for: what the building can become. We can usually complete one inside a conveyancing window.</div>

      <h2>What you receive, and what it commits you to</h2>
      <p>Our studies deliver drawn options, usually two or three, a planning risk assessment for each, cost banding, and a written recommendation. The fee is fixed and agreed before we start, and the study commits you to nothing: it is a standalone appointment whose output is yours. Some clients proceed with us, some use the study to negotiate a purchase price, and some learn that the project they imagined does not work, which is the study doing exactly its job at the cheapest possible moment.</p>

      <h2>How to read a feasibility study</h2>
      <p>A good study is honest about risk rather than optimistic about everything. Planning conclusions should cite the policies and local decisions they rest on; cost bands should state what they include and exclude; and at least one option should usually be the modest one, because the comparison is the information. If every option in a study is achievable and affordable, the study has been written to please rather than to inform.</p>
''',
 refs=[
  "Ministry of Housing, Communities and Local Government (2024) <em>National Planning Policy Framework</em>. London: MHCLG.",
  "Royal Institute of British Architects (2020) <em>RIBA Plan of Work 2020 Overview</em>. London: RIBA Publishing.",
  "Town and Country Planning Act 1990, c. 8. London: HMSO.",
  "Town and Country Planning (General Permitted Development) (England) Order 2015 (SI 2015/596). London: The Stationery Office.",
 ],
 cta_h='Thinking of buying, or unsure if your project works?',
 cta_p='A fixed-fee feasibility study answers the planning, design and cost questions before you commit. Most complete within two to three weeks.'))

for a in ARTICLES:
    open(f"blog/{a['slug']}.html", 'w').write(article_page(**a))
    print(f"blog/{a['slug']}.html", os.path.getsize(f"blog/{a['slug']}.html")//1024, 'KB')
