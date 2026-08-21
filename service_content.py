# Content for all 8 service hubs — aggressive skim-ready version.
# ~800 words per hub. Scannable in 45 seconds.
# Honest, restrained, non-hype register. National scope. No fee ranges.

HUBS = [

# ==================================================================
# 01 — PLANNING APPLICATIONS
# ==================================================================
dict(
    slug='planning-applications',
    title='Planning Applications',
    meta_desc='Planning application preparation and submission by FADP Architecture. Full applications, householder, prior approval and pre-application, from feasibility to determination.',
    strap='Applications designed to be approved, not argued. We prepare, submit and manage the whole process with your local planning authority.',
    intro_lead=[
        'A planning application is the formal request to a local planning authority for permission to build. Most alterations to a property need one. Getting it wrong &mdash; wrong route, wrong documentation, wrong argument &mdash; costs months and, in the worst case, ends in a refusal that follows the address for years. We handle the whole process: feasibility, drawings, statements, submission, and the case-officer conversations that decide approval or refusal. Fees fixed in writing before we begin. First consultation free.',
    ],
    sections=[
        dict(h2='When you need one',
             body=[
                 'You need an application whenever the works are not covered by permitted development, or when those rights have been withdrawn by an Article 4 direction, a planning condition, or the property being in a conservation area, National Park or AONB.',
                 'In practice: most rear extensions above a certain depth, most side extensions, most changes of use, most work to flats, and almost all commercial work. Loft conversions often go through permitted development but the exceptions catch people out. We run the check as part of the free consultation.',
             ]),
        dict(h2='The application types',
             body=[
                 '<strong>Householder</strong> — extensions and alterations to a single house. Shortest route.',
                 '<strong>Full</strong> — flats, new builds, commercial, changes of use, or works beyond householder scope.',
                 '<strong>Prior approval</strong> — where permitted development applies but the authority still checks size, siting and impact. Faster than full, but the tests are real.',
                 '<strong>Lawful development certificate</strong> — confirms works are lawful without needing planning permission. Useful for anything you may need to prove to a buyer or lender.',
                 '<strong>Pre-application</strong> — a paid conversation with the case officer before you submit. On borderline sites, almost always worth it.',
             ]),
        dict(h2='What decides approval',
             body=[
                 'Applications are decided on the local plan and on material considerations — the NPPF, neighbourhood plans, heritage, daylight, ecology, highways. A good application evidences its compliance in the officer&rsquo;s own language. A weak one leaves the officer to do that translation, which they rarely have time for.',
                 'The single biggest predictor of approval is not the design; it is the quality of the supporting statements. Most of our time goes on the argument, not the drawings.',
             ]),
    ],
    deliverables=[
        'Application forms completed and validated',
        'Existing and proposed plans, elevations and sections',
        'Site location and block plans with red-line boundary',
        'Design and Access Statement where required',
        'Heritage, daylight, ecology and other supporting reports where relevant',
        'CIL forms and pre-commencement condition notices',
        'Case-officer liaison and response to consultee comments',
        'Amendments or resubmission strategy if refused',
    ],
    process=[
        ('Assessment', 'Site, policy, planning history and constraints checked. The right route confirmed.'),
        ('Design', 'The proposal drawn to meet the brief inside the policy tests.'),
        ('Statements', 'Supporting statements written to answer the tests the officer will apply.'),
        ('Submission', 'Application validated, submitted and its progress managed on your behalf.'),
        ('Determination', 'Consultee comments and officer queries handled. Amendments negotiated if needed.'),
    ],
    standards=dict(
        intro='The frameworks we work to as standard.',
        items=[
            ('Town and Country Planning Act 1990', 'The primary legislation. Every application is made under it.'),
            ('National Planning Policy Framework', 'Updated December 2024. Material to every decision.'),
            ('Local Plan', 'The council&rsquo;s own policy document, which carries statutory weight.'),
            ('Neighbourhood Plans', 'Where adopted, carry the same weight as the local plan.'),
            ('Article 4 Directions', 'Removes permitted development rights in specified areas. Common in London.'),
            ('Building Safety Act 2022', 'Changed designer duties on all projects. Coordinated with planning where relevant.'),
        ],
    ),
    faqs=[
        ('How long does an application take?',
         'Statutory eight weeks for a householder, thirteen for a full application, from validation. Total time from starting design to a decision is usually four to six months on a straightforward project.'),
        ('What does it cost?',
         'The council&rsquo;s application fee is a statutory amount (currently &pound;258 for a householder application; more for full and commercial). Our fee is separate, fixed in writing before we begin.'),
        ('What if it&rsquo;s refused?',
         'Every refusal comes with reasons. Three routes usually follow: an amended resubmission (often at no extra fee within twelve months), a planning appeal to the Planning Inspectorate, or an alternative permitted-development route.'),
        ('Do neighbours have to be consulted?',
         'Yes — the authority runs formal consultation. Objections don&rsquo;t automatically defeat an application, but well-founded ones are weighted. On sensitive projects we recommend a five-minute conversation with neighbours before submission.'),
        ('Can I appeal a refusal?',
         'Yes. Appeals go to the Planning Inspectorate and take four to nine months. Well-argued appeals win regularly.'),
        ('Do I need permission to change use?',
         'Usually yes. Use Class E (introduced 2020) merged several former uses, making some changes automatic and others restricted.'),
        ('What is permitted development?',
         'A set of national rights allowing certain works without an application. Detailed conditions apply, and many properties have had these rights removed by Article 4 or planning conditions.'),
        ('Do you work outside London?',
         'Yes. English planning law is national. We work across the UK.'),
    ],
    closing='Get in touch and we&rsquo;ll confirm the route and the fee.',
),


# ==================================================================
# 02 — FEASIBILITY STUDIES
# ==================================================================
dict(
    slug='feasibility-studies',
    title='Feasibility Studies',
    meta_desc='Property feasibility studies by FADP Architecture. What can be built, whether it will secure planning, and what it will cost — before you commit.',
    strap='What can be built, whether it will secure planning, and what it will cost. The cheapest decision on any project, made first.',
    intro_lead=[
        'A feasibility study answers three questions before design begins: what can be built, will it secure planning, and roughly what will it cost. It sits at the front of every serious project. The effort is measured in weeks; what it saves you is the expensive alternative &mdash; committing to a scheme that runs into a policy wall six months in, or buying a property whose real potential is smaller than the estate agent implied.',
    ],
    sections=[
        dict(h2='When it makes sense',
             body=[
                 '<strong>Before you buy</strong> a property whose price depends on future potential. The cheapest way to test what that potential actually is.',
                 '<strong>Before you commit</strong> to a design direction on a property you already own.',
                 '<strong>Before you speak to a builder.</strong> Contractors price what they are given; the study gives them something worth pricing.',
                 '<strong>When two or more options are on the table</strong> &mdash; extend versus loft, refurbish versus rebuild &mdash; and you need a like-for-like comparison.',
             ]),
        dict(h2='What we examine',
             body=[
                 '<strong>The site.</strong> Orientation, aspect, access, levels, ground, existing structure, services and constraints.',
                 '<strong>The policy.</strong> Local plan, neighbourhood plan, conservation designations, Article 4 directions, listed status, TPOs. Read before any option is tested.',
                 '<strong>The planning history.</strong> What has been applied for at your address before, and what the council has approved nearby. Precedent from two doors down is more predictive than policy alone.',
                 '<strong>The construction reality.</strong> Cost banded per option, using rates per square metre for the relevant construction type. Precise costing is a QS&rsquo;s job later.',
             ]),
        dict(h2='What you get',
             body=[
                 'A written report (typically 20-40 pages), two or three options drawn to sketch design level, a cost band for each option with assumptions stated, and a recommended route to permission. A meeting to walk through it all at the end.',
             ]),
    ],
    deliverables=[
        'Written feasibility report with constraints and options',
        'Two or three options drawn to sketch design level',
        'Site analysis diagrams: sun path, aspect, constraints',
        'Planning-policy summary for your address',
        'Planning-history review and nearby precedents',
        'Cost banding per option, with assumptions stated',
        'Recommended route to permission if you proceed',
        'Handover meeting',
    ],
    process=[
        ('Instruction', 'Short call to confirm the brief and site. Fixed fee agreed before we start.'),
        ('Site & policy', 'Site visit, survey as needed, full read of policy and planning history.'),
        ('Options', 'Two or three options developed to sketch design level and tested against the brief.'),
        ('Costing & report', 'Cost banding applied. Report and drawings issued in one document.'),
        ('Handover', 'Meeting to walk through findings. If you proceed, the fee is credited against the next stage.'),
    ],
    standards=dict(
        intro='What we assess against as standard.',
        items=[
            ('National Planning Policy Framework', 'Read for the policy tests likely to apply to the site.'),
            ('Local Plan and adopted policies', 'The specific policies and SPDs that carry weight in decisions.'),
            ('Planning history of the address', 'Every previous application, decision and appeal.'),
            ('Permitted development rights', 'Whether they apply, and whether they have been removed.'),
            ('Heritage and conservation status', 'Listed status, curtilage, conservation area, Historic England guidance.'),
            ('Party wall considerations', 'Flagged where they will affect programme or design.'),
        ],
    ),
    faqs=[
        ('How long does it take?',
         'Typically four to six weeks. Simpler sites can be quicker; complex heritage or policy takes longer.'),
        ('What does it cost?',
         'Fixed fee, agreed before we begin, based on the site and the options to be tested. A fraction of what construction will cost.'),
        ('Do I need one before I buy?',
         'Strongly recommended if the purchase depends on the potential to extend or develop. We regularly complete studies inside a purchase timeline.'),
        ('Can I use the study in a planning application?',
         'The sketch drawings are the starting point, not the finished application. The analysis and policy review all carry through.'),
        ('Are surveys included?',
         'Site visits are included. Formal measured, topographical or ecological surveys are third-party costs and separate.'),
        ('What if the site can&rsquo;t support what I want?',
         'The value of the study is the honest answer. If the brief and the site can&rsquo;t both be met, we say so and set out what could realistically be achieved instead.'),
        ('Do you cover commercial and mixed-use?',
         'Yes. Same discipline, different policy tests and cost bases.'),
        ('Is the fee credited if we go on to design?',
         'Yes. If you appoint us within twelve months, the feasibility fee is credited against the concept design fee.'),
    ],
    closing='Get in touch and we&rsquo;ll tell you whether a study is worth commissioning.',
),


# ==================================================================
# 03 — SITE ANALYSIS
# ==================================================================
dict(
    slug='site-analysis',
    title='Site Analysis',
    meta_desc='Site analysis by FADP Architecture. Constraints, opportunities, orientation, access and context — the groundwork every design decision depends on.',
    strap='Constraints, opportunities, orientation, access and context. The groundwork every design decision depends on.',
    intro_lead=[
        'Site analysis reads the site properly before anything is designed on it. It maps what is already there &mdash; the constraints, opportunities, neighbours, light, ground, drainage, trees, access, acoustic and visual context &mdash; and translates them into design parameters a scheme has to work within. It is not a survey (which measures) or a feasibility study (which tests options); it sits between the two.',
    ],
    sections=[
        dict(h2='When to commission it separately',
             body=[
                 '<strong>Before buying land</strong> that has not been built on, or has been built on badly.',
                 '<strong>When issuing a brief</strong> to multiple designers &mdash; a shared analysis stops each entrant duplicating the discovery work.',
                 '<strong>When a scheme has failed at planning</strong> and you need to know why. Refusal reasons often point back to a condition missed at the start.',
                 '<strong>When multiple owners are involved</strong>, or a phased development is planned. The analysis becomes the shared reference document.',
             ]),
        dict(h2='What we examine',
             body=[
                 '<strong>Physical.</strong> Topography, levels, ground conditions, orientation, sun path, prevailing wind, drainage, services.',
                 '<strong>Legal.</strong> Boundaries, easements, covenants, rights of way, planning designations, listed status, TPOs, Article 4 directions, planning history.',
                 '<strong>Movement.</strong> Vehicular, pedestrian, cycle and servicing routes. Highway constraints.',
                 '<strong>Environmental.</strong> Ecology, protected species, trees, flood zone, drainage, air quality, noise.',
                 '<strong>Visual.</strong> Views in and out, sightlines, adjacent heights, character, materials palette.',
                 '<strong>Social.</strong> Neighbours, existing patterns of use, likely stakeholder reactions.',
             ]),
        dict(h2='What we deliver',
             body=[
                 'A written report by theme (drawing conclusions, not just listing observations), analysis diagrams over an OS or site plan base, a consolidated constraints-and-opportunities plan, and a short set of design parameters for the next stage.',
             ]),
    ],
    deliverables=[
        'Written report with findings and design implications',
        'Sun path and aspect analysis diagrams',
        'Constraints and opportunities plan',
        'Movement, access and servicing analysis',
        'Views and townscape context diagrams',
        'Trees, ecology and protected features plan',
        'Boundary, easements and covenants summary',
        'Design parameters brief for the next stage',
    ],
    process=[
        ('Instruction', 'Confirm the scope and purpose. Fixed fee agreed before starting.'),
        ('Site visit', 'Structured visit at the right time for the aspect being analysed.'),
        ('Desktop research', 'Planning, ecology, Land Registry, TPOs. All checked against current sources.'),
        ('Analysis & drawings', 'Findings mapped as diagrams, reduced to a short design brief.'),
        ('Handover', 'Report issued and walked through in a meeting.'),
    ],
    standards=dict(
        intro='The sources we work from as standard.',
        items=[
            ('Ordnance Survey MasterMap', 'Base topographic data. Always confirmed against a site visit.'),
            ('Land Registry Title Register', 'Boundaries, easements, covenants, rights of way.'),
            ('LPA policy maps', 'Conservation areas, Article 4 directions, listed buildings, TPOs.'),
            ('MAGIC and NBN Atlas', 'Ecology, protected species, flood zones, designated sites.'),
            ('BS 5837:2012', 'The British Standard for trees in relation to design and construction.'),
            ('Historic Environment Record', 'The local authority-held record of heritage and archaeology.'),
        ],
    ),
    faqs=[
        ('Is it the same as a site survey?',
         'No. A survey measures the site; site analysis interprets what those measurements mean for design.'),
        ('Do I need it if you&rsquo;re doing my feasibility study?',
         'No — it&rsquo;s included as the first stage of every feasibility study. Only worth commissioning separately when needed independently of design work.'),
        ('How long does it take?',
         'Residential-scale: two to three weeks. Larger or complex sites: four to six.'),
        ('Can you analyse a site before I&rsquo;ve bought it?',
         'Yes, and it&rsquo;s often the most valuable time. Desktop research and design-parameter conclusions don&rsquo;t need physical access.'),
        ('What if it identifies a serious problem?',
         'You&rsquo;ve found it in the cheapest possible way. Common examples: unregistered rights of way, undisclosed TPOs, ground contamination indicators. Better to know before you commit.'),
        ('Do you cover commercial and industrial?',
         'Yes. Same framework, different emphasis &mdash; servicing, contamination and industrial constraint typically carry more weight than residential amenity.'),
    ],
    closing='Get in touch and we&rsquo;ll confirm what would be involved for your site.',
),


# ==================================================================
# 04 — BIM
# ==================================================================
dict(
    slug='bim',
    title='Building Information Modelling',
    meta_desc='BIM services by FADP Architecture. Fully coordinated 3D models, clash detection, accurate quantities and construction drawings generated from a single source of truth.',
    strap='One coordinated 3D model that runs from concept to construction. Clash-detected, quantity-accurate, generating every drawing the project needs.',
    intro_lead=[
        'BIM is the discipline of designing a building as a single coordinated 3D model rather than as a set of separate drawings. Every element carries data about what it is, what it&rsquo;s made of, how it connects, and what happens to it in construction and use. Drawings issued from it are consistent by construction, quantities are accurate as of the moment they&rsquo;re exported, and coordination between disciplines happens in design time rather than on site. We work in BIM as standard on every project &mdash; the effort sits inside our fixed fee.',
    ],
    sections=[
        dict(h2='What it means in practice',
             body=[
                 'A wall is not a line; it&rsquo;s a wall of a specific construction, thickness, insulation value and material. A window is not a rectangle; it&rsquo;s a window of specific size, glazing performance and installation detail.',
                 'Once the model exists, everything downstream comes from it. Plans, sections, elevations and details are views into the same model, so they cannot contradict each other. Quantities export as data, not counted by hand. Clash detection compares structure, drainage and services against the fabric before drawings are issued.',
                 'On coordinated projects the model integrates with the structural engineer&rsquo;s, the services engineer&rsquo;s and any specialists. That&rsquo;s where BIM does its most valuable work &mdash; on traditionally drawn projects, the contractor finds the coordination problems, and every one becomes a variation.',
             ]),
        dict(h2='What you get as a client',
             body=[
                 'A 3D model you can walk through at any stage of design. Drawings that are consistent, up to date and internally coordinated. Accurate quantities for tender &mdash; contractors bid tighter against real data. Fewer variations on site. A digital asset at handover, genuinely useful for future alterations, insurance and sale.',
             ]),
    ],
    deliverables=[
        'Fully coordinated 3D model of existing and proposed',
        'Clash detection before tender',
        'Accurate quantities and schedules for pricing',
        'Interactive visualisations at every design stage',
        'Drawing packages generated from the single model',
        'IFC exports for other consultants',
        'BIM Execution Plan on ISO 19650 projects',
        'Model handed over as a digital asset at completion',
    ],
    process=[
        ('Set up', 'Model set up at the start with the right templates and exchange formats.'),
        ('Model', 'Existing and proposed built in 3D from survey data. Materials and specs attached.'),
        ('Coordinate', 'Structure, drainage and services resolved together. Clashes closed out.'),
        ('Quantify', 'Schedules exported for contractors to price against. Updates automatically.'),
        ('Deliver', 'Construction drawings issued from the model, consistent by construction.'),
    ],
    standards=dict(
        intro='The standards we work within.',
        items=[
            ('BS EN ISO 19650 series', 'The core BIM standard, adopted in the UK to replace PAS 1192.'),
            ('UK BIM Framework', 'The umbrella framework hosting ISO 19650 and supporting guidance.'),
            ('IFC (Industry Foundation Classes)', 'Open, vendor-neutral format for cross-discipline model exchange.'),
            ('BS 8541 series', 'The British Standard for BIM library objects.'),
            ('COBie', 'Structured spreadsheet for handover asset data on larger projects.'),
            ('Building Safety Act 2022', 'The golden thread of information delivered through the BIM model.'),
        ],
    ),
    faqs=[
        ('Will I see my project in 3D?',
         'Yes, at every design stage. Most clients find decisions much easier in 3D than on plan.'),
        ('Does BIM cost more?',
         'No. Modelling sits inside our fixed design fee. On balance it saves money by tighter tender pricing and fewer variations on site.'),
        ('Do contractors need BIM software?',
         'No. Contractors receive conventional drawings and schedules. The BIM benefit is baked in.'),
        ('What is BIM Level 2?',
         'The UK standard for centrally-procured public projects since 2016. We apply the working method to all projects, not just those where it&rsquo;s mandated.'),
        ('Can BIM handle existing and heritage buildings?',
         'Yes. The case is often stronger &mdash; a model of the existing fabric makes coordination with new work possible.'),
        ('Who owns the model?',
         'Typically the client, on payment in full, with the practice retaining design copyright. Same principle as conventional drawings.'),
        ('What happens to it after completion?',
         'Handed over as part of completion documentation. Sensible clients keep it for future alterations and asset management.'),
    ],
    closing='Get in touch and we&rsquo;ll talk through what BIM looks like on your project.',
),


# ==================================================================
# 05 — MASTERPLANNING & URBAN DESIGN
# ==================================================================
dict(
    slug='masterplanning-urban-design',
    title='Masterplanning & Urban Design',
    meta_desc='Masterplanning and urban design by FADP Architecture. Sites, streets and neighbourhoods — capacity testing, design codes and delivery frameworks argued through policy to consent.',
    strap='Sites, streets and neighbourhoods. Capacity, density and design codes, argued through policy and taken to consent.',
    intro_lead=[
        'Masterplanning operates at the scale above the individual building &mdash; how a site is divided, where movement runs, what density it can carry, how the public realm between the buildings works. It is a policy discipline as much as a design one, governed by the local plan, the NPPF, and increasingly the design codes authorities now expect for phased or multi-developer schemes. Led here by Aun Naeem, whose experience covers sites from single infill plots to multi-plot frameworks.',
    ],
    sections=[
        dict(h2='When it&rsquo;s the right first step',
             body=[
                 'When the site is too large or complex to be treated as a single building brief. When a scheme will be delivered in phases or by multiple developers over time. When a site&rsquo;s potential is being tested for the first time and finance depends on a unit count. When the site sits inside a regeneration brief or emerging plan allocation.',
             ]),
        dict(h2='What a masterplan contains',
             body=[
                 '<strong>Site analysis</strong> at strategic scale.',
                 '<strong>Capacity study</strong> testing how many units or how much floorspace the site can genuinely support once daylight, aspect, access, drainage and policy are honestly applied.',
                 '<strong>Layout</strong> delivering the capacity: blocks arranged around streets, squares, courtyards.',
                 '<strong>Movement strategy</strong> — vehicles, pedestrians, cyclists, servicing, refuse.',
                 '<strong>Public realm strategy</strong> — what happens between the buildings. The most decisive part.',
                 '<strong>Phasing plan</strong> — how the scheme is built out and how partial phases work as places.',
                 '<strong>Design code</strong> where the scheme will be delivered by others. Sets rules on heights, massing, materials, frontage.',
             ]),
        dict(h2='The planning route',
             body=[
                 'Most masterplans reach consent through an <strong>outline application</strong> — establishing principle and parameters, reserving detailed design for later "reserved matters" applications. On smaller or single-owner masterplans, a <strong>full application</strong> is sometimes right. Either route benefits from structured <strong>pre-application engagement</strong> with the authority.',
             ]),
    ],
    deliverables=[
        'Site analysis at strategic scale',
        'Capacity study with density and typology testing',
        'Masterplan layout drawings, models and diagrams',
        'Movement, access and public realm strategy',
        'Phasing and delivery framework',
        'Design code where the scheme is built by others',
        'Design and Access Statement for the application',
        'Pre-application and community engagement where required',
    ],
    process=[
        ('Understand', 'Site, context, constraints and policy.'),
        ('Test', 'Capacity options modelled and compared honestly.'),
        ('Frame', 'The chosen option developed as a masterplan or framework, with a design code where needed.'),
        ('Engage', 'Pre-application meetings and community engagement. Concerns identified early cost far less to resolve.'),
        ('Consent', 'Outline or full permission with the parameter plans and design code.'),
    ],
    standards=dict(
        intro='The primary references we work with.',
        items=[
            ('NPPF Chapter 12', 'The framework&rsquo;s chapter on well-designed and beautiful places.'),
            ('National Design Guide (2021)', 'How well-designed places can be achieved in practice.'),
            ('National Model Design Code (2021)', 'The template for local design codes.'),
            ('Levelling-up and Regeneration Act 2023', 'Strengthened the role of design codes in plan-making.'),
            ('Local Plan and Neighbourhood Plans', 'The site-specific policies that carry statutory weight.'),
            ('Building for a Healthy Life (2020)', 'Industry benchmark for the design of neighbourhoods.'),
        ],
    ),
    faqs=[
        ('What size of site do you work on?',
         'From infill plots and backland sites up to multi-plot frameworks. The question is whether the site needs decisions about layout and density rather than just a single building.'),
        ('What is a design code?',
         'A document setting the rules a later designer must follow &mdash; heights, massing, materials, frontage. Increasingly required by authorities for phased schemes.'),
        ('Can you take a site through outline planning?',
         'Yes. Outline with parameter plans and a design code is the standard route for large or phased sites.'),
        ('How is capacity tested?',
         'Not by dividing site area by an assumed density. We model actual buildings on the actual site against the daylight, amenity and drainage standards. The number that survives is the real capacity — almost always lower than the early estimate.'),
        ('Do you work on plan-making?',
         'Yes. Site promotion through Local Plan reviews, Neighbourhood Plan support, response to emerging policy.'),
        ('Do you run community engagement?',
         'Yes. Workshops, exhibitions, targeted stakeholder meetings. Objections at planning stage often trace back to issues that could have been resolved earlier.'),
        ('What about environmental impact assessment?',
         'For schemes above thresholds an EIA is required. We coordinate with the specialists who prepare it.'),
        ('Do you work on regeneration?',
         'Yes. Both directors have regeneration experience across residential and mixed-use.'),
    ],
    closing='If you have a site you&rsquo;re considering, a director will make time to talk it through.',
),


# ==================================================================
# 06 — LISTED BUILDINGS
# ==================================================================
dict(
    slug='listed-buildings',
    title='Listed Buildings',
    meta_desc='Listed building consent applications, heritage statements and specialist advice on works to Grade I, II* and II listed buildings by FADP Architecture.',
    strap='Listed building consent, heritage statements and schedules of works, argued in the language conservation officers use.',
    intro_lead=[
        'Any works affecting a listed building&rsquo;s character need listed building consent &mdash; external, internal, and often structures in its curtilage. The test is not visibility from the street; it is effect on significance. Unauthorised works are a criminal offence under Section 9 of the Planning (Listed Buildings and Conservation Areas) Act 1990, carrying unlimited fines and up to two years&rsquo; imprisonment, with no time limit on enforcement. Done well, listed consent is a design conversation leading to a better building. Done badly, it is a two-year stalemate followed by refusal.',
    ],
    sections=[
        dict(h2='What listed status restricts',
             body=[
                 'Almost all external alterations, most internal alterations that affect historic fabric or spatial hierarchy, and often works to outbuildings and walls within the curtilage.',
                 'The three grades (I, II*, II) indicate significance, but they don&rsquo;t change the consent regime &mdash; the same consent is required for a Grade II as for a Grade I. The grade affects how sensitive the officer&rsquo;s judgement will be.',
                 'A common trap: internal features often carry more significance than external ones. In Georgian and Regency townhouses the stair and principal rooms are the historic core; owners routinely underestimate what would need consent internally.',
             ]),
        dict(h2='The test the officer applies',
             body=[
                 'Section 16 of the 1990 Act requires the authority to have special regard to preserving the building. In practice, the officer decides whether the works cause <strong>harm</strong> to significance, and if so, whether the harm is outweighed by public benefits.',
                 'The officer&rsquo;s judgement is shaped almost entirely by the <strong>heritage statement</strong>. A heritage statement is not a description; it is an argument. The biggest predictor of success is not the design quality &mdash; it is the quality of the heritage statement in front of the officer.',
             ]),
    ],
    deliverables=[
        'Listed building consent applications, submitted and managed',
        'Heritage statements written to the significance-and-harm framework',
        'Schedules of works with justification for each intervention',
        'Specification of appropriate materials, methods and craftsmen',
        'Curtilage assessments where the position is unclear',
        'Negotiation with conservation officers, Historic England and amenity societies',
        'Coordination with parallel planning applications',
        'Advice on unauthorised works and retrospective applications',
    ],
    process=[
        ('Understand', 'Research the listing, history and what carries significance.'),
        ('Design', 'Change located where significance is lowest. Every intervention justified.'),
        ('Pre-app', 'Early conversation with the conservation officer aligns the application with their reading.'),
        ('Justify', 'Heritage statement and schedule of works make the case in the officer&rsquo;s own terms.'),
        ('Consent', 'Submission, negotiation, conditions negotiated through to workable approval.'),
    ],
    standards=dict(
        intro='The primary references we work from.',
        items=[
            ('Planning (Listed Buildings and Conservation Areas) Act 1990', 'The primary legislation. Sections 7-9 create the consent regime; Section 16 sets the statutory test.'),
            ('NPPF Chapter 16', 'The framework&rsquo;s heritage policy. Paragraphs 200-208 applied to every decision.'),
            ('Historic England Good Practice Advice', 'GPA 2 on significance and GPA 3 on setting.'),
            ('Historic England Conservation Principles (2008)', 'Framework for identifying significance.'),
            ('Local authority conservation policies', 'Adopted local plan policies and conservation area appraisals.'),
            ('BS 7913:2013', 'The British Standard for conservation of historic buildings.'),
        ],
    ),
    faqs=[
        ('Does everything need consent, even inside?',
         'Almost everything that affects the building&rsquo;s character. Some routine like-for-like repairs don&rsquo;t, but the line is finer than most owners assume. We establish exactly what needs consent at the start of every project, in writing.'),
        ('How long does consent take?',
         'Statutory eight weeks. Pre-application discussion typically adds four to six weeks up front but shortens the formal determination. Total from starting design: four to eight months on complex applications.'),
        ('Can I modernise a listed building?',
         'Almost always, and often substantially. Kitchens, bathrooms, services and extensions are achieved in listed buildings every week. What&rsquo;s not usually possible is wholesale gutting or interventions that erase the historic core.'),
        ('What&rsquo;s the difference between Grade I, II* and II?',
         'Relative significance. All three carry the same consent requirement; the grade affects how sensitive the officer&rsquo;s judgement will be.'),
        ('Do I need planning permission too?',
         'Often yes. Planning for changes of use and extensions; listed consent for works affecting character. Where both are needed we prepare them in parallel.'),
        ('What if works were done without consent?',
         'Specific advice on the facts needed. Sometimes a retrospective application regularises; sometimes undoing the works is pragmatic. Enforcement has no time limit on listed buildings. We advise without judgement.'),
        ('Can you deal with Historic England?',
         'Yes. HE is a statutory consultee on Grade I and II* applications and some Grade II. Where consulted, we deal with them directly.'),
        ('Do listed buildings have to meet current building regulations?',
         'Yes, but the regulations recognise that historic buildings sometimes can&rsquo;t meet current standards without unacceptable heritage harm. Reasonable provision is interpreted in light of significance.'),
    ],
    closing='If you own or are considering a listed building, the first consultation is free. A director will visit where practical.',
),


# ==================================================================
# 07 — CONSERVATION AREAS
# ==================================================================
dict(
    slug='conservation-areas',
    title='Conservation Areas',
    meta_desc='Conservation area planning applications, Article 4 checks and townscape-evidenced arguments by FADP Architecture. Designed to secure permission where restrictions apply.',
    strap='Article 4 directions, permitted development checks and applications evidenced by what your council has already approved.',
    intro_lead=[
        'A conservation area is an area of special architectural or historic interest designated under Section 69 of the 1990 Act. Designation removes some permitted development rights automatically, and many areas &mdash; particularly in London &mdash; carry Article 4 directions that remove further rights, street by street. Every application inside is decided against the character-and-appearance test rather than a general design test, which changes the evidence a good application needs to present. The first consultation includes the check on which rights survive at your address.',
    ],
    sections=[
        dict(h2='What&rsquo;s restricted automatically',
             body=[
                 'The size of rear extensions is reduced. Roof extensions are removed in most cases. Chimneys, flues and soil pipes on principal or side elevations are restricted. Cladding &mdash; stone, artificial stone, pebble dash, render, timber, plastic or tiles &mdash; is removed. Demolition of most unlisted buildings requires planning permission.',
                 'Every tree in a conservation area with a trunk diameter greater than 75mm at 1.5m is protected. Six weeks&rsquo; notice must be given for any works to it &mdash; failure to give notice is a criminal offence.',
             ]),
        dict(h2='Article 4 directions',
             body=[
                 'A formal direction removing specified permitted development rights in a defined area. Common examples in London: changing window styles, replacing front doors, painting brickwork, altering front elevations, installing solar panels or satellite dishes on principal elevations.',
                 'Works undertaken without permission where a direction applies are unlawful, and the authority can require reversal. This is one of the most common enforcement issues in London. The check for your address is included in the free consultation.',
             ]),
        dict(h2='How applications are argued differently',
             body=[
                 '<strong>Precedent is central.</strong> A well-evidenced argument that similar works have been approved nearby is often the strongest evidence in favour.',
                 '<strong>Townscape evidence matters.</strong> Photographs, elevational studies and street-scene drawings are usually more persuasive than plans and elevations alone.',
                 '<strong>Materials are decisive.</strong> The specific brick, mortar, window profile. On sensitive elevations we specify to a level of detail well beyond what would be needed elsewhere.',
                 '<strong>Character appraisals set the terms.</strong> Applications that read the appraisal and address it directly succeed more often.',
             ]),
    ],
    deliverables=[
        'Article 4 check specific to the property address',
        'Permitted development analysis of what remains',
        'Design in context, evidenced by local precedent',
        'Street scene and townscape drawings',
        'Design and Access Statement addressing the character-and-appearance test',
        'Materials specification to the level the officer will scrutinise',
        'Coordination with any listed building consent issues',
        'Negotiation with conservation officers and amenity societies',
    ],
    process=[
        ('Check', 'Designation, Article 4 directions, character appraisal, planning history.'),
        ('Precedent', 'What the council has approved nearby, and on what reasoning.'),
        ('Design', 'A proposal that meets the brief while passing the character test.'),
        ('Statement', 'Design and access statement citing precedent and character appraisal.'),
        ('Apply', 'Submission with the townscape evidence that makes refusal hard to justify.'),
    ],
    standards=dict(
        intro='The framework we work within.',
        items=[
            ('Planning (Listed Buildings and Conservation Areas) Act 1990, Sections 69-74', 'Establishes the conservation area regime and the special attention duty.'),
            ('Town and Country Planning (General Permitted Development) Order 2015', 'Sets which permitted development rights are automatically removed.'),
            ('NPPF Chapter 16', 'The framework&rsquo;s policy on the historic environment.'),
            ('Conservation area appraisal', 'The council&rsquo;s own document describing what makes the area special.'),
            ('Article 4 direction (where applicable)', 'The specific direction for the property.'),
            ('Historic England guidance', 'Good Practice Advice notes on conservation area management.'),
        ],
    ),
    faqs=[
        ('How do I know if I&rsquo;m in a conservation area?',
         'Council policy maps show every boundary and Article 4 direction. We run this check as part of the free consultation.'),
        ('Can I still extend?',
         'Usually yes. Extensions are approved constantly. The bar is design quality, materials and townscape evidence.'),
        ('What is an Article 4 direction?',
         'A direction removing specific permitted development rights &mdash; often on windows, doors, brickwork or front elevations. Every London conservation area address should be checked.'),
        ('What if I&rsquo;ve already done work without checking?',
         'Specific advice on the facts. Retrospective applications are often the pragmatic route. If refused, enforcement may follow. We advise without judgement.'),
        ('Do I need conservation area consent as well as planning?',
         'No. Conservation Area Consent as a separate regime was abolished in 2013. Everything goes through the planning application process.'),
        ('What about trees?',
         'Every tree over 75mm trunk diameter is protected. Six weeks&rsquo; notice of any works must be given &mdash; failure is a criminal offence.'),
        ('Are solar panels allowed?',
         'Sometimes. On principal or side elevations they usually need permission and Article 4 often restricts them further. On rear elevations the restrictions are lighter.'),
        ('Does the conservation officer&rsquo;s view matter?',
         'They&rsquo;re a statutory consultee on many applications and provide specialist advice to the planning officer. Their view carries significant weight on character-and-appearance. Pre-application engagement often makes the difference.'),
    ],
    closing='The first consultation includes the Article 4 check and an initial view on what would be achievable.',
),


# ==================================================================
# 08 — PRINCIPAL DESIGNER
# ==================================================================
dict(
    slug='principal-designer',
    title='Principal Designer',
    meta_desc='Principal Designer appointments under CDM 2015 and the Building Safety Act 2022 by FADP Architecture. Formal duty holder, risk registers and pre-construction information kept properly.',
    strap='The legal duty holder role under CDM 2015 and the Building Safety Act 2022, taken formally and recorded properly.',
    intro_lead=[
        'Principal Designer is a legal role, not a professional title. Two Acts create it. Under CDM 2015 a Principal Designer must be appointed on any project involving more than one contractor &mdash; almost every project, including domestic. Under the Building Safety Act 2022 (in force October 2023), a separate Principal Designer role applies to all projects requiring building regulations approval, with expanded duties on higher-risk buildings. Both must be appointed in writing. Non-appointment isn&rsquo;t a defence &mdash; the duty defaults to the client personally under CDM 2015. Most homeowners have no idea this is the law.',
    ],
    sections=[
        dict(h2='The two roles',
             body=[
                 '<strong>The CDM 2015 Principal Designer</strong> plans, manages and monitors health and safety through pre-construction. Duties include identifying, eliminating or reducing foreseeable design risks; coordinating other designers; preparing pre-construction information and the health and safety file.',
                 '<strong>The Building Safety Act Principal Designer</strong> coordinates design work in relation to building regulations compliance. On all projects: plan, manage and monitor design work so it complies. On higher-risk buildings: expanded duties as part of the gateway regime.',
             ]),
        dict(h2='When each applies',
             body=[
                 '<strong>CDM 2015 PD:</strong> any project with more than one contractor. Includes almost every project of any size, and includes domestic &mdash; the pre-2015 domestic exemption was removed.',
                 '<strong>BSA PD:</strong> all projects requiring building regulations approval. Expanded on higher-risk buildings (residential ≥18m or ≥7 storeys with ≥2 units).',
                 'On a typical domestic project, both apply. The same person can hold both, and often does &mdash; we take both on our full-service appointments as standard.',
             ]),
        dict(h2='What the role actually does',
             body=[
                 '<strong>Design risk management</strong> — foreseeable risks identified, eliminated where possible, otherwise recorded.',
                 '<strong>Coordination</strong> of other designers&rsquo; CDM duties across the team.',
                 '<strong>Pre-construction information</strong> prepared for the Principal Contractor.',
                 '<strong>Building regulations compliance</strong> coordinated across all designers on BSA-applicable projects.',
                 '<strong>Health and safety file</strong> compiled and handed over at completion.',
             ]),
    ],
    deliverables=[
        'Formal Principal Designer appointment under CDM 2015, in writing',
        'Formal PD appointment under the Building Safety Act where applicable',
        'Design risk register maintained through design',
        'Pre-construction information document',
        'Coordination of other designers&rsquo; CDM duties',
        'Compliance coordination under the Building Safety Act',
        'Higher-risk building gateway support where applicable',
        'Health and safety file compiled at completion',
    ],
    process=[
        ('Appoint', 'Role confirmed in writing at the start, as both regulations require.'),
        ('Plan', 'Design risks identified from the beginning and designed out where possible.'),
        ('Coordinate', 'Other designers&rsquo; CDM duties managed. BSA compliance coordinated across the team.'),
        ('Record', 'Design risk register and PCI maintained through the design stages.'),
        ('Hand over', 'Health and safety file compiled and passed to the client at completion.'),
    ],
    standards=dict(
        intro='The primary references.',
        items=[
            ('Construction (Design and Management) Regulations 2015', 'The primary CDM 2015 legislation. Duties in Regulations 4-16.'),
            ('HSE L153', 'The HSE&rsquo;s Approved Code of Practice for CDM 2015.'),
            ('Building Safety Act 2022', 'Creates the BSA PD role. Core duties commenced October 2023.'),
            ('Building Regulations 2010', 'The regulations against which compliance is coordinated.'),
            ('Building Regulations Amendment (England) Regulations 2023', 'Introduced the BSA duty-holder regime.'),
            ('BSR guidance', 'The Building Safety Regulator&rsquo;s guidance on higher-risk buildings and the golden thread.'),
        ],
    ),
    faqs=[
        ('Does my house extension really need this?',
         'If more than one contractor is involved (almost every project once you count subcontractors), CDM 2015 requires a PD to be appointed in writing. The BSA PD duty also applies to any project needing building regulations approval, which includes almost every extension.'),
        ('Is it included in your full-service fee?',
         'Yes. On full appointments we take both PD roles as standard. No separate charge.'),
        ('Can you be PD on a project designed by someone else?',
         'Yes. Stand-alone PD appointments are quoted separately. We&rsquo;re frequently appointed on this basis where the designer doesn&rsquo;t hold the role.'),
        ('What&rsquo;s a higher-risk building?',
         'Broadly, residential buildings of ≥18m or ≥7 storeys with ≥2 units. Care homes and hospitals of similar height too. These fall under the BSA gateway regime with substantially stricter duties.'),
        ('What&rsquo;s the golden thread?',
         'Structured information about the building maintained through design, construction and occupation. Required on higher-risk buildings under the BSA. The PD is responsible for it through the design phase.'),
        ('What if no PD is appointed?',
         'Under CDM 2015, duties default to the client personally. Under the BSA on higher-risk buildings, non-appointment can prevent gateway approvals. Non-appointment itself is a breach, enforceable by the HSE or BSR.'),
        ('Do I need to appoint the PD in writing?',
         'Yes. Both roles require written appointment. A verbal appointment or an assumption that &ldquo;the architect will handle it&rdquo; does not discharge the duty.'),
        ('What&rsquo;s a Principal Contractor?',
         'A separate CDM 2015 duty-holder role, normally held by the main contractor and appointed by the client for the construction phase. Both a PD and a PC must be appointed on any project with more than one contractor.'),
    ],
    closing='Get in touch and we&rsquo;ll confirm what applies to your project.',
),

]
