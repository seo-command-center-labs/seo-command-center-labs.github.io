"""CI check for the neutral test site: every page parses, has a doctype, <html lang>, exactly one <title>, a closing </html>, and loads no
script from another host. Standard library only (runs on the GitHub runner without installs). Exit 1 on the first failing page."""
import sys, pathlib, re
from html.parser import HTMLParser

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.titles = 0; self.lang = False; self.foreign_scripts = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html' and a.get('lang'): self.lang = True
        if tag == 'title': self.titles += 1
        if tag == 'script' and re.match(r'^(https?:)?//', a.get('src') or ''): self.foreign_scripts.append(a['src'])

def check(path: pathlib.Path) -> list:
    text = path.read_text(encoding='utf-8'); p = Page(); p.feed(text); errors = []
    if not text.lstrip().lower().startswith('<!doctype html>'): errors.append('doctype missing')
    if not p.lang: errors.append('<html lang> missing')
    if p.titles != 1: errors.append(f'{p.titles} <title> elements')
    if '</html>' not in text.lower(): errors.append('</html> missing')
    if p.foreign_scripts: errors.append('script from another host: ' + ', '.join(p.foreign_scripts))
    return errors

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.'); bad = 0
for f in sorted(root.rglob('*.html')):
    errs = check(f)
    print(('FAIL ' if errs else 'ok   ') + str(f) + ('  ' + '; '.join(errs) if errs else '')); bad += bool(errs)
sys.exit(1 if bad else 0)
