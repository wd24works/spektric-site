from common import *
from page_services import page_hero

CATS = [("aba", "ABA", "aba"), ("development", "Autism &amp; development", "neuro"), ("parenting", "Parenting &amp; caregiving", "aba"),
        ("mental-health", "Mental health", "mh"), ("behavior", "Behavioral skills", "aba"), ("regulation", "Emotional regulation", "mh"),
        ("communication", "Communication", "aba"), ("family", "Family resources", "mh")]
CAT_LABEL = {k: l for k, l, _ in CATS}
CAT_COLOR = {k: c for k, _, c in CATS}

ARTICLES = [
    {"slug": "what-is-aba", "title": "What is ABA? A plain-language guide", "cats": ["aba", "development"], "read": "5 min read",
     "excerpt": "What Applied Behavior Analysis is, what a good program looks like, and the questions worth asking before you start.", "shot": "A child and clinician at a table, clinician modeling a sign; tight, warm, documentary", "c": "aba"},
    {"slug": "understanding-neuropsychological-evaluation", "title": "Understanding neuropsychological and developmental evaluations", "short": "Understanding neuropsychological evaluations", "cats": ["development", "mental-health"], "read": "6 min read",
     "excerpt": "What an evaluation measures, what it can and cannot tell you, and how to make the report useful afterward.", "shot": "A desk with a closed report folder, glasses, and a cup of tea; calm, no faces", "c": "neuro"},
    {"slug": "supporting-skills-at-home", "title": "Five ways families can support new skills at home", "cats": ["parenting", "family", "behavior"], "read": "4 min read",
     "excerpt": "Small, practical habits that help skills learned in sessions show up in real life.", "shot": "A caregiver and child putting away groceries together, child holding a box; everyday, unposed", "c": "mh"},
]

COMING = [("How to prepare for a first therapy appointment", ["mental-health", "family"], "mh"),
          ("Communication before words: recognizing early signals", ["communication", "development"], "aba"),
          ("Emotional regulation: what it is and how it grows", ["regulation", "parenting"], "mh")]


def article_card(a):
    cats = " ".join(a["cats"])
    tags = " &middot; ".join(CAT_LABEL[c] for c in a["cats"][:2])
    return (f'<a class="article-card" href="/resources/{a["slug"]}" data-cats="{cats}">{photo(a["shot"], "article illustration", a["c"], "photo-wide")}'
            f'<span class="tag" data-c="{CAT_COLOR[a["cats"][0]]}">{tags}</span><h3>{a["title"]}</h3><p>{a["excerpt"]}</p><span class="meta">{a["read"]}</span></a>')


def coming_card(title, cats, c):
    tags = " &middot; ".join(CAT_LABEL[x] for x in cats[:2])
    return (f'<div class="article-card" data-cats="{" ".join(cats)}" aria-label="{title} — coming soon"><div class="ph-block"><strong>Coming soon</strong><p>{title}</p></div>'
            f'<span class="tag" data-c="{c}">{tags}</span><p class="small">This article is planned and will be published here.</p></div>')


def build_resources():
    hero = page_hero("Resources", "Plain-language guides for families and individuals.",
                     "Short, practical reading on ABA, development, mental health, and caregiving — written to be useful, not to sell anything.", "spectrum", ctas=False)
    filters = '<button class="filter" type="button" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button class="filter" type="button" data-filter="{k}" aria-pressed="false">{l}</button>' for k, l, _ in CATS)
    cards = "".join(article_card(a) for a in ARTICLES) + "".join(coming_card(*c) for c in COMING)
    body = hero + f'''
<section class="section" aria-labelledby="articles-h">
  <div class="container">
    <h2 id="articles-h" class="visually-hidden">Articles</h2>
    <div class="filters" role="group" aria-label="Filter by topic">{filters}</div>
    <p class="visually-hidden" aria-live="polite" data-filter-live></p>
    <div class="grid grid-3" style="--gap:2rem">{cards}</div>
    <p class="sched-empty mt-2" data-filter-empty hidden>No articles in this topic yet. New guides are added regularly.</p>
    <div class="mt-3">{notice("Articles are educational and general in nature. They are not individualized clinical advice and do not replace assessment or treatment by a qualified professional.", "", "i")}</div>
  </div>
</section>''' + cta_band("Have a question an article can’t answer?", "Ask it. A clinician will respond.")
    return page("/resources/", "Resources",
                "Plain-language guides on ABA, autism and development, parenting and caregiving, mental health, and emotional regulation from Spektric.",
                body, active="/resources/")


def article_page(a, body_html, date="2026-08-01"):
    tags = " &middot; ".join(CAT_LABEL[c] for c in a["cats"])
    body = f'''
<section class="article-hero"><div class="container"><span class="tag" data-c="{CAT_COLOR[a["cats"][0]]}" style="margin-bottom:1rem">{tags}</span><h1>{a["title"]}</h1><p class="lede">{a["excerpt"]}</p><p class="article-meta"><span>{a["read"]}</span><span>Reviewed by {ph("CLINICIAN NAME, CREDENTIALS")}</span></p></div></section>
<section class="article-body"><div class="container"><div class="prose">{body_html}
<div class="callout"><p><strong>A note on this article.</strong> It is general, educational information. It is not individualized clinical advice and does not replace assessment or treatment by a qualified professional. If you have questions about a specific situation, <a href="/contact">reach out</a>.</p></div>
<p class="mt-2"><a class="text-link" href="/resources/">All resources</a></p></div></div></section>''' + cta_band()
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["excerpt"], "datePublished": date,
               "author": {"@type": "Organization", "name": "Spektric LLC"}, "publisher": {"@id": SITE + "/#organization"}, "mainEntityOfPage": SITE + "/resources/" + a["slug"]}]
    return page("/resources/" + a["slug"], a["title"], a["excerpt"], body, active="/resources/", schema=schema, og_type="article", doc_title=a.get("short", a["title"]))


def build_articles():
    out = {}
    out["resources/what-is-aba.html"] = article_page(ARTICLES[0], '''
<p>Applied Behavior Analysis — ABA — is a therapeutic approach built on a simple observation: behavior is learned, and learning follows patterns that can be understood. When we understand why a behavior happens and what it accomplishes for a person, we can teach new skills that meet the same need more effectively, and we can shape environments so that learning is easier.</p>
<h2>What ABA is not</h2>
<p>ABA is not a single program, a set of drills, or a way to make a person “normal.” Good ABA does not aim to erase difference. It aims to expand what a person can do and choose — to communicate, to connect, to manage daily life, and to participate in the places that matter to them — in ways that respect who they are.</p>
<h2>What a good program looks like</h2>
<ul>
<li><strong>It starts with assessment.</strong> Structured observation and conversation with the family establish current skills, challenges, and what a good outcome would look like in this person’s life.</li>
<li><strong>Goals are individualized and functional.</strong> They are chosen with the person and family, not taken from a generic list, and they are useful outside the therapy room.</li>
<li><strong>Teaching fits the learner.</strong> Strategies are matched to how the person learns best and to the settings where the skill needs to work.</li>
<li><strong>Progress is measured continuously.</strong> Data collected during sessions drive decisions about what to keep, change, or finish.</li>
<li><strong>Families are partners.</strong> Caregivers learn the strategies and use them in everyday routines, which is how new skills become lasting ones.</li>
</ul>
<h2>Questions worth asking any provider</h2>
<ol>
<li>How will you decide which goals to work on, and how will I be involved?</li>
<li>How will I know whether it is working?</li>
<li>What will my role be between sessions?</li>
<li>How do you decide when a goal — or the whole program — is complete?</li>
<li>What will you do if something is not working?</li>
</ol>
<p>A good answer to each of these is specific, plain, and points back to the person receiving care.</p>
<h2>Is ABA the right fit?</h2>
<p>ABA is most often associated with autism, but it can support a range of developmental, learning, and behavioral needs at any age. Whether it is the right choice depends on the individual, their goals, and a careful assessment. Sometimes a different service — psychotherapy, an evaluation, or a referral elsewhere — is the better first step. A thoughtful provider will tell you so.</p>''')

    out["resources/understanding-neuropsychological-evaluation.html"] = article_page(ARTICLES[1], '''
<p>A neuropsychological or developmental evaluation is a structured way of answering a question: <em>How does this person think, learn, and develop — and what would help?</em> It brings together standardized measures, observation, history, and input from the people who know the person best, then translates all of it into a profile of strengths and needs with practical recommendations.</p>
<h2>What it measures</h2>
<p>The specific measures depend on the question and the person’s age, but evaluations commonly look at attention and focus, executive functioning (planning, organization, flexibility), memory and learning, language and communication, visual-spatial skills, processing speed, academic skills, social-emotional functioning, and adaptive skills for daily living. For young children, developmental evaluation focuses on milestones, early communication, play, and learning.</p>
<h2>What it can tell you</h2>
<ul>
<li>Whether a specific diagnosis fits — or does not — when that is the question</li>
<li>Where a person’s strengths are, and how to build on them</li>
<li>Which areas need support, and what kind is likely to help</li>
<li>How to plan school supports and accommodations, including IEP and 504 conversations</li>
<li>A baseline for tracking change over time and response to services</li>
</ul>
<h2>What it cannot tell you</h2>
<p>An evaluation describes a person at a point in time. It does not predict the future, and it does not replace the knowledge of the people who live with that person every day. A good report treats test scores as one source of information among several, and is careful to say what is uncertain.</p>
<h2>What the process looks like</h2>
<ol>
<li><strong>Intake conversation.</strong> The referral question, history, and goals are discussed, and the clinician confirms that an evaluation is likely to be useful.</li>
<li><strong>Testing sessions.</strong> One or more sessions, paced to the person. Breaks are normal; effort matters more than speed.</li>
<li><strong>Scoring and interpretation.</strong> Results are interpreted in context — history, observation, and what teachers, caregivers, or the person themselves report.</li>
<li><strong>Feedback session.</strong> Findings are explained in plain language, with time for questions.</li>
<li><strong>Written report.</strong> A document with recommendations that can be shared with schools, physicians, and treatment providers.</li>
</ol>
<h2>Making the report useful</h2>
<p>Ask the evaluating clinician to walk you through the recommendations in priority order, and ask which ones matter most in the next three months. Share the report with the school and other providers. Bring it to planning meetings. A report that lives in a drawer helps no one; one that shapes the plan can change a year.</p>
<h2>When an evaluation is not the right first step</h2>
<p>Sometimes a conversation, a brief screening, or simply starting services is more useful than formal testing. A thoughtful provider will help you decide, and will not recommend an evaluation that is unlikely to change the plan.</p>''')

    out["resources/supporting-skills-at-home.html"] = article_page(ARTICLES[2], '''
<p>Skills learned in a session are a beginning. They become part of a person’s life when they show up at the kitchen table, in the car, at the store, and at bedtime. Families make that happen — not by running therapy at home, but by building a few habits into the routines they already have.</p>
<h2>1. Pick one routine, not the whole day</h2>
<p>Choose a single daily moment — getting dressed, setting the table, the walk to the bus — and practice one skill there. A small, reliable practice window beats a grand plan that collapses by Wednesday.</p>
<h2>2. Make the first step easy</h2>
<p>Set things up so the skill is likely to succeed: the cup within reach, the picture card on the fridge, the two choices already laid out. Success early makes the next attempt more likely.</p>
<h2>3. Notice what goes right</h2>
<p>Attention is powerful. When the skill happens — even partially — say what you saw, specifically and warmly. “You asked for the juice with your card. I heard you.” Specific recognition teaches more than general praise.</p>
<h2>4. Keep your response consistent</h2>
<p>The same request, the same response, from every adult who can manage it. Consistency makes the world predictable, and predictability makes learning easier. Ask your clinician for the two or three responses that matter most.</p>
<h2>5. Tell the clinician what you see</h2>
<p>You are the best observer of how skills are transferring to real life. A quick note about what worked and what did not is some of the most useful data a clinician will receive, and it shapes the next plan.</p>
<h2>A word about hard days</h2>
<p>Some days nothing goes to plan. That is normal, and it is not a measure of you or your child. Rest, reset, and pick the routine back up tomorrow. Progress is measured across weeks and months, not afternoons.</p>''')
    return out


# ---------------------------------------------------------------- Contact
def build_contact():
    hero = f'''
<section class="page-hero" data-c="spectrum"><div class="container">
  {eyebrow("Contact")}
  <h1>Let’s start with a conversation.</h1>
  <p class="lede">Two simple ways to reach us. Choose a time for a brief consultation, or send us a note and we will follow up the way you prefer.</p>
  <div class="path-tabs" role="tablist" aria-label="Choose how to reach us">
    <a class="path-tab" role="tab" href="#schedule" aria-selected="true">Schedule a consultation</a>
    <a class="path-tab" role="tab" href="#request" aria-selected="false">Request information</a>
  </div>
</div></section>'''

    sched_steps = '<ol class="sched-steps" aria-label="Progress"><li aria-current="false"><span class="n">1</span>Topic</li><li aria-current="step"><span class="n">2</span>Day</li><li aria-current="false"><span class="n">3</span>Time</li><li aria-current="false"><span class="n">4</span>Details</li></ol>'

    scheduler = f'''
<section class="section" id="schedule" aria-labelledby="sched-h">
  <div class="container contact-grid">
    <div>
      {eyebrow("Schedule a consultation")}
      <h2 id="sched-h" style="font-size:clamp(1.75rem,1.3rem+1.6vw,2.5rem)">Choose a time that suits you.</h2>
      <p class="lede" style="margin-bottom:1.5rem">Pick a consultation type, a day, and a time. We will confirm by email — or suggest an alternative if that window is not available.</p>
      <div id="scheduler">
        {sched_steps}
        <div class="field" style="margin-bottom:1.5rem">
          <span class="label" id="type-label">What would you like to discuss?</span>
          <div class="choices" role="radiogroup" aria-labelledby="type-label" data-sched-types></div>
          <p class="help" data-type-note></p>
        </div>
        <div class="sched">
          <div class="cal" aria-label="Choose a day">
            <div class="cal-head"><div class="cal-title" data-cal-title aria-live="polite">Month</div>
              <div class="cal-nav"><button type="button" data-cal-prev aria-label="Previous month">&#8249;</button><button type="button" data-cal-next aria-label="Next month">&#8250;</button></div></div>
            <div class="cal-grid" data-cal-grid></div>
            <div class="cal-legend"><span><i aria-hidden="true"></i>Available to request</span></div>
          </div>
          <div data-slots></div>
        </div>
        <p class="visually-hidden" aria-live="polite" data-sched-live></p>
        <div data-sched-details hidden style="margin-top:2rem">
          <div class="sched-summary" data-sched-summary></div>
          <form id="consult-form" class="form" name="consultation-request" method="post" action="/" data-netlify="true" netlify-honeypot="company" novalidate>
            <input type="hidden" name="form-name" value="consultation-request">
            <p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company" tabindex="-1" autocomplete="off"></label></p>
            <div class="field-row">
              <div class="field" data-required="Enter your name."><label for="c-name">Your name</label><input id="c-name" type="text" name="Name" autocomplete="name" required><p class="error" aria-live="polite"></p></div>
              <div class="field" data-required="Enter your email address."><label for="c-email">Email</label><input id="c-email" type="email" name="Email" autocomplete="email" required><p class="error" aria-live="polite"></p></div>
            </div>
            <div class="field-row">
              <div class="field"><label for="c-phone">Phone <span class="muted" style="font-weight:400">(optional)</span></label><input id="c-phone" type="tel" name="Phone" autocomplete="tel"></div>
              <div class="field"><label for="c-for">Who is this for?</label><select id="c-for" name="Who is this for"><option>Myself</option><option>My child</option><option>Another family member</option><option>A client I am referring</option></select></div>
            </div>
            <div class="field" data-required="Please confirm before sending."><label class="check"><input type="checkbox" name="Acknowledged" value="Yes" required><span>I understand this request is not for urgent needs, and I will not include medical details here.</span></label><p class="error" aria-live="polite"></p></div>
            <div class="btn-row"><button class="btn" type="submit" data-track="consult_submit">Request this time{ARROW}</button></div>
            <p class="form-status" role="alert" data-form-status></p>
          </form>
        </div>
      </div>
      <div class="mt-2">{notice("<strong>This is a request, not a confirmed appointment.</strong> A member of our team will confirm by email. Please do not include medical details, diagnoses, or treatment history — we will gather anything clinical through secure channels once we connect.", "", "i")}</div>
    </div>
    <aside class="contact-aside" aria-label="Contact details">
      <div class="card">
        <dl>
          <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>Phone</dt><dd>{ph("PHONE NUMBER")}</dd></div>
          <div><dt>Location / service area</dt><dd>{ph("ADDRESS OR SERVICE AREA")}</dd></div>
          <div><dt>Hours</dt><dd>{ph("HOURS OF OPERATION")}</dd></div>
        </dl>
      </div>
      <div class="card">
        <h3 style="font-size:1.15rem">What happens next</h3>
        <ol class="prose" style="padding-left:1.2rem;margin:0;font-size:.95rem">
          <li>We confirm your consultation time, or suggest another.</li>
          <li>We talk through what you are looking for and answer questions.</li>
          <li>Together, we decide on a sensible next step — which may be an assessment, a referral, or a plan to begin.</li>
        </ol>
      </div>
      {notice(EMERGENCY, "urgent", "!")}
    </aside>
  </div>
</section>'''

    request = f'''
<section class="section section-alt" id="request" aria-labelledby="req-h">
  <div class="container contact-grid">
    <div>
      {eyebrow("Request information")}
      <h2 id="req-h" style="font-size:clamp(1.75rem,1.3rem+1.6vw,2.5rem)">Send us a note.</h2>
      <p class="lede" style="margin-bottom:1.5rem">Tell us a little about what you are looking for. We will follow up using the contact method you choose.</p>
      <div>
      <form id="request-form" class="form" name="information-request" method="post" action="/" data-netlify="true" netlify-honeypot="company" novalidate>
        <input type="hidden" name="form-name" value="information-request">
        <p class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="company" tabindex="-1" autocomplete="off"></label></p>
        <div class="field-row">
          <div class="field" data-required="Enter your name."><label for="r-name">Your name</label><input id="r-name" type="text" name="Name" autocomplete="name" required><p class="error" aria-live="polite"></p></div>
          <div class="field"><label for="r-care">Parent or caregiver name <span class="muted" style="font-weight:400">(if applicable)</span></label><input id="r-care" type="text" name="Parent or caregiver name"></div>
        </div>
        <div class="field-row">
          <div class="field" data-required="Enter your email address."><label for="r-email">Email</label><input id="r-email" type="email" name="Email" autocomplete="email" required><p class="error" aria-live="polite"></p></div>
          <div class="field"><label for="r-phone">Phone <span class="muted" style="font-weight:400">(optional)</span></label><input id="r-phone" type="tel" name="Phone" autocomplete="tel"></div>
        </div>
        <div class="field">
          <span class="label" id="pref-label">Preferred contact method</span>
          <div class="choices" role="radiogroup" aria-labelledby="pref-label">
            <label class="choice"><input type="radio" name="Preferred contact" value="Email" checked><span>Email</span></label>
            <label class="choice"><input type="radio" name="Preferred contact" value="Phone call"><span>Phone call</span></label>
            <label class="choice"><input type="radio" name="Preferred contact" value="Text message"><span>Text message</span></label>
          </div>
        </div>
        <div class="field-row">
          <div class="field" data-required="Choose a service, or “Not sure yet.”"><label for="r-service">Service of interest</label><select id="r-service" name="Service of interest" required><option value="">Choose one</option><option>ABA services</option><option>Mental health services</option><option>Neurology &amp; evaluation</option><option>Not sure yet</option></select><p class="error" aria-live="polite"></p></div>
          <div class="field"><label for="r-for">Who is this for?</label><select id="r-for" name="Who is this for"><option>Myself</option><option>My child</option><option>Another family member</option><option>A client I am referring</option></select></div>
        </div>
        <div class="field-row">
          <div class="field"><label for="r-pay">Insurance or payment</label><select id="r-pay" name="Insurance or payment"><option>Not sure yet</option><option>I plan to use insurance</option><option>Private pay</option></select><p class="help">Just a general indication — no plan numbers or member IDs, please.</p></div>
          <div class="field"><label for="r-format">Preferred service format</label><select id="r-format" name="Preferred format"><option>Not sure yet</option><option>In person</option><option>Telehealth</option><option>Either</option></select></div>
        </div>
        <div class="field"><label for="r-msg">What are you looking for? <span class="muted" style="font-weight:400">(optional)</span></label><textarea id="r-msg" name="Message" maxlength="1000" placeholder="A sentence or two is plenty. Please don’t include medical details or diagnoses."></textarea><p class="help">We will gather any clinical information through secure channels after we connect.</p></div>
        <div class="field" data-required="Please confirm before sending."><label class="check"><input type="checkbox" name="Acknowledged" value="Yes" required><span>I understand this form is not for urgent needs, and I will not include medical details here.</span></label><p class="error" aria-live="polite"></p></div>
        <div class="btn-row"><button class="btn" type="submit" data-track="request_submit">Send request{ARROW}</button></div>
        <p class="form-status" role="alert" data-form-status></p>
      </form>
      </div>
    </div>
    <aside class="contact-aside" aria-label="Before you write">
      <div class="card">
        <h3 style="font-size:1.15rem">Before you write</h3>
        <ul class="prose" style="padding-left:1.2rem;margin:0;font-size:.95rem">
          <li>Keep it general. We will collect clinical details securely later.</li>
          <li>Referring professionals: include the best way to reach you and whether the family has consented to contact.</li>
          <li>Not sure which service fits? Choose “Not sure yet” and we will help.</li>
        </ul>
      </div>
      <div class="card">
        <h3 style="font-size:1.15rem">Insurance &amp; payment</h3>
        <p class="small">Coverage varies by plan and service. We can help you understand your options before care begins.</p>
        {ph_block("Insurance accepted", "Insert the verified list of plans accepted.")}
      </div>
    </aside>
  </div>
</section>'''

    body = hero + scheduler + request
    schema = [{"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact", "name": "Contact Spektric LLC"}]
    return page("/contact", "Contact & Schedule a Consultation",
                "Schedule a consultation or request information from Spektric LLC. ABA, mental health, and neuropsychological evaluation for children, adolescents, and adults.",
                body, active="/contact", schema=schema, body_class="no-mobile-cta")
