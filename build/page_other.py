from common import *
from page_services import page_hero


# ---------------------------------------------------------------- Who we serve
def build_serve():
    hero = page_hero("Who we serve", "Support across ages and stages.",
                     "Spektric works with children, adolescents, and adults — and with the families, caregivers, and professionals around them.", "spectrum")

    def group(id_, eb, c, h2, lede, paras, fits, shot, alt, rev=False, alt_bg=False):
        links = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in fits)
        text = f'''<div class="reveal">{eyebrow(eb, c)}<h2 id="{id_}-h">{h2}</h2><p class="lede">{lede}</p>{"".join(f"<p>{p}</p>" for p in paras)}
        <h3 style="font-size:1rem;margin-top:1.5rem">Often a fit for</h3><ul class="prose" style="padding-left:1.2rem;margin-bottom:0">{links}</ul></div>'''
        pic = f'<div class="reveal">{photo(shot, alt, c, "photo-tall" + (" photo-alt" if rev else ""))}</div>'
        inner = text + pic
        return f'<section class="section{" section-alt" if alt_bg else ""}" id="{id_}" aria-labelledby="{id_}-h"><div class="container split{" split-rev" if rev else ""}" style="align-items:start">{inner}</div></section>'

    s = []
    s.append(group("children", "Children", "aba", "Early skills, early clarity.",
                   "Young children learn fastest when support fits their development and their family’s daily life.",
                   ["We help children build communication, play, daily living, social, and school-readiness skills, and we help families understand what they are seeing and how to respond. When a developmental question needs answering, evaluation can provide clarity early — when it makes the biggest difference."],
                   [("ABA services", "/aba-services"), ("Developmental evaluation", "/neurology"), ("Parent support", "/mental-health")],
                   "A preschool-age child absorbed in stacking blocks on a rug, clinician at the child’s level nearby; soft daylight", "young child playing with blocks while a clinician observes"))
    s.append(group("adolescents", "Adolescents", "mh", "Independence, connection, and a voice in the plan.",
                   "Teenagers deserve care that respects their growing autonomy and takes their goals seriously.",
                   ["Whether the focus is emotional regulation, anxiety, social connection, school transitions, or building independence, adolescents are partners in their own care. We work with the teen and — with their knowledge — with the adults who support them."],
                   [("Individual therapy", "/mental-health"), ("ABA services", "/aba-services"), ("Neuropsychological evaluation", "/neurology")],
                   "A teenager walking through a school or park with earbuds in, relaxed and self-possessed; documentary style", "a teenager walking outdoors", rev=True, alt_bg=True))
    s.append(group("adults", "Adults", "neuro", "Care that takes adult life seriously.",
                   "Adults come to Spektric for therapy, for evaluation, and for skills that make daily life and work more manageable.",
                   ["That might mean psychotherapy for anxiety, mood, or a major transition; an evaluation to understand long-standing questions about attention, learning, or development; or behavioral support for independence, employment, and community participation."],
                   [("Individual therapy", "/mental-health"), ("Neuropsychological evaluation", "/neurology"), ("ABA services", "/aba-services")],
                   "An adult at a kitchen table with coffee and a notebook, morning light; composed, unposed, no clinical props", "an adult at a kitchen table in the morning"))
    s.append(group("families", "Families &amp; caregivers", "coral", "You are part of the plan.",
                   "Caregivers carry more of the day than any clinician ever will. We build support that works in your routines, not just in ours.",
                   ["Parent and caregiver training, family support, and clear, usable progress updates are part of how we work across every service. We also help families coordinate care across providers when they ask us to."],
                   [("Parent &amp; caregiver training", "/aba-services"), ("Family support", "/mental-health")],
                   "Two caregivers and a child on a couch, one caregiver laughing; lived-in living room, golden hour", "a family relaxing together on a couch", rev=True, alt_bg=True))
    s.append(group("partners", "Schools, physicians &amp; community partners", "yellow", "Referrals welcome. Coordination with consent.",
                   "We work alongside pediatricians, schools, and community organizations — with the family’s permission — so care is coherent across settings.",
                   ["Evaluation reports are written to be useful in IEP, 504, and treatment-planning conversations. When families ask us to, we coordinate with teachers, physicians, and other providers so everyone is working from the same understanding."],
                   [("Refer a client", "/contact#request"), ("Neuropsychological evaluation", "/neurology")],
                   "A pediatrician and a clinician in conversation over a desk, both engaged; clean, professional, collegial", "two professionals in conversation"))

    body = hero + "".join(s) + cta_band()
    return page("/who-we-serve", "Who We Serve",
                "Spektric serves children, adolescents, and adults, and works alongside families, caregivers, schools, and physicians. Find the right starting point.",
                body, active="/who-we-serve")


# ---------------------------------------------------------------- About
def build_about():
    hero = page_hero("About Spektric", "We understand behavior. We understand people. We build care around both.",
                     "Spektric was founded to bring behavioral, psychological, and neurodevelopmental expertise together — in one practice, around one person at a time.", "spectrum", ctas=False)

    mission = f'''
<section class="section" aria-labelledby="mission-h">
  <div class="container grid grid-3 reveal-stagger" style="--gap:2.5rem">
    <div>{eyebrow("Mission")}<h2 id="mission-h" style="font-size:clamp(1.5rem,1.2rem+1.2vw,2.1rem)">Meaningful skills. Greater independence. A better life.</h2><p>To help individuals develop meaningful skills, stronger relationships, and a better quality of life — through care that is individualized, evidence-informed, and deeply respectful of the person.</p></div>
    <div>{eyebrow("Vision")}<h2 style="font-size:clamp(1.5rem,1.2rem+1.2vw,2.1rem)">Every person seen whole.</h2><p>A behavioral healthcare experience where every person is seen as a whole person, every plan is built around a real life, and progress is measured by what matters.</p></div>
    <div>{eyebrow("The name")}<h2 style="font-size:clamp(1.5rem,1.2rem+1.2vw,2.1rem)">Why “Spektric.”</h2><p>A spectrum is not a line from less to more. It is a full range of strengths, needs, abilities, and possibilities, unique to each person. Our name — and the spectrum line that runs through this site — is a reminder to look at the whole range.</p></div>
  </div>
</section>'''

    approach = f'''
<section class="section section-alt" aria-labelledby="approach-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Clinical approach")}
      <h2 id="approach-h">How we practice.</h2>
      <p class="lede">Four commitments hold across every service and every clinician.</p>
    </div>
    <div class="defs reveal-stagger">
      <div class="def" data-c="aba"><h3>Individualized</h3><p>Assessment comes before intervention. Goals are written with the person and family and reflect the settings where skills must actually work.</p></div>
      <div class="def" data-c="mh"><h3>Evidence-informed</h3><p>We use approaches grounded in established behavioral and psychological science — and we measure whether they are working for this person.</p></div>
      <div class="def" data-c="neuro"><h3>Collaborative</h3><p>Families, caregivers, schools, and physicians are partners. With consent, we coordinate so that care is coherent across settings.</p></div>
      <div class="def"><h3>Ethical</h3><p>We recommend only what we believe will help, we say so when something else would serve you better, and we protect privacy and dignity at every step.</p></div>
    </div>
  </div>
</section>'''

    team = f'''
<section class="section" aria-labelledby="team-h">
  <div class="container">
    {section_head("Leadership", "The people behind the practice.", "Clinical, operational, and compliance leadership under one roof.")}
    <div class="grid grid-3 reveal-stagger">
      <article class="team-card">
        <picture><source srcset="/assets/img/team/alina.webp" type="image/webp"><img src="/assets/img/team/alina.jpg" alt="Alina Vitali, Chief Executive Officer of Spektric LLC" width="675" height="900" loading="lazy"></picture>
        <h3>Alina Vitali</h3>
        <p class="creds">MSW, LMHC</p>
        <p class="role">Chief Executive Officer</p>
        <p>{ph("SHORT BIOGRAPHY — background, clinical focus, and what drew her to this work. 60–90 words.")}</p>
      </article>
      <article class="team-card">
        <picture><source srcset="/assets/img/team/sheryl.webp" type="image/webp"><img src="/assets/img/team/sheryl.jpg" alt="Sheryl Mayoz, Chief Financial Officer of Spektric LLC" width="672" height="900" loading="lazy"></picture>
        <h3>Sheryl Mayoz</h3>
        <p class="creds">RN, MBA, LHRM, CHC, CCA</p>
        <p class="role">Chief Financial Officer</p>
        <p>{ph("SHORT BIOGRAPHY — background, operational and compliance focus, and what drew her to this work. 60–90 words.")}</p>
      </article>
      <div class="stack">
        {ph_block("Additional clinicians", "Add team members here as they join, using the same card format. Publish names and credentials only once verified.")}
        {ph_block("Clinical team &amp; licensure", "Insert the licensed clinicians who deliver and supervise each service line, with state licensure and board certifications.")}
        {ph_block("Professional affiliations", "Insert verified memberships or affiliations, if any. Remove this block otherwise.")}
      </div>
    </div>
  </div>
</section>'''

    commitments = f'''
<section class="section section-alt" aria-labelledby="commit-h">
  <div class="container">
    {section_head("Our commitments", "What we promise.")}
    <div class="grid grid-3 reveal-stagger">
      <div class="card card-flat"><h3>To families</h3><p>Plain language, honest updates, and a real seat at the table in every decision about care.</p></div>
      <div class="card card-flat"><h3>To ethical practice</h3><p>Recommendations based on assessment and evidence, never on what is convenient or billable.</p></div>
      <div class="card card-flat"><h3>To individualized care</h3><p>No template plans. No one-size-fits-all programs. Care that starts with the person every time.</p></div>
    </div>
  </div>
</section>'''

    body = hero + mission + approach + team + commitments + cta_band()
    schema = [{"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about", "name": "About Spektric LLC", "about": {"@id": SITE + "/#organization"}}]
    return page("/about", "About Spektric",
                "Spektric brings ABA, neuropsychological evaluation, and psychotherapy together in one practice. Learn about our mission, clinical approach, and leadership.",
                body, active="/about", schema=schema)


# ---------------------------------------------------------------- FAQ
FAQ_ALL = [
    ("What is ABA?", "<p>Applied Behavior Analysis (ABA) is a therapeutic approach grounded in the science of learning and behavior. It is used to build meaningful skills — communication, daily living, social connection, independence — and to reduce barriers that get in the way of learning and participation. At Spektric, ABA is individualized, data-informed, and centered on the person’s quality of life.</p>"),
    ("Who can benefit from ABA?", "<p>ABA is most often associated with autism, but it can support a range of developmental, learning, and behavioral needs across ages. Whether it is the right fit depends on the person, their goals, and a careful assessment — not on a diagnosis alone. We will tell you candidly if we think a different service would serve you better.</p>"),
    ("What is a neuropsychological or developmental evaluation?", "<p>A structured assessment of how brain-based abilities — attention, memory, language, learning, executive functioning, social-emotional and adaptive skills — show up in everyday life. Results are explained in plain language and written into a report with practical recommendations for home, school, work, and treatment.</p>"),
    ("Do you provide mental health services?", "<p>Yes. Spektric offers psychotherapy and behavioral health support for children, adolescents, and adults, including individual therapy, family support, parent support, and behavioral health assessment.</p>"),
    ("What ages do you serve?", "<p>Children through adults. The specific services that fit vary by age and need — a first conversation is the quickest way to find the right starting point.</p>"),
    ("Do you accept insurance?", f"<p>Coverage varies by plan, service, and authorization requirements. Our team can help you understand your options before care begins. {ph('INSERT VERIFIED INSURANCE / PRIVATE-PAY DETAILS')}</p>"),
    ("How do I get started?", "<p>Request a brief consultation or send us a note through the <a href=\"/contact\">contact page</a>. We will talk through what you are looking for, answer questions, and outline appropriate next steps together.</p>"),
    ("What happens during an initial consultation?", "<p>A short conversation — usually by phone or video — about the person, the concern, and what a good outcome would look like. We answer questions about services, format, and logistics, and suggest a sensible next step. There is no obligation.</p>"),
    ("How is progress measured?", "<p>Through meaningful data and clinical observation tied directly to the goals in the plan. Progress is reviewed on a regular schedule and whenever the data show an unexpected trend, and plans are adjusted accordingly.</p>"),
    ("How involved are parents and caregivers?", "<p>Very. Caregiver training, coaching in everyday routines, and regular progress conversations are built into care. Skills that only work with a clinician in the room are not finished.</p>"),
    ("Do you work with schools and other providers?", "<p>Yes, with the family’s consent. We coordinate with teachers, physicians, and other providers so everyone is working from the same understanding, and our evaluation reports are written to be useful in IEP, 504, and treatment-planning conversations.</p>"),
    ("What should I do in an emergency?", "<p>If you are experiencing an emergency, call 911 or use the appropriate emergency resource. This website and its forms are not monitored for urgent needs.</p>"),
]


def build_faq():
    import re
    hero = page_hero("Questions &amp; answers", "Answers before you ask.",
                     "Plain answers to the questions families and individuals ask most. If yours is not here, reach out — we would rather you ask than wonder.", "spectrum", ctas=False)
    body = hero + f'''
<section class="section" aria-label="Frequently asked questions">
  <div class="container" style="max-width:860px">{faq(FAQ_ALL)}</div>
</section>''' + cta_band("Still have a question?", "Send it our way. A real person will answer.")
    def strip(html): return re.sub(r"<[^>]+>", "", html).replace("[", "").replace("]", "")
    schema = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in FAQ_ALL]}]
    return page("/faq", "Questions & Answers",
                "Plain answers to common questions about ABA, mental health services, neuropsychological evaluation, insurance, and getting started at Spektric.",
                body, active=None, schema=schema)


# ---------------------------------------------------------------- Legal
def legal(path, title, intro, sections, desc):
    secs = "".join(f"<h2>{h}</h2>{c}" for h, c in sections)
    body = f'''
<section class="article-hero"><div class="container">{eyebrow("Policies")}<h1>{title}</h1><p class="lede">{intro}</p><p class="article-meta">Effective date: {ph("EFFECTIVE DATE")}</p></div></section>
<section class="article-body"><div class="container"><div class="prose">{ph_block("Legal review required", "This page is a starting draft for review by Spektric’s legal counsel and compliance advisor. Replace or edit every section before launch.")}{secs}</div></div></section>'''
    return page(path, title, desc, body, noindex=False)


def build_privacy():
    return legal("/privacy", "Privacy Policy",
                 "How Spektric LLC collects, uses, and protects information submitted through this website.",
                 [("What this policy covers", "<p>This policy applies to spektric.com and the forms on it. It does not replace the Notice of Privacy Practices that applies to clinical care, which you will receive separately when services begin.</p>"),
                  ("Information you submit", "<p>When you request information or a consultation, we collect the details you provide: name, contact information, preferred contact method, the service you are interested in, and any general note you include. Please do not include medical details, diagnoses, or treatment history in website forms; we gather clinical information through secure channels after we connect.</p>"),
                  ("How we use it", "<p>To respond to your request, schedule and confirm consultations, and communicate with you about Spektric services. We do not sell personal information.</p>"),
                  ("How it is transmitted and stored", f"<p>Form submissions are delivered to Spektric by {ph('FORM SERVICE PROVIDER OR EMAIL')} and handled according to our internal policies. {ph('INSERT RETENTION PERIOD AND SAFEGUARDS')}</p>"),
                  ("Analytics and cookies", f"<p>{ph('INSERT ANALYTICS TOOL, IF ANY, AND WHAT IT COLLECTS')} You can control cookies through your browser settings.</p>"),
                  ("Third-party links", "<p>This site may link to other websites. Their privacy practices are their own.</p>"),
                  ("Children’s privacy", "<p>Website forms are intended for use by adults. Information about minors should be submitted only by a parent or legal guardian.</p>"),
                  ("Your choices", f"<p>To ask what information we hold about you, or to request correction or deletion, contact <a href=\"mailto:{EMAIL}\">{EMAIL}</a>.</p>"),
                  ("Changes", "<p>We may update this policy; the effective date above will change when we do.</p>")],
                 "Privacy policy for spektric.com — what information is collected through website forms, how it is used, and how to contact Spektric LLC with questions.")


def build_terms():
    return legal("/terms", "Terms of Use",
                 "The terms that apply to your use of spektric.com.",
                 [("Educational information only", "<p>Content on this website is general and educational. It is not medical, psychological, or behavioral advice, does not create a clinician–client relationship, and is not a substitute for individualized assessment, diagnosis, or treatment by a qualified professional.</p>"),
                  ("No emergency use", "<p>This website and its forms are not monitored for urgent needs. If you are experiencing an emergency, call 911 or use the appropriate emergency resource.</p>"),
                  ("Consultation requests", "<p>A scheduling request made through this site is a request, not a confirmed appointment, until Spektric confirms it with you directly.</p>"),
                  ("Intellectual property", "<p>The Spektric name, logo, and site content are the property of Spektric LLC and may not be reproduced without permission.</p>"),
                  ("Acceptable use", "<p>Do not use this site to submit unlawful, harmful, or misleading content, or to interfere with its operation.</p>"),
                  ("Limitation of liability", f"<p>{ph('INSERT LIMITATION-OF-LIABILITY LANGUAGE APPROVED BY COUNSEL')}</p>"),
                  ("Governing law", f"<p>{ph('INSERT GOVERNING STATE AND VENUE')}</p>"),
                  ("Contact", f"<p>Questions about these terms: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>.</p>")],
                 "Terms of use for spektric.com, including the educational nature of site content and how consultation requests work.")


def build_accessibility():
    return legal("/accessibility", "Accessibility Statement",
                 "Spektric is committed to a website that everyone can use.",
                 [("Our standard", "<p>spektric.com is designed to conform to the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA: semantic structure, keyboard operability, visible focus, sufficient color contrast, text alternatives, and respect for reduced-motion preferences.</p>"),
                  ("Known limitations", f"<p>{ph('LIST ANY KNOWN ISSUES AND PLANNED FIXES, OR REMOVE THIS SECTION')}</p>"),
                  ("Tell us if something is not working", f"<p>If any part of this site is difficult to use, email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> with the page and the problem. We will respond and work to fix it.</p>"),
                  ("Accommodations in care", "<p>If you need accommodations to access Spektric services — communication supports, interpreters, physical access, or scheduling flexibility — tell us when you reach out and we will plan for them.</p>")],
                 "Spektric LLC’s accessibility statement: our WCAG 2.2 AA commitment, how to report a problem, and how to request accommodations.")


# ---------------------------------------------------------------- 404
def build_404():
    body = f'''
<section class="section error-page"><div class="container">
  <div class="error-code" aria-hidden="true">404</div>
  <h1 style="font-size:clamp(2rem,1.5rem+2vw,3.2rem)">This page took a different path.</h1>
  <p class="lede">The page you are looking for may have moved, or the link may be out of date. Here is where to go next.</p>
  <div class="btn-row mt-2">{btn("Go to the home page", "/", "primary", None, arrow=True)}{btn("Contact us", "/contact", "ghost")}</div>
  <ul class="chips mt-3"><li><a class="chip" href="/aba-services">ABA Services</a></li><li><a class="chip" href="/mental-health">Mental Health</a></li><li><a class="chip" href="/neurology">Neurology &amp; Evaluation</a></li><li><a class="chip" href="/resources/">Resources</a></li></ul>
</div></section>'''
    return page("/404", "Page not found", "The page you requested could not be found.", body, noindex=True, canonical=SITE + "/404")
