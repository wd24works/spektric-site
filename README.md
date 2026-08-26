# Spektric LLC — website (spektric.com)

A static site: plain HTML, one CSS file, two small JS files. No build step is required to host it — upload the contents of this folder to any static host.

## Deploy (pick one)

| Host | What to do |
|---|---|
| **Netlify** | Drag this folder onto app.netlify.com. `netlify.toml` is included (security headers). Forms work automatically — set `formProvider: "netlify"` in `assets/js/config.js`, or leave `"auto"`. |
| **Vercel** | `vercel deploy` from this folder. `vercel.json` enables clean URLs (`/about` → `about.html`). |
| **cPanel / Apache** | Upload everything to `public_html`. `.htaccess` handles clean URLs and the 404 page. |
| **Any other host** | Make sure `/about` serves `about.html` (clean URLs) and `/404.html` is the not-found page. |

## Connect the forms and scheduler — edit ONE file

`assets/js/config.js`

- `formEndpoint` — paste a Formspree / Basin / Getform endpoint and submissions are POSTed there as JSON.
- `formProvider` — `"auto"` (default), `"endpoint"`, `"netlify"`, or `"email"`. With no endpoint configured, the site falls back to opening the visitor's email app with the request pre-written, addressed to `contactEmail`.
- `calendlyUrl` — paste a Calendly (or similar) link to replace the built-in scheduler with a live booking calendar. Leave empty to keep the built-in **request-a-time** scheduler.
- `scheduler` — days ahead, lead time, weekdays, hours, slot length, time-zone label, blocked dates.
- `consultationTypes` — the options shown in the scheduler.

The built-in scheduler sends a **booking request**, not a confirmed appointment — the site says so at every step. You confirm by email.

## Before launch — replace every placeholder

Search the HTML for `[` … `]` and `Placeholder —`. Each one marks information that must come from Spektric and be verified:

1. Phone number, address / service area, hours (footer, contact page).
2. Insurance accepted, private-pay details, authorization notes (home, contact, FAQ).
3. Clinical team, licensure, and supervision structure for each service line (About, ABA, Neurology, Mental Health).
4. Leadership biographies (About).
5. Additional neurology services (Neurology) — or remove that block.
6. Service settings (clinic / home / school / telehealth) and any age limits per service.
7. Testimonials — only with written consent, or leave the section as is.
8. Privacy Policy, Terms of Use, Accessibility Statement — counsel review and effective dates.
9. Notice of Privacy Practices link (footer).
10. "Reviewed by" clinician on each article.
11. Photo slots — each placeholder carries an art-direction note describing the photo to commission.
12. `assets/img/og-image.png` — optional: replace with a designed social-share image.
13. Organization schema in every page `<head>` — the `[PLACEHOLDER]` address and phone fields.

## Editing content

Page HTML is readable and hand-editable. If you want to regenerate pages from the source templates instead, the Python generator lives in the separate `build/` folder (run `python3 build/build.py`).

## Accessibility & compliance notes

- Targets WCAG 2.2 AA: semantic landmarks, skip link, visible focus, 4.5:1 text contrast, keyboard-operable scheduler and menus, `prefers-reduced-motion` respected.
- Forms avoid collecting PHI: no diagnosis, history, or insurance-ID fields; reminders appear on every form.
- Emergency (911) notice appears on every page footer and on clinical pages.
- No credentials, outcomes, insurance plans, or testimonials are stated anywhere without a placeholder.
