from common import *

FAQ_HOME = [
    ("What is ABA?", "<p>Applied Behavior Analysis (ABA) is a therapeutic approach grounded in the science of learning and behavior. It is used to build meaningful skills — communication, daily living, social connection, independence — and to reduce barriers that get in the way of learning and participation. At Spektric, ABA is individualized, data-informed, and centered on the person’s quality of life.</p>"),
    ("Who can benefit from ABA?", "<p>ABA is most often associated with autism, but it can support a range of developmental, learning, and behavioral needs across ages. Whether it is the right fit depends on the person, their goals, and a careful assessment — not on a diagnosis alone. We will tell you candidly if we think a different service would serve you better.</p>"),
    ("Do you accept insurance?", f"<p>Coverage varies by plan, service, and authorization requirements. Our team can help you understand your options before care begins. {ph('INSERT VERIFIED INSURANCE / PRIVATE-PAY DETAILS')}</p>"),
    ("How do I get started?", "<p>Request a brief consultation or send us a note. We will talk through what you are looking for, answer questions, and outline appropriate next steps together — which may include an assessment, a referral, or a plan to begin services.</p>"),
]


def build():
    hero = f'''
<section class="hero" aria-labelledby="hero-h">
  <div class="hero-art">{hero_art()}</div><div class="hero-art-m">{hero_art(mobile=True)}</div>
  <div class="container"><div class="hero-inner">
    {eyebrow("ABA &middot; Neurology &middot; Psychotherapy")}
    <h1 id="hero-h"><span class="line">Different minds.</span><span class="line">Meaningful progress.</span></h1>
    <p class="lede">Evidence-based ABA, neuropsychological evaluation, and psychotherapy designed around the individual — not a diagnosis. For children, adolescents, and adults.</p>
    <div class="btn-row">{btn("Get Started", "/contact#schedule", "light", "hero_get_started", arrow=True)}{btn("Explore Our Services", "#services", "ghost-light", "hero_explore")}</div>
    <ul class="hero-trust"><li>Compassionate care</li><li>Evidence-based practice</li><li>Individualized support</li></ul>
  </div></div>
</section>'''

    services = f'''
<section class="section" id="services" aria-labelledby="services-h">
  <div class="container">
    {section_head("What we do", "Three ways to begin. One standard of care.", "Behavioral, psychological, and neurodevelopmental expertise within one practice — so care can be coordinated around the person instead of split across providers.")}
    <div class="grid grid-3 reveal-stagger">
      <article class="card card-hover card-service" data-c="aba">
        {eyebrow("ABA Services", "aba")}
        <h3>Skills that matter, built with precision and warmth</h3>
        <p>Individualized behavioral support focused on communication, independence, adaptive functioning, social development, and quality of life.</p>
        <a class="text-link" data-c="aba" href="/aba-services">Explore ABA</a>
      </article>
      <article class="card card-hover card-service" data-c="mh">
        {eyebrow("Mental Health", "mh")}
        <h3>Psychotherapy shaped around you</h3>
        <p>Compassionate, evidence-informed therapy and support tailored to the individual’s needs, goals, development, and circumstances.</p>
        <a class="text-link" data-c="mh" href="/mental-health">Explore Mental Health</a>
      </article>
      <article class="card card-hover card-service" data-c="neuro">
        {eyebrow("Neurology &amp; Evaluation", "neuro")}
        <h3>Clarity about how a person thinks, learns, and develops</h3>
        <p>Neuropsychological and developmental evaluation that identifies strengths and needs — and informs the plan that follows.</p>
        <a class="text-link" data-c="neuro" href="/neurology">Explore Neurology</a>
      </article>
    </div>
  </div>
</section>'''

    philosophy = f'''
<section class="section section-alt" aria-labelledby="phil-h">
  <div class="container split">
    <div class="reveal">
      {eyebrow("Our philosophy")}
      <h2 id="phil-h">More than a diagnosis. More than a behavior.</h2>
      <p class="lede">A diagnosis describes a pattern. A behavior describes a moment. Neither one describes a person.</p>
      <p>Effective care starts by understanding the whole picture — strengths, communication, environment, relationships, emotional and developmental needs, functional skills, goals, and the family and support system around the person. Then it builds support that fits that picture, rather than asking the person to fit a program.</p>
      <p>Every plan we build is anchored to what matters in that person’s life: at home, at school, at work, and in the community.</p>
      <a class="text-link" href="/about">How we think about care</a>
    </div>
    <div class="reveal">{orbit()}</div>
  </div>
</section>'''

    why = f'''
<section class="section" aria-labelledby="why-h">
  <div class="container">
    {section_head("Why Spektric", "Care you can see working.", "Six commitments that shape every plan, every session, and every conversation with a family.")}
    <div class="features reveal-stagger">
      <div class="feature"><h3 class="display">Individualized</h3><p>Care is designed around the person, not a protocol. Goals reflect their life, their priorities, and their pace.</p></div>
      <div class="feature"><h3 class="display">Evidence-informed</h3><p>Clinical decisions are guided by established behavioral and psychological science — and by what the data say about this person.</p></div>
      <div class="feature"><h3 class="display">Measurable</h3><p>Progress is monitored with meaningful data and clinical observation, so you can see what is changing and why.</p></div>
      <div class="feature"><h3 class="display">Collaborative</h3><p>Families and caregivers are active partners. Skills are built to carry over into everyday settings.</p></div>
      <div class="feature"><h3 class="display">Human</h3><p>People are treated as individuals, not cases. Dignity and respect are part of the method, not an afterthought.</p></div>
      <div class="feature"><h3 class="display">Adaptive</h3><p>Treatment evolves as needs and goals change. What worked last season may not be what is needed next.</p></div>
    </div>
  </div>
</section>'''

    how = f'''
<section class="section section-alt" aria-labelledby="how-h">
  <div class="container">
    <div class="section-head-row" style="margin-bottom:clamp(2.5rem,5vw,4rem)">
      {section_head("How it works", "From first conversation to meaningful progress.", "Five steps, each at a human pace. You will always know what comes next.")}
      {btn("Get Started", "/contact#schedule", "primary", "how_get_started", arrow=True)}
    </div>
    {steps([("Connect", "Tell us what you’re looking for. A short conversation is enough to begin."),
            ("Understand", "We gather information and determine appropriate next steps together."),
            ("Assess", "When clinically appropriate, we conduct or coordinate an assessment."),
            ("Personalize", "We develop an individualized plan based on identified needs and goals."),
            ("Grow", "We monitor progress and adapt services over time.")])}
  </div>
</section>'''

    serve = f'''
<section class="section" aria-labelledby="serve-h">
  <div class="container">
    <div class="section-head-row" style="margin-bottom:clamp(2.5rem,5vw,4rem)">
      {section_head("Who we serve", "Support across ages and stages.")}
      <a class="text-link" href="/who-we-serve">See who we work with</a>
    </div>
    <div class="tiles reveal-stagger">
      <a class="tile" href="/who-we-serve#children">{photo("A young child and caregiver at a table with a simple picture-exchange routine; natural light, real home", "child and caregiver working together at home", "aba")}<h3>Children</h3><p>Early skill-building, communication, and developmental clarity.</p></a>
      <a class="tile" href="/who-we-serve#adolescents">{photo("A teenager mid-conversation with a clinician in a calm, uncluttered room; eye level, unposed", "teenager talking with a clinician", "mh", "photo-alt")}<h3>Adolescents</h3><p>Independence, social connection, and emotional regulation.</p></a>
      <a class="tile" href="/who-we-serve#adults">{photo("An adult in a quiet office or at a window; reflective, dignified, no clinical props", "adult in a calm setting", "neuro")}<h3>Adults</h3><p>Therapy, evaluation, and skills for work and daily life.</p></a>
      <a class="tile" href="/who-we-serve#families">{photo("Two caregivers reviewing a simple plan together at a kitchen counter; warm, collaborative", "caregivers planning together", "coral", "photo-alt")}<h3>Families &amp; Caregivers</h3><p>Training, coaching, and support that travels home.</p></a>
      <a class="tile" href="/who-we-serve#partners">{photo("A clinician and an educator in a school hallway or office, comparing notes; professional, collegial", "clinician and educator collaborating", "yellow")}<h3>Schools &amp; Partners</h3><p>Referrals and coordination with consent.</p></a>
    </div>
  </div>
</section>'''

    stories = f'''
<section class="section section-alt" aria-labelledby="stories-h">
  <div class="container split">
    <div class="reveal">
      {eyebrow("Family stories")}
      <h2 id="stories-h">Experiences, shared with permission.</h2>
      <p class="lede">We will publish the words of the people and families we work with only with their informed consent — and never in exchange for anything.</p>
      <p>Until then, this space stays empty on purpose. We would rather show nothing than something that was not freely given.</p>
    </div>
    <figure class="testimonial reveal">
      <div class="quote-mark" aria-hidden="true">&#8220;</div>
      <blockquote>{ph("CLIENT OR FAMILY TESTIMONIAL — ADD ONLY WITH WRITTEN CONSENT")}</blockquote>
      <figcaption>{ph("NAME OR INITIALS, RELATIONSHIP, SERVICE")}</figcaption>
    </figure>
  </div>
</section>'''

    insurance = f'''
<section class="section" aria-labelledby="ins-h">
  <div class="container split split-even">
    <div class="reveal">
      {eyebrow("Insurance &amp; payment")}
      <h2 id="ins-h">Understanding your coverage.</h2>
      <p class="lede">Coverage can vary by plan, service, diagnosis, authorization requirements, and location. Our team can help you understand your options before care begins.</p>
      <div class="btn-row">{btn("Talk With Our Team", "/contact#request", "primary", "insurance_cta", arrow=True)}</div>
    </div>
    <div class="stack reveal">
      {ph_block("Insurance accepted", "Insert the verified list of insurance plans Spektric accepts. Do not list a plan until the contract is active.")}
      {ph_block("Private pay", "Insert verified private-pay information, including whether a good-faith estimate is provided.")}
      {ph_block("Authorization", "Insert a short note on how authorizations are handled and what families can expect.")}
    </div>
  </div>
</section>'''

    faqs = f'''
<section class="section section-alt" aria-labelledby="faq-h">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      {eyebrow("Questions")}
      <h2 id="faq-h">Answers before you ask.</h2>
      <p class="lede">Plain answers to the questions families and individuals ask most.</p>
      <a class="text-link" href="/faq">See all questions</a>
    </div>
    <div class="reveal">{faq(FAQ_HOME)}</div>
  </div>
</section>'''

    body = hero + services + philosophy + why + how + serve + stories + insurance + faqs + cta_band()
    return page("/", "Spektric LLC — ABA, Neurology & Psychotherapy",
                "Evidence-based ABA, neuropsychological evaluation, and psychotherapy designed around the individual, not a diagnosis. For children, adolescents, and adults.",
                body, active=None)
