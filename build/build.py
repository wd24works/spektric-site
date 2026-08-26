import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from common import SITE
import page_home, page_services, page_other, page_contact_resources as pcr

OUT = os.path.join(os.path.dirname(__file__), "..", "site")

pages = {
    "index.html": page_home.build(),
    "aba-services.html": page_services.build_aba(),
    "mental-health.html": page_services.build_mh(),
    "neurology.html": page_services.build_neuro(),
    "who-we-serve.html": page_other.build_serve(),
    "about.html": page_other.build_about(),
    "faq.html": page_other.build_faq(),
    "resources/index.html": pcr.build_resources(),
    "contact.html": pcr.build_contact(),
    "privacy.html": page_other.build_privacy(),
    "terms.html": page_other.build_terms(),
    "accessibility.html": page_other.build_accessibility(),
    "404.html": page_other.build_404(),
}
pages.update(pcr.build_articles())

for name, html in pages.items():
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

# sitemap
urls = [("", "1.0"), ("/aba-services", "0.9"), ("/mental-health", "0.9"), ("/neurology", "0.9"), ("/who-we-serve", "0.8"), ("/about", "0.8"),
        ("/resources/", "0.7"), ("/faq", "0.7"), ("/contact", "0.9"), ("/privacy", "0.3"), ("/terms", "0.3"), ("/accessibility", "0.3")]
urls += [("/resources/" + a["slug"], "0.6") for a in pcr.ARTICLES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}{u}{'/' if u == '' else ''}</loc><priority>{p}</priority></url>\n" for u, p in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

# host configs for clean URLs + 404
open(os.path.join(OUT, "vercel.json"), "w").write(json.dumps({"cleanUrls": True, "trailingSlash": False}, indent=2) + "\n")
open(os.path.join(OUT, "netlify.toml"), "w").write('[build]\n  publish = "."\n\n[[headers]]\n  for = "/*"\n  [headers.values]\n    X-Content-Type-Options = "nosniff"\n    X-Frame-Options = "SAMEORIGIN"\n    Referrer-Policy = "strict-origin-when-cross-origin"\n')
open(os.path.join(OUT, ".htaccess"), "w").write("Options -MultiViews\nRewriteEngine On\nRewriteCond %{REQUEST_FILENAME} !-d\nRewriteCond %{REQUEST_FILENAME}.html -f\nRewriteRule ^(.+)$ $1.html [L]\nErrorDocument 404 /404.html\n")
print("built", len(pages), "pages")
