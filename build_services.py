# Appended service-page generator: run after build_pages.py
import os, sys
sys.path.insert(0, '.')
exec(open('build_pages.py').read().split("# ---------------------------------------------------------------- write")[0])

def service_page(slug, title, strap, img, intro, includes, steps, why, faqs, guide):
    inc = '\n'.join(f'        <li>{i}</li>' for i in includes)
    stp = '\n'.join(
        f'''      <div class="step">
        <div class="step-num">0{n+1}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>''' for n, (t, d) in enumerate(steps))
    fq = '\n'.join(
        f'''      <details{" open" if n==0 else ""}>
        <summary>{q} <span class="m">+</span></summary>
        <div class="a">{a}</div>
      </details>''' for n, (q, a) in enumerate(faqs))
    ip = '\n'.join(f'        <p>{p}</p>' for p in intro)
    wp = '\n'.join(f'        <p>{p}</p>' for p in why)

    body = f'''
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> &#183; <a href="../services.html">Services</a> &#183; {title}</div>
    <h1>{title}</h1>
    <p class="lede">{strap}</p>
  </div>
</div>

<section style="padding-top:48px;">
  <div class="wrap">
    <figure class="svc-lead"><img src="{img}" alt="{title}" loading="lazy"></figure>
  </div>
</section>

<section style="padding-top:72px;">
  <div class="wrap">
    <div class="svc-layout">
      <div class="svc-main">
        <h2>What this covers</h2>
{ip}
        <h2>What you receive</h2>
        <ul class="svc-includes">
{inc}
        </ul>
        <h2>Why it matters</h2>
{wp}
      </div>
      <aside class="svc-aside">
        <div class="aside-card">
          <h3>Fixed fee, in writing</h3>
          <p>Every stage is quoted before it begins. No hourly surprises, no scope creep.</p>
          <ul>
            <li>Written quote within one working day</li>
            <li>Free initial consultation</li>
            <li>Directors lead every project</li>
          </ul>
          <a class="btn" href="../index.html#quote">Get a fixed-fee quote</a>
          <div class="aside-contact">
            <a href="tel:+442080000000">020 8000 0000</a>
            <a href="mailto:design@fadp.co.uk">design@fadp.co.uk</a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-label"><span>How it works</span></div>
    <div class="process-list">
{stp}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-label"><span>Common questions</span><a class="link" href="{guide}">Read the full guide</a></div>
    <div class="faq">
{fq}
    </div>
  </div>
</section>
'''
    return (head(f'{title} &#183; FADP Architecture, London', strap, depth=1)
            + header('services', depth=1) + body + cta_band(depth=1) + '\n' + footer(depth=1))

SERVICES = [
 dict(slug='planning-applications', title='Planning Applications',
  strap='Applications designed to be approved, not argued. We prepare, submit and manage the whole process with your council.',
  img=IMG['draw'],
  intro=[
   "Planning permission is where most projects are won or lost, and most refusals were predictable. Before we draw a line, we read your council's local plan and its recent decisions on streets like yours, so the application we submit answers the questions the case officer will actually ask.",
   "We handle householder, full and listed building consents, prepare all supporting documents, submit on your behalf, and deal with the council directly through the eight-week determination period, including any amendments the officer requests."],
  includes=[
   "Planning appraisal of your site and proposal",
   "Full drawing package to application standard",
   "Design and access or planning statement where required",
   "Submission, validation and all council correspondence",
   "Discharge of conditions after approval"],
  steps=[("Appraisal","We assess your proposal against local policy and recent decisions, and tell you honestly what will pass."),
         ("Pre-application","Where the case is finely balanced, we test it with the council first, so you know their position before committing."),
         ("Submission","We prepare the drawings and statements, submit, and manage validation and officer queries."),
         ("Decision","Approval, then discharge of conditions. If a refusal is wrong, we advise on appeal.")],
  why=[
   "A refused application costs months and thousands in redesign, and refusals sit on your property's planning history for every future application to contend with. An application grounded in policy and precedent is cheaper than a beautiful one that gets refused."],
  faqs=[
   ("How long does planning permission take?","Councils have an eight-week statutory determination period for householder applications from validation. Allow two to four weeks before that for survey and drawings. We give you a written programme at the start."),
   ("What if my application is refused?","First we establish why. Many refusals are resolved with a revised application addressing the officer's reasons, which is usually faster than an appeal. Where the refusal is wrong on policy, we advise on appealing to the Planning Inspectorate."),
   ("Do I even need planning permission?","Not always. Many extensions and lofts fall under permitted development. We check your property's planning history, conservation status and any Article 4 directions as part of the free consultation, and tell you in writing.")],
  guide='../blog/planning-permission-rear-extension.html'),

 dict(slug='feasibility-studies', title='Feasibility Studies',
  strap='What can be built, will it get planning, and roughly what will it cost. Answered for a fixed fee, before you commit to anything.',
  img=IMG['p7'],
  intro=[
   "A feasibility study is the cheapest decision you will make on the whole project. For a fixed fee, we test your site against planning policy, physical constraints and budget, and give you drawn options with an honest risk assessment.",
   "Many clients commission a study before exchanging on a property. Knowing that the side return can take a full-width extension, or that the loft cannot achieve head height, changes what the building is worth to you."],
  includes=[
   "Measured appraisal of the existing building or site",
   "Two to three drawn design options",
   "Planning risk assessment against local policy",
   "Build cost banding for each option",
   "A written recommendation you can act on, or stop with"],
  steps=[("Brief","A conversation about what you want the building to do, and the budget you are working to."),
         ("Study","We test the options against planning policy, daylight, structure and cost."),
         ("Report","Drawn options, risks and cost bands in a document you can share with lenders or partners."),
         ("Decision","Proceed with us, proceed with someone else, or stop. The study is yours either way.")],
  why=[
   "Projects fail at the start, not the end: a purchase made on wrong assumptions, a design developed against policy, a budget set without cost evidence. A study surfaces those problems while they still cost hundreds to fix rather than tens of thousands."],
  faqs=[
   ("Can I use the study to buy a property?","Yes. Pre-purchase studies are common, and we can usually turn one around inside the conveyancing window. Tell us your deadline at the first call."),
   ("Am I committed to using FADP afterwards?","No. The study is a standalone piece of work with its own fixed fee. Most clients continue with us; some use it to brief another architect or to decide not to proceed. All are fine."),
   ("What does a feasibility study cost?","It depends on the size and complexity of the site, but it is a fixed fee agreed in writing before we start, and it is quoted in your free consultation.")],
  guide='../blog/feasibility-studies-before-you-buy.html'),

 dict(slug='site-analysis', title='Site Analysis',
  strap='Orientation, daylight, trees, flood risk, boundaries and ground conditions. Established before design begins, not discovered on site.',
  img=IMG['site'],
  intro=[
   "Every site has constraints that shape what can be built: how daylight moves across it, which trees are protected, where the boundaries actually sit, what the ground will carry, whether it floods. Finding these early is unglamorous work, and it is where budgets are protected.",
   "Our site analysis produces a constraints and opportunities report that the design is then built on, so nothing in the drawings depends on an assumption we have not checked."],
  includes=[
   "Constraints and opportunities report",
   "Daylight, sunlight and overshadowing review",
   "Tree protection, flood risk and heritage screening",
   "Boundary and rights of light review",
   "Measured survey, arranged and checked"],
  steps=[("Desk study","Planning history, designations, flood maps, tree orders and utilities records."),
         ("Survey","A measured survey of the site or building, commissioned and verified by us."),
         ("Assessment","Daylight, overlooking, access and structure tested against your brief."),
         ("Report","One document of everything the design must respect, and everything it can exploit.")],
  why=[
   "Almost every expensive mid-project surprise, from a root protection area to a sewer easement, was findable at the start for a fraction of the cost. Analysis is how a fixed-fee design stays fixed."],
  faqs=[
   ("Is this included in a full appointment?","Yes. Site analysis is the first stage of every full project. It is also available standalone, for clients who want the ground truth before deciding how to proceed."),
   ("Do you arrange the measured survey?","Yes. We commission the survey, check it on receipt, and take responsibility for the accuracy of what the design is drawn on."),
   ("My site is in a conservation area. Does that change the analysis?","It adds a layer: we screen the designation, any Article 4 directions and the character appraisal, so the constraints report covers heritage from day one.")],
  guide='../blog/feasibility-studies-before-you-buy.html'),

 dict(slug='bim', title='Building Information Modelling',
  strap='Every project modelled in 3D, coordinated before tender. Clashes found on screen, where they cost nothing.',
  img=IMG['model'],
  intro=[
   "We design in a coordinated 3D model rather than flat drawings. The model holds the structure, the drainage and the services in one place, so the beam that clashes with the soil pipe is found on screen during design, not on site during construction where it becomes a variation and a delay.",
   "The model also measures itself: quantities come out accurate, which is why our tender returns price tightly and our clients rarely meet a surprise cost."],
  includes=[
   "Fully coordinated 3D model of the proposal",
   "Clash detection before tender",
   "Accurate quantities and schedules for pricing",
   "Visualisations of the design as it will be built",
   "Drawing packages generated from the single model"],
  steps=[("Model","The existing building and the proposal, built in 3D from the measured survey."),
         ("Coordinate","Structure, drainage and services resolved together, clashes closed out."),
         ("Quantify","Schedules and quantities exported for contractors to price against."),
         ("Deliver","Construction drawings issued from the model, consistent by construction.")],
  why=[
   "On a traditionally drawn project, the contractor finds the coordination problems, and every one becomes a variation priced without competition. BIM moves that discovery into design time, where fixing it is our job at no extra cost to you."],
  faqs=[
   ("Will I be able to see my project in 3D?","Yes. Walkthrough views are part of the design stages, and most clients find decisions much easier in 3D than on plan."),
   ("Does BIM cost more?","The modelling effort sits inside our fixed design fee. On balance it usually saves money, through tighter tender prices and fewer variations on site."),
   ("Do contractors need special software?","No. Contractors receive conventional drawings and schedules; the coordination benefit is baked into what they price.")],
  guide='../blog/how-bim-cuts-construction-costs.html'),

 dict(slug='listed-buildings', title='Listed Buildings',
  strap='Listed building consent, heritage statements and schedules of works, argued in the language conservation officers use.',
  img=IMG['listed'],
  intro=[
   "Altering a listed building needs listed building consent, and the test is different from ordinary planning: the question is harm to the building's significance. The officer's judgement is shaped almost entirely by the quality of the heritage statement in front of them.",
   "We prepare the statement, the schedule of works and the justification as one argument, and we deal with the conservation officer directly. Done well, listed consent is a design conversation; done badly, it is a two-year stalemate."],
  includes=[
   "Listed building consent applications",
   "Heritage statements and impact assessments",
   "Schedules of works and repairs",
   "Negotiation with conservation officers",
   "Specification of appropriate materials and methods"],
  steps=[("Understand","We research the listing, the building's history and what actually carries its significance."),
         ("Design","Proposals shaped to preserve what matters, so the application starts from agreement."),
         ("Justify","Heritage statement and schedule of works making the case in the officer's own terms."),
         ("Consent","Submission, negotiation and conditions through to a workable approval.")],
  why=[
   "Unauthorised works to a listed building are a criminal offence, and enforcement can require reversal at your cost, years later. Consent obtained properly protects you, your works and the building's value when you sell."],
  faqs=[
   ("Does everything need consent, even inside?","Almost everything that affects the building's character, inside and out, and sometimes structures in its curtilage. We establish exactly what applies to your building before any design work."),
   ("How long does listed building consent take?","The statutory period is eight weeks, but pre-application discussion with the conservation officer often front-loads the time and shortens the whole process. We plan the route case by case."),
   ("Can I modernise a listed building at all?","Usually yes, and often substantially. The skill is in locating change where significance is lowest and making the case properly. Kitchens, services and extensions are achieved in listed buildings every week.")],
  guide='../blog/listed-building-consent.html'),

 dict(slug='conservation-areas', title='Conservation Areas',
  strap='Article 4 directions, permitted development checks and applications evidenced by what your council has already approved.',
  img=IMG['p8'],
  intro=[
   "Conservation areas restrict permitted development, and many London ones carry Article 4 directions that remove more rights again, street by street. Designing here starts with knowing exactly which rights survive at your address and what the council has recently approved two doors down.",
   "Our applications in conservation areas lead with that evidence. Sympathetic does not have to mean timid; it means demonstrating that the proposal preserves or enhances the character the area is designated for."],
  includes=[
   "Article 4 and permitted development check for your address",
   "Design in context, evidenced by local precedent",
   "Street scene and townscape drawings",
   "Conservation area consent where demolition is involved",
   "Heritage input coordinated with any listed building issues"],
  steps=[("Check","Designation, Article 4 directions and the character appraisal for your street."),
         ("Precedent","What the council has approved nearby, and on what reasoning."),
         ("Design","A proposal that meets your brief inside the character tests."),
         ("Apply","Submission with the townscape evidence that makes refusal hard to justify.")],
  why=[
   "The most common conservation-area mistake is assuming permitted development still applies. Building without checking can mean enforcement and demolition of completed work. The check takes us a day and is included in the free consultation."],
  faqs=[
   ("How do I know if I am in a conservation area?","Your council's policy maps show designations and Article 4 directions. We run this check, with the planning history of your address, as part of the free consultation."),
   ("Can I still extend in a conservation area?","Usually yes. Extensions are approved in conservation areas constantly; the bar is design quality and evidence, which is exactly what an architect is for."),
   ("What is an Article 4 direction?","A direction removing specific permitted development rights in a defined area, meaning works that are normally automatic need a planning application. Many London conservation areas have one.")],
  guide='../blog/conservation-area-permitted-development.html'),

 dict(slug='principal-designer', title='Principal Designer',
  strap='The legal duty holder role under CDM 2015 and the Building Safety Act 2022, taken formally and recorded properly.',
  img=IMG['studio'],
  intro=[
   "Most construction projects are legally required to have a Principal Designer: a duty holder responsible for planning, managing and monitoring health and safety through the design phase, and, since the Building Safety Act 2022, for compliance with building regulations on relevant projects.",
   "It is a formal appointment with real liability, not a checkbox. We take the role properly, keep the risk registers and records the law requires, and make sure your project never trips on a duty nobody knew they held."],
  includes=[
   "Formal Principal Designer appointment under CDM 2015",
   "Principal Designer duties under the Building Safety Act 2022",
   "Design risk registers and coordination records",
   "Pre-construction information for contractors",
   "Higher-risk building gateway support where applicable"],
  steps=[("Appoint","The role confirmed in writing at the start, as the regulations require."),
         ("Plan","Design risks identified, recorded and designed out where possible."),
         ("Coordinate","Duties managed across every designer contributing to the project."),
         ("Hand over","The health and safety file compiled and passed to you at completion.")],
  why=[
   "If no Principal Designer is appointed, the duties default to you, the client, personally. Most homeowners have no idea this is the law. Appointing us formally moves that responsibility to professionals who carry it daily."],
  faqs=[
   ("Does my house extension really need this?","If more than one contractor will be involved, which is almost every project, CDM 2015 requires a Principal Designer to be appointed in writing. It applies to domestic projects."),
   ("Is this included in your full service?","Yes. On full appointments we take the role as standard. We also accept standalone Principal Designer appointments on projects designed by others."),
   ("What is a higher-risk building?","Broadly, residential buildings of at least 18 metres or seven storeys, which fall under the Building Safety Act gateway regime. Duties there are stricter, and we advise case by case.")],
  guide='../blog/principal-designer-explained.html'),
]

os.makedirs('services', exist_ok=True)
for s in SERVICES:
    open(f"services/{s['slug']}.html", 'w').write(service_page(**s))
    print(f"services/{s['slug']}.html", os.path.getsize(f"services/{s['slug']}.html")//1024, 'KB')
