/* ==========================================================================
   SPEKTRIC — Site configuration
   This is the only file you need to edit to connect the forms and scheduler.
   Everything below is a plain setting; no programming knowledge needed.
   ========================================================================== */
window.SPEKTRIC_CONFIG = {

  /* Where form submissions go. Options:
     "auto"     — use formEndpoint if it is filled in; otherwise fall back to email.
     "endpoint" — always POST to formEndpoint (Formspree, Basin, Getform, your own server…).
     "netlify"  — use Netlify Forms (works automatically when the site is hosted on Netlify).
     "email"    — open the visitor's email app with the request pre-written (no setup needed). */
  formProvider: "auto",

  /* Paste a form endpoint URL here, e.g. "https://formspree.io/f/abcd1234" */
  formEndpoint: "",

  /* Where email-fallback messages are addressed. */
  contactEmail: "info@spektric.com",

  /* OPTIONAL: paste a Calendly (or similar) scheduling link here to replace the built-in
     consultation scheduler with a live booking calendar, e.g. "https://calendly.com/spektric/intro-call" */
  calendlyUrl: "",

  /* Built-in scheduler settings (used when calendlyUrl is empty). */
  scheduler: {
    daysAhead: 28,                  // how far ahead visitors can request a time
    minLeadDays: 1,                 // earliest request is tomorrow (1) — set 0 to allow same-day
    weekdays: [1, 2, 3, 4, 5],      // 0 = Sunday … 6 = Saturday
    startTime: "09:00",             // first consultation start time
    endTime: "17:00",               // last slot starts before this time
    stepMinutes: 30,                // length of each consultation window
    timeZoneLabel: "Eastern Time (ET)",
    blockedDates: []                // e.g. ["2026-11-26", "2026-12-25"]
  },

  /* Consultation types offered in the scheduler. */
  consultationTypes: [
    { id: "intro",  label: "Introductory call",          note: "15–20 minutes. Questions, fit, next steps." },
    { id: "aba",    label: "ABA services consultation",  note: "Discuss ABA for a child, teen, or adult." },
    { id: "mh",     label: "Mental health consultation", note: "Individual, family, or parent support." },
    { id: "neuro",  label: "Evaluation inquiry",         note: "Neuropsychological or developmental testing." }
  ]
};
