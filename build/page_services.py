from common import *


def page_hero(eb, h1, lede, c, ctas=True, extra=""):
    b = f'<div class="btn-row">{btn("Get Started", "/contact#schedule", "primary", "page_get_started", arrow=True)}{btn("Request Information", "/contact#request", "ghost", "page_request_info")}</div>' if ctas else ""
    return f'<section class="page-hero" data-c="{c}"><div class="container">{eyebrow(eb, c)}<h1>{h1}</h1><p class="lede">{lede}</p>{b}{extra}</div></section>'


def defs(items, c):
    return '<div class="defs reveal-stagger">' + "".join(f'<div class="def" data-c="{c}"><h3>{t}</h3><p>{p}</p></div>' for t, p in items) + '</div>'


# ---------------------------------------------------------------- ABA
def build_aba():
    hero = page_hero("ABA Services", "ABA built around the person — and the life they’re building.",
                     "Applied Behavior Analysis (ABA) uses the science of learning and behavior to build meaningful skills and reduce barriers to learning. At Spektric, it is delivered with precision, warmth, and a clear view of what matters in each person’s life.", "aba")

    individualized = f'''
<section class="section" aria-labelledby="ind-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Individualized ABA", "aba")}
      <h2 id="ind-h">No two plans look alike.</h2>
      <p class="lede">A program is only as good as its understanding of the person it serves. That is why every plan starts with listening, observing, and asking what a good outcome would actually look like in this life.</p>
      <p>From there, each element of care is deliberately chosen and continuously checked against the data — not inherited from a template.</p>
    </div>
    {defs([("Assessment", "Structured observation, skills assessment, and conversation with the family establish where the person is now and what matters most."),
           ("Treatment planning", "Goals are written with the individual and family, based on assessment findings, developmental stage, and the settings where skills need to work."),
           ("Data-informed intervention", "Teaching strategies are selected to fit the learner, then measured continuously so decisions rest on evidence rather than impression."),
           ("Ongoing clinical decision-making", "Supervising clinicians review progress regularly and adjust the plan when the data say it is time — including when a goal is complete.")], "aba")}
  </div>
</section>'''

    skills = [("Communication", "aba"), ("Functional communication", "aba"), ("Social skills", "aba"), ("Daily living skills", "aba"), ("Adaptive behavior", "aba"), ("Functional independence", "aba"),
              ("School-readiness skills", "aba"), ("Community skills", "aba"), ("Emotional regulation", "aba"), ("Coping skills", "aba"), ("Problem solving", "aba"), ("Parent &amp; caregiver training", "aba")]
    skill_dev = f'''
<section class="section section-alt" aria-labelledby="skills-h">
  <div class="container">
    <div class="section-head-row" style="margin-bottom:clamp(2rem,4vw,3rem)">
      {section_head("Skill development", "Skill areas we address.", "Goals are chosen with the individual and family based on assessment — not drawn from a checklist. These are the areas we most often work in.")}
    </div>
    <ul class="chips reveal-stagger" style="gap:.7rem">{"".join(f'<li class="chip" data-c="{c}" style="font-size:1rem;padding:.75rem 1.15rem">{s}</li>' for s, c in skills)}</ul>
    <p class="small mt-2">Skill areas are adjusted to the person’s age, developmental stage, and priorities. Adults, for example, may focus on independence, employment-related skills, and community participation.</p>
  </div>
</section>'''

    approach = f'''
<section class="section" aria-labelledby="appr-h">
  <div class="container split split-rev" style="align-items:start">
    <div class="reveal">{photo("A clinician and child side by side at a low table, the child reaching for a toy; clinician’s attention on the child, not the camera", "clinician and child working side by side", "aba", "photo-tall")}</div>
    <div class="reveal">
      {eyebrow("Our approach", "aba")}
      <h2 id="appr-h">Good goals share six qualities.</h2>
      <p class="lede">If a goal doesn’t meet all six, we rewrite it.</p>
      <div class="features features-2">
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Individualized</h3><p>Built for this person, in this family, in these settings.</p></div>
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Functional</h3><p>Useful in daily life, not only in the therapy room.</p></div>
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Measurable</h3><p>Defined clearly enough that progress can be seen.</p></div>
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Meaningful</h3><p>Chosen because it matters to the person and family.</p></div>
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Developmentally appropriate</h3><p>Matched to the person’s stage, not a chronological checklist.</p></div>
        <div class="feature"><h3 class="display" style="font-size:1.35rem">Reviewed and adjusted</h3><p>Revisited on a schedule, and changed when the data call for it.</p></div>
      </div>
    </div>
  </div>
</section>'''

    family = f'''
<section class="section section-alt" aria-labelledby="fam-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Family partnership", "aba")}
      <h2 id="fam-h">Progress that travels home.</h2>
      <p class="lede">Skills that only work with a clinician in the room are not finished. Families and caregivers are partners in the plan from the beginning.</p>
      <p>That means clear explanations of what we are teaching and why, practical coaching in everyday routines, and regular conversations about what is working and what needs to change. Caregiver involvement is not an add-on — it is how generalization happens.</p>
      <ul class="prose" style="padding-left:1.2rem">
        <li>Caregiver training built into the plan, at a pace that fits the family</li>
        <li>Strategies designed for real routines: mealtimes, mornings, transitions, bedtime</li>
        <li>Progress reviews in plain language, with data you can actually use</li>
        <li>Coordination with schools and other providers when you ask us to</li>
      </ul>
    </div>
    <div class="reveal">{photo("A parent practicing a routine with their child in the family kitchen, clinician observing from the side; candid, warm", "parent and child practicing a routine at home", "aba", "photo-alt")}</div>
  </div>
</section>'''

    progress = f'''
<section class="section" aria-labelledby="prog-h">
  <div class="container">
    {section_head("Progress that matters", "We count what counts.", "Data are meaningful only when they describe real outcomes — a first conversation, a calmer morning, a skill used without prompting in a new place. This is the pathway every plan follows.", "aba")}
    <div class="card card-flat" style="padding:clamp(1.25rem,3vw,2.5rem) clamp(1rem,2.5vw,2rem)">{pathway()}</div>
    <div class="grid grid-3 mt-3 reveal-stagger">
      <div><h3 style="font-size:1.2rem">Meaningful data</h3><p class="small">We measure what the person is learning to do, not just what they are learning to stop. Data collection is built around the goals, not the other way around.</p></div>
      <div><h3 style="font-size:1.2rem">Ongoing evaluation</h3><p class="small">Plans are reviewed on a regular schedule and whenever the data show an unexpected trend — up or down.</p></div>
      <div><h3 style="font-size:1.2rem">Outcome-focused</h3><p class="small">The measure of success is the person’s quality of life, independence, and participation — at home, at school, at work, and in the community.</p></div>
    </div>
  </div>
</section>'''

    fit = f'''
<section class="section section-alt" aria-labelledby="fit-h">
  <div class="container split split-even" style="align-items:start">
    <div class="reveal">
      {eyebrow("Is ABA the right fit?", "aba")}
      <h2 id="fit-h">Not always — and we will say so.</h2>
      <p class="lede">ABA is one tool among several. Whether it is appropriate depends on the person, their goals, and a careful assessment, not on a diagnosis alone.</p>
      <p>Sometimes the right first step is a mental health service, an evaluation, or a referral to someone else entirely. A short conversation is the fastest way to find out.</p>
      <div class="btn-row">{btn("Talk With Us", "/contact#schedule", "primary", "aba_fit_cta", arrow=True)}</div>
    </div>
    <div class="stack reveal">
      {ph_block("Provider credentials", "Insert who delivers and supervises ABA services at Spektric (for example, the supervision structure and relevant certifications). Do not publish credentials until verified.")}
      {ph_block("Service settings", "Insert verified service settings (clinic, home, school, community, telehealth) and service area.")}
      {ph_block("Ages served for ABA", "Spektric serves children through adults. Insert any age ranges that apply specifically to ABA services, if different.")}
    </div>
  </div>
</section>'''

    body = hero + individualized + skill_dev + approach + family + progress + fit + cta_band("Learn whether ABA is a fit.", "Tell us a little about the person and what you are hoping for. We will tell you candidly what we recommend.")
    schema = [{"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "Applied Behavior Analysis (ABA)", "provider": {"@id": SITE + "/#organization"},
               "url": SITE + "/aba-services", "description": "Individualized, evidence-based ABA services for children, adolescents, and adults."}]
    return page("/aba-services", "ABA Services",
                "Individualized, evidence-based Applied Behavior Analysis for children, adolescents, and adults — focused on communication, independence, and quality of life.",
                body, active="/aba-services", schema=schema)


# ---------------------------------------------------------------- Mental health
def build_mh():
    hero = page_hero("Mental Health Services", "Mental health care should feel personal — not transactional.",
                     "Psychotherapy and behavioral health support for children, adolescents, and adults, shaped by who you are, what you are facing, and what you want to change.", "mh")

    services = f'''
<section class="section" aria-labelledby="mhs-h">
  <div class="container">
    {section_head("Services", "How we can help.", "Services are matched to the person and reviewed together as needs change.", "mh")}
    <div class="grid grid-2 reveal-stagger">
      <article class="card card-service" data-c="mh"><h3>Individual therapy</h3><p>One-to-one psychotherapy for children, adolescents, and adults. Sessions are paced to the person, with clear goals you set together with your clinician.</p></article>
      <article class="card card-service" data-c="mh"><h3>Family support</h3><p>Support for families navigating stress, change, or a new diagnosis — strengthening communication and the relationships that carry a person through hard seasons.</p></article>
      <article class="card card-service" data-c="mh"><h3>Parent support</h3><p>Practical, non-judgmental guidance for parents and caregivers: understanding behavior, responding with consistency, and caring for yourself along the way.</p></article>
      <article class="card card-service" data-c="mh"><h3>Behavioral health assessment</h3><p>A structured look at emotional, behavioral, and functional concerns to clarify what is happening and which supports are likely to help.</p></article>
    </div>
    <div class="mt-2">{ph_block("Confirm service list &amp; provider credentials", "Edit this list to reflect exactly the mental health services Spektric offers, the ages covered, and the licensed clinicians who provide them.")}</div>
  </div>
</section>'''

    areas = ["Anxiety-related concerns", "Depression-related concerns", "Trauma-related concerns", "Adjustment difficulties", "Life transitions", "Emotional regulation", "Coping skills", "Behavioral concerns"]
    focus = f'''
<section class="section section-alt" aria-labelledby="focus-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Areas of focus", "mh")}
      <h2 id="focus-h">Common reasons people reach out.</h2>
      <p class="lede">If what you are experiencing is not on this list, ask anyway. We will tell you candidly whether we are the right fit — or help you find someone who is.</p>
      <ul class="chips" style="gap:.7rem">{"".join(f'<li class="chip" data-c="mh" style="font-size:1rem;padding:.75rem 1.15rem">{a}</li>' for a in areas)}</ul>
    </div>
    <div class="reveal">{photo("Two chairs angled toward each other in a softly lit room, a plant, a window; calm and private, no people", "a calm therapy room with two chairs", "mh", "photo-tall")}</div>
  </div>
</section>'''

    commit = f'''
<section class="section" aria-labelledby="commit-h">
  <div class="container">
    {section_head("Our commitment", "What you can expect from us.", None, "mh")}
    <div class="features features-4 reveal-stagger">
      <div class="feature"><h3 class="display">Individualized</h3><p>Treatment reflects your goals, your history, your culture, and your pace.</p></div>
      <div class="feature"><h3 class="display">Respectful</h3><p>You are the expert on your own life. We bring clinical training; you bring everything else.</p></div>
      <div class="feature"><h3 class="display">Evidence-informed</h3><p>Approaches are grounded in established psychological science and adapted thoughtfully to you.</p></div>
      <div class="feature"><h3 class="display">Collaborative</h3><p>Goals and progress are reviewed together. You will never wonder what the plan is.</p></div>
    </div>
  </div>
</section>'''

    expect = f'''
<section class="section section-alt" aria-labelledby="expect-h">
  <div class="container">
    {section_head("What to expect", "The first few steps.", "Starting therapy should not feel like a leap. Here is how it usually goes.", "mh")}
    {steps([("A first conversation", "A brief call to understand what you are looking for and answer questions about fit, format, and logistics."),
            ("An initial appointment", "Time to talk through your history, concerns, and hopes for therapy — at whatever depth feels right."),
            ("A plan, together", "You and your clinician agree on goals and a way of working, including how often to meet."),
            ("Ongoing sessions", "Regular sessions focused on your goals, with room to adjust as life changes."),
            ("Regular check-ins", "Progress is reviewed openly, and the plan changes when it should — including when it is time to finish.")])}
  </div>
</section>'''

    safety = f'''
<section class="section-tight" aria-label="Important notice">
  <div class="container">{notice(EMERGENCY + " Information on this page is educational and does not constitute a diagnosis or individualized clinical advice.", "urgent", "!")}</div>
</section>'''

    body = hero + services + focus + commit + expect + safety + cta_band("Start with a conversation.", "Tell us a little about what you are looking for. We will help you decide on a sensible first step.")
    schema = [{"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "Psychotherapy and mental health services", "provider": {"@id": SITE + "/#organization"},
               "url": SITE + "/mental-health", "description": "Individual therapy, family support, parent support, and behavioral health assessment for children, adolescents, and adults."}]
    return page("/mental-health", "Mental Health Services",
                "Personal, evidence-informed psychotherapy for children, teens, and adults: individual therapy, family and parent support, and behavioral health assessment.",
                body, active="/mental-health", schema=schema)


# ---------------------------------------------------------------- Neurology & evaluation
def build_neuro():
    hero = page_hero("Neurology &amp; Evaluation", "Clarity about how a person thinks, learns, and develops.",
                     "Neuropsychological and developmental evaluation gives individuals, families, and care teams a clearer picture of strengths and needs — and a stronger foundation for the plan that follows.", "neuro")

    what = f'''
<section class="section" aria-labelledby="eval-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Neuropsychological &amp; developmental evaluation", "neuro")}
      <h2 id="eval-h">What an evaluation looks at.</h2>
      <p class="lede">An evaluation examines how brain-based abilities show up in everyday life — not just in a testing room.</p>
      <p>Using standardized measures, observation, history, and input from the people who know the person best, the evaluating clinician builds a profile of strengths and areas of need, then translates it into practical recommendations for home, school, work, and treatment.</p>
      <p>For young children, developmental evaluation focuses on milestones, early communication, play, and learning, and on identifying supports early.</p>
    </div>
    <div class="reveal">
      <h3 style="font-size:1.1rem;margin-bottom:1rem">Areas commonly assessed</h3>
      <ul class="chips" style="gap:.7rem">{"".join(f'<li class="chip" data-c="neuro" style="font-size:1rem;padding:.75rem 1.15rem">{a}</li>' for a in ["Attention &amp; focus", "Executive functioning", "Memory &amp; learning", "Language &amp; communication", "Visual-spatial skills", "Processing speed", "Academic skills", "Social-emotional functioning", "Adaptive &amp; daily living skills", "Developmental milestones"])}</ul>
      <p class="small mt-2">The specific measures used depend on the referral question, the person’s age, and what will be most useful to answer it.</p>
    </div>
  </div>
</section>'''

    helps = f'''
<section class="section section-alt" aria-labelledby="helps-h">
  <div class="container">
    {section_head("Why evaluate", "What an evaluation can help with.", None, "neuro")}
    <div class="grid grid-3 reveal-stagger">
      <div class="card card-flat"><h3 style="font-size:1.2rem">Clarifying the picture</h3><p class="small">When clinically appropriate, an evaluation can clarify a diagnostic question or rule one out — and describe the person far more fully than a label does.</p></div>
      <div class="card card-flat"><h3 style="font-size:1.2rem">Guiding treatment</h3><p class="small">Findings inform ABA and psychotherapy planning, so services target the right skills in the right order.</p></div>
      <div class="card card-flat"><h3 style="font-size:1.2rem">Supporting school planning</h3><p class="small">A clear report helps families and schools plan supports, accommodations, and IEP or 504 conversations.</p></div>
      <div class="card card-flat"><h3 style="font-size:1.2rem">Establishing a baseline</h3><p class="small">A documented starting point makes it possible to track development and response to services over time.</p></div>
      <div class="card card-flat"><h3 style="font-size:1.2rem">Informing decisions</h3><p class="small">Families and adults use results to make decisions about services, educational paths, and workplace needs.</p></div>
      <div class="card card-flat"><h3 style="font-size:1.2rem">Answering a specific question</h3><p class="small">Evaluations are most useful when they start with a clear question. We help define it before testing begins.</p></div>
    </div>
  </div>
</section>'''

    process = f'''
<section class="section" aria-labelledby="process-h">
  <div class="container">
    {section_head("The process", "From first question to written report.", "Each step is explained in advance, so there are no surprises for the person being evaluated — or the people supporting them.", "neuro")}
    {steps([("Intake conversation", "We discuss the referral question, history, and goals, and confirm that an evaluation is likely to be useful."),
            ("Testing sessions", "One or more sessions, paced to the person, using measures selected for the question at hand."),
            ("Scoring &amp; interpretation", "Results are scored and interpreted in the context of history, observation, and input from others."),
            ("Feedback session", "Findings are explained in plain language, with time for questions."),
            ("Written report", "A report with recommendations you can share with schools, physicians, and treatment providers.")])}
  </div>
</section>'''

    scope = f'''
<section class="section section-alt" aria-labelledby="scope-h">
  <div class="container split split-even" style="align-items:start">
    <div class="reveal">
      {eyebrow("Additional neurology services", "neuro")}
      <h2 id="scope-h">Scope being finalized.</h2>
      <p class="lede">Spektric is finalizing the full scope of its neurology offering. Neuropsychological and developmental evaluation is confirmed; additional services will be described here once they are.</p>
      <p>If you have a question about a neurology-related need not listed on this page, ask — we will tell you what we can offer and where else to look.</p>
    </div>
    <div class="stack reveal">
      {ph_block("Additional neurology services — to be confirmed", "Describe additional neurology services here once confirmed (for example, consultation, specific assessments, or coordination with medical neurology). Remove this block if no additional services are offered.")}
      {ph_block("Evaluating clinician credentials", "Insert the licensed professional(s) who conduct evaluations and their credentials. Do not publish until verified.")}
      {ph_block("Ages served for evaluation", "Spektric serves children through adults. Insert any age ranges specific to evaluation services, if different.")}
    </div>
  </div>
</section>'''

    fit = f'''
<section class="section-tight" aria-label="A note on fit">
  <div class="container">{notice("<strong>An evaluation is not always the right first step.</strong> Sometimes a conversation, a screening, or starting services is more useful than formal testing. We will help you decide, and we will not recommend an evaluation that is unlikely to change the plan.", "info", "i")}</div>
</section>'''

    body = hero + what + helps + process + scope + fit + cta_band("Not sure whether an evaluation would help?", "Tell us the question you are trying to answer. We will help you decide on a sensible next step.")
    schema = [{"@context": "https://schema.org", "@type": "MedicalTest", "name": "Neuropsychological and developmental evaluation", "url": SITE + "/neurology",
               "description": "Comprehensive evaluation of attention, executive functioning, memory, language, learning, and social-emotional and adaptive functioning for children, adolescents, and adults."}]
    return page("/neurology", "Neurology & Neuropsychological Evaluation",
                "Neuropsychological and developmental evaluation for children, adolescents, and adults: clarity about strengths and needs to guide treatment and school planning.",
                body, active="/neurology", schema=schema)
