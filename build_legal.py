"""Builds terms.html and privacy.html.
Imports shared head/header/footer from build_pages."""
import importlib.util, os

spec = importlib.util.spec_from_file_location("bp", os.path.join(os.path.dirname(__file__), "build_pages.py"))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

FIRM = "Fa Design Partners Limited"
TRADING = "FADP Architecture"
CONO = "17331773"
ADDR = "66 Paul Street, London EC2A 4NA"
EMAIL = "design@fadp.co.uk"
UPDATED = "August 2026"


def clause(n, title, paras):
    body = "\n".join(f"      <p>{p}</p>" for p in paras)
    return f"""    <div class="clause" id="c{n}">
      <h3><span class="c-num">{n}</span>{title}</h3>
{body}
    </div>"""


# ============================================================ TERMS
terms_clauses = [
    (1, "Who we are and the basis of our appointment", [
        f"These terms govern the provision of services by <strong>{FIRM}</strong>, a company registered in England and Wales (company number {CONO}), whose registered office is {ADDR}, trading as {TRADING} (&ldquo;we&rdquo;, &ldquo;us&rdquo;, &ldquo;the practice&rdquo;). Your contract is with the company and not with any individual director or employee.",
        "<strong>Status.</strong> The practice provides architectural design, planning and related consultancy services. Neither the practice nor its directors are registered with the Architects Registration Board, and we do not offer services as, or hold ourselves out to be, registered architects within the meaning of the Architects Act 1997. We make this clear at the outset so that you can make an informed decision before appointing us. Where a project requires input from a registered architect, a chartered engineer, a chartered surveyor or any other regulated professional, we will tell you and that person will be appointed separately.",
        "No appointment arises until we have issued a written fee proposal and you have accepted it in writing, or you have otherwise instructed us to proceed in writing. These terms apply to that appointment and to every subsequent stage unless we agree otherwise in writing.",
    ]),
    (2, "Services and scope", [
        "The services we will provide are those set out in our fee proposal for the relevant stage, and only those. Anything not expressly listed is excluded.",
        "Unless our proposal states otherwise, the following are <strong>not</strong> included: structural engineering design and calculations; measured, topographical, asbestos, drainage or condition surveys; ecology, arboricultural, acoustic, transport, flood risk or energy assessments; party wall surveying and awards; building control or planning application fees; quantity surveying and cost consultancy; contract administration; and interior specification or furniture procurement. Where any of these are required we will say so, and they will be the subject of a separate appointment and fee, whether with us or with a third party.",
        "Work proceeds in stages. Each stage is quoted, agreed and confirmed in writing before it begins, and no stage commences until the preceding stage has been approved by you.",
    ]),
    (3, "Variations", [
        "If you ask us to change the brief, the scope or the deliverables, or if a change is required by a planning authority, building control body, statutory undertaker or other third party, we will confirm in writing the effect on the fee and the programme before carrying out the additional work.",
        "We are not obliged to carry out varied work until the variation has been agreed in writing. Abortive work arising from a change of instruction, a change of brief, or information that later proves to be inaccurate will be chargeable.",
    ]),
    (4, "Fees, expenses and payment", [
        "Fees are fixed for each stage and stated in the fee proposal. Fees exclude VAT, which will be added at the prevailing rate where the practice is registered for VAT, and exclude disbursements and third-party fees, which are recharged at cost.",
        "Invoices are payable within 14 days of the invoice date unless stated otherwise. Where payment is not made by the due date we may charge interest, and in the case of a business client we reserve the right to claim interest and recovery costs under the Late Payment of Commercial Debts (Interest) Act 1998.",
        "If an invoice remains unpaid, we may suspend work on giving you seven days&rsquo; written notice. We will not be liable for any delay, cost or consequence arising from a suspension properly made under this clause. Work will resume once payment is received, and the programme will be adjusted accordingly.",
    ]),
    (5, "Your right to cancel", [
        "Where you are a consumer and the contract is concluded away from our premises or at a distance &mdash; for example at your home, by email, by telephone or by video call &mdash; you have the right to cancel within 14 days of the day the contract is made, without giving a reason and without liability, except as set out below.",
        "To cancel, you need only tell us clearly in writing, by post to the address above or by email to " + EMAIL + ", before the 14-day period expires. You may use the model cancellation form we provide with our fee proposal, but you are not required to.",
        "<strong>If you want us to start within the cancellation period</strong>, you must request this expressly in writing. If you then cancel, you remain liable for a proportionate amount for the work performed up to the point you told us you wished to cancel. If you do not make such a request, we will not begin work until the cancellation period has expired.",
        "We will refund any sum you have paid, less any proportionate amount properly due under this clause, within 14 days of being told of the cancellation.",
    ]),
    (6, "Your obligations", [
        "You agree to provide, promptly and without charge, the information we reasonably require: title documents, deeds and plans, existing drawings, survey information, reports in your possession, details of covenants, easements, rights of way and rights of light, and details of any dispute affecting the property.",
        "We are entitled to rely on the accuracy and completeness of information you or your other advisers supply, and we are not responsible for verifying it independently unless our proposal expressly says we will.",
        "You agree to give decisions and approvals within a reasonable time, and to notify us promptly of anything that affects the brief, the budget or the programme. You warrant that you have the authority to instruct works to the property, and you will hold us harmless in respect of any claim arising from a lack of such authority.",
    ]),
    (7, "Third parties and other consultants", [
        "Where other consultants, specialists or contractors are appointed, they are appointed by you and are responsible to you for their own services, whether or not we recommended them or coordinated their work. We are not liable for their acts, omissions, defaults or insolvency.",
        "Where we coordinate the work of others, our responsibility is limited to the exercise of reasonable skill and care in that coordination, and does not extend to the correctness of their design, advice or workmanship.",
        "Nothing we do constitutes legal, financial, tax, valuation or investment advice, and you should take advice from an appropriately qualified adviser on those matters.",
    ]),
    (8, "Approvals, consents and outcomes", [
        "The grant of planning permission, listed building consent, conservation area consent, prior approval, building regulations approval or any other consent is a matter for the relevant authority and lies outside our control.",
        "We will exercise reasonable skill and care in preparing and pursuing applications, but we give no warranty, guarantee or representation that any application will succeed, that it will succeed within a particular period, or that it will succeed without conditions. Statements on our website or in discussion about typical timescales or likely outcomes are indicative only and do not form part of this contract.",
        "Cost information we provide is an estimate for guidance based on the information available at the time. It is not a quotation, a tender price or a cost guarantee, and construction costs are determined by the market and by the contractor you appoint.",
    ]),
    (9, "Standard of care and limitation of liability", [
        "We will perform our services with the reasonable skill and care to be expected of a competent provider of services of a similar type. We do not accept, and nothing in these terms shall be construed as, any fitness for purpose obligation, absolute obligation, guarantee or warranty of result.",
        "<strong>Nothing in these terms limits or excludes our liability for death or personal injury caused by our negligence, for fraud or fraudulent misrepresentation, or for any other liability which cannot lawfully be limited or excluded. Nothing in these terms affects your statutory rights as a consumer.</strong>",
        "Subject to the paragraph above, our total liability to you arising out of or in connection with this appointment, whether in contract, tort (including negligence), breach of statutory duty or otherwise, shall not exceed the greater of (a) the total fees paid to us under the appointment, or (b) such sum as is recoverable under our professional indemnity insurance in respect of the claim, up to the limit of indemnity in force at the time.",
        "Subject to the second paragraph of this clause, we shall not be liable for loss of profit, loss of rent, loss of opportunity, loss of anticipated saving, loss arising from delay, or any indirect or consequential loss.",
        "<strong>Net contribution.</strong> Our liability shall be limited to the proportion of your loss which it would be just and equitable for us to pay having regard to the extent of our responsibility, on the assumption that all other parties who have any responsibility for that loss have provided contractual undertakings on terms no less onerous than these, have paid to you such proportion as is just and equitable for them to pay, and are not prevented from doing so by any limitation, exclusion or insolvency.",
        "No claim may be brought against us after the expiry of six years from completion of our services, or such shorter period as may be agreed in writing.",
        "No claim may be brought against any director or employee of the practice personally. You agree to pursue any claim against the company alone.",
    ]),
    (10, "Insurance", [
        "We maintain professional indemnity insurance and public liability insurance appropriate to the services we provide. Details of the level of cover are available on request.",
        "We are not obliged to maintain professional indemnity insurance after the appointment ends beyond the period required by law or such period as we consider reasonable, and our obligation to maintain cover is subject to it remaining available on commercially reasonable terms.",
    ]),
    (11, "Copyright and licence to use our drawings", [
        "We retain copyright and all other intellectual property rights in all drawings, models, specifications, reports and other documents we produce, in accordance with the Copyright, Designs and Patents Act 1988.",
        "<strong>Subject to payment in full of all fees and expenses properly due</strong>, you are granted a licence to copy and use those documents for the purposes of constructing, extending, maintaining, letting, advertising and selling the property to which they relate. That licence does not extend to any other site, to repeat construction, or to use by any other party.",
        "Where fees remain outstanding, no licence to use our documents arises and any purported use will be an infringement of copyright.",
        "We accept no liability for any use of our documents for a purpose other than that for which they were prepared, for use after termination of the appointment, or where they have been amended by anyone other than us.",
        "We may photograph completed work and reproduce images and drawings of the project for our portfolio, website, awards submissions and marketing, unless you tell us in writing that you would prefer us not to.",
    ]),
    (12, "Site inspections and safety", [
        "Where our appointment includes inspection of works in progress, inspections are periodic and visual. They are made to satisfy ourselves generally as to progress and quality against the design intent, and they do not constitute continuous supervision, a guarantee of the contractor&rsquo;s workmanship, or a warranty that the works comply in every respect with the contract documents.",
        "Responsibility for construction methods, sequencing, site safety and compliance with the Construction (Design and Management) Regulations 2015 on site rests with the contractor.",
        "Where we accept appointment as a duty holder, our duties are those imposed by the relevant regulations and no more, and such an appointment must be made expressly in writing.",
    ]),
    (13, "Suspension and termination", [
        "Either party may terminate the appointment on 14 days&rsquo; written notice. We may terminate or suspend immediately where fees remain unpaid after notice, where you are in material breach, or on your insolvency.",
        "On termination you will pay all fees for services performed to the date of termination, together with expenses properly incurred and any commitments reasonably entered into on your behalf.",
        "Termination does not affect the parties&rsquo; accrued rights, nor the clauses relating to fees, liability, copyright, confidentiality and governing law, which survive.",
    ]),
    (14, "Confidentiality and data protection", [
        "Each party will keep confidential information belonging to the other confidential, except where disclosure is required by law, by an authority, or in the proper performance of the services.",
        "We process personal data in accordance with our Privacy Policy and with the UK General Data Protection Regulation and the Data Protection Act 2018.",
    ]),
    (15, "Complaints", [
        "If you are dissatisfied, please tell us in writing at " + EMAIL + ". A director will acknowledge your complaint within five working days and give a substantive response within 21 days. We would prefer to resolve any concern directly and promptly.",
    ]),
    (16, "Disputes and governing law", [
        "If a dispute cannot be resolved through our complaints procedure, the parties will consider mediation before commencing proceedings. Nothing in this clause prevents either party from seeking urgent relief, or requires a consumer to submit a dispute exclusively to arbitration.",
        "These terms and any dispute arising out of them are governed by the law of England and Wales, and the courts of England and Wales have jurisdiction.",
    ]),
    (17, "General", [
        "These terms, together with our fee proposal, form the entire agreement between us and supersede any earlier discussion, representation or understanding, save that nothing excludes liability for fraudulent misrepresentation.",
        "No person other than the parties may enforce these terms under the Contracts (Rights of Third Parties) Act 1999.",
        "If any provision is held to be invalid or unenforceable, the remaining provisions continue in force.",
        "We may amend these terms from time to time. The terms applying to your appointment are those in force when the appointment was made.",
    ]),
]

website_clauses = [
    (1, "Use of this website", [
        f"This website is operated by {FIRM}, trading as {TRADING}. By using the site you accept these terms of use.",
        "The site is provided for general information about the practice and its services. It does not constitute professional advice and must not be relied upon as such. No client relationship arises from use of this website or from any enquiry made through it.",
    ]),
    (2, "Accuracy of content", [
        "We take care to ensure that information on this site is accurate at the time of publication, but law, policy and practice change. Guidance on planning rules, permitted development, timescales, statutory duties and costs is general in nature, is not tailored to any particular property or project, and may not be current.",
        "Indicative timescales, cost ranges and outputs generated by any tool on this site, including the fee enquiry form, are estimates for guidance only. They are not quotations, do not constitute an offer capable of acceptance, and are subject to confirmation in writing.",
        "To the fullest extent permitted by law we exclude liability for any loss arising from reliance on the content of this site. Nothing excludes liability for death or personal injury caused by negligence, or for fraud.",
    ]),
    (3, "Intellectual property", [
        "All content on this site, including text, drawings, images, layout and design, is owned by or licensed to the practice and is protected by copyright. You may view and print pages for your own use, but you may not reproduce, republish or use any part of the site commercially without our written consent.",
        "Photographs used to illustrate the site may be stock imagery and may not depict projects by the practice unless expressly captioned as such.",
    ]),
    (4, "External links", [
        "Where we link to third-party sites we do so for convenience. We do not endorse and are not responsible for their content or their privacy practices.",
    ]),
]

privacy_clauses = [
    (1, "Who is responsible for your data", [
        f"{FIRM} (company number {CONO}), trading as {TRADING}, of {ADDR}, is the data controller for personal data collected through this website and in the course of providing our services.",
        f"If you have any question about this notice or about how we handle your information, contact us at <a class=\"link\" href=\"mailto:{EMAIL}\">{EMAIL}</a>.",
    ]),
    (2, "What we collect", [
        "<strong>Information you give us.</strong> Your name, email address, telephone number, the address of the property, details of the project you are considering, your budget range and intended timescale, and anything else you choose to tell us in an enquiry or during the course of a project.",
        "<strong>Project information.</strong> In the course of an appointment we may hold title documents, plans, surveys, correspondence with authorities, photographs of the property, and correspondence with you and with other consultants.",
        "<strong>Technical information.</strong> Standard server logs may record your IP address, browser type and the pages you visit. Our website does not use advertising or tracking cookies.",
        "We do not knowingly collect special category data. Please do not send us health, biometric or similar sensitive information unless it is necessary for the project, in which case we will tell you how it will be handled.",
    ]),
    (3, "Why we use it, and our lawful basis", [
        "<strong>To respond to your enquiry and prepare a fee proposal</strong> &mdash; because you have asked us to take steps prior to entering a contract, and because we have a legitimate interest in responding to enquiries.",
        "<strong>To provide our services and administer the appointment</strong> &mdash; performance of our contract with you.",
        "<strong>To comply with legal and regulatory obligations</strong> &mdash; including tax, company law, building safety and health and safety record-keeping.",
        "<strong>To establish, exercise or defend legal claims and maintain insurance</strong> &mdash; our legitimate interest in protecting the practice.",
        "<strong>To send occasional updates about the practice</strong> &mdash; only where you have consented. You may withdraw consent at any time.",
    ]),
    (4, "Who we share it with", [
        "We share information only where it is necessary: with local planning authorities, building control bodies and statutory consultees in connection with applications; with structural engineers, surveyors, contractors and other consultants working on your project; with our professional advisers, insurers and accountants; and with IT and email providers who host our systems under contract.",
        "We do not sell personal data, and we do not share it for third-party marketing.",
        "Please note that planning applications are a matter of public record. Material submitted in support of an application, including drawings and the site address, is published by the authority on its public register.",
    ]),
    (5, "How long we keep it", [
        "Enquiries that do not become projects are kept for up to two years.",
        "Project records are kept for a minimum of six years after completion, and commonly longer, because claims relating to design and construction can be brought many years after the work is finished and we need to be able to respond to them. Records relating to statutory duties are kept for the period the relevant regulations require.",
        "Financial records are kept for six years as required for tax purposes.",
    ]),
    (6, "Where your data is held", [
        "Your data is held on systems within the United Kingdom or the European Economic Area wherever possible. Where a provider processes data outside the UK, we ensure an appropriate safeguard is in place, such as UK International Data Transfer Agreement clauses or an adequacy decision.",
    ]),
    (7, "Security", [
        "We use access controls, encrypted storage and reputable providers to protect information. No transmission over the internet is entirely secure, and you send information to us at your own risk, but we take reasonable measures to protect it once received.",
    ]),
    (8, "Your rights", [
        "You have the right to be informed about how your data is used; to request a copy of the data we hold; to have inaccurate data corrected; to request erasure where there is no continuing reason for us to hold it; to restrict or object to processing; to data portability where processing is by consent or contract and carried out by automated means; and to withdraw consent at any time where consent is the basis of processing.",
        "These rights are not absolute. We may need to retain certain records to comply with a legal obligation or to defend a claim, and we will explain if that applies.",
        f"To exercise a right, write to us at <a class=\"link\" href=\"mailto:{EMAIL}\">{EMAIL}</a>. We will respond within one month.",
        "If you are not satisfied with our response you may complain to the Information Commissioner&rsquo;s Office at ico.org.uk, or by telephone on 0303 123 1113. We would ask you to raise the matter with us first so that we have the opportunity to put it right.",
    ]),
    (9, "Cookies", [
        "This site uses only cookies that are strictly necessary for it to function, and cookies set by our font provider. We do not use analytics, advertising or profiling cookies. You can block cookies in your browser settings, though parts of the site may then not work as intended.",
    ]),
    (10, "Changes to this notice", [
        f"We may update this notice. The version published here is the one in force. It was last updated in {UPDATED}.",
    ]),
]


def build_page(title, lede, sections, filename, meta):
    parts = []
    for heading, intro, clauses in sections:
        cl = "\n".join(clause(n, t, p) for n, t, p in clauses)
        intro_html = f'      <p class="legal-intro">{intro}</p>\n' if intro else ""
        parts.append(f"""<section class="legal-section">
  <div class="wrap">
    <div class="legal-head">
      <h2>{heading}</h2>
{intro_html}    </div>
{cl}
  </div>
</section>""")
    body = f"""
<div class="page-hero legal-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &#183; {title}</div>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
    <p class="legal-date">Last updated {UPDATED}</p>
  </div>
</div>

{"".join(parts)}
"""
    html = (bp.head(f"{title} &#183; {TRADING}", meta, depth=0)
            + bp.header('', depth=0) + body + bp.footer(depth=0))
    open(os.path.join(os.path.dirname(__file__), filename), 'w').write(html)
    print(f"{filename} written")


build_page(
    "Terms",
    "The terms on which we provide our services, and the terms governing use of this website.",
    [("Terms of engagement",
      "These terms apply to every appointment unless we agree otherwise in writing. Please read clause 9, which limits our liability, and clause 5, which sets out your right to cancel.",
      terms_clauses),
     ("Website terms of use", "", website_clauses)],
    "terms.html",
    "Terms of engagement and website terms of use for FADP Architecture.")

build_page(
    "Privacy",
    "How we collect, use and protect personal information.",
    [("Privacy notice", "", privacy_clauses)],
    "privacy.html",
    "Privacy notice for FADP Architecture: what personal data we collect, why, and your rights under UK GDPR.")
