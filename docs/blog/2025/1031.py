from difflib import Differ
from lino.utils.soup import sanitized_soup

TOC_MARKER = "=TOC_HERE="
html = """\
<html><body><p>This page is an example.</p>
<p>=TOC_HERE=</p>
<h1>First approach</h1>
<p>The first approach has 2 steps</p>
<h2>First</h2>
<p>In a <b>first</b> step ...</p>
<h2>Second</h2>
<p>In a second step ...</p>
<h1>Second approach</h1>
<h2>Third</h2>
<p>In a third step ...</p>
<h2>Fourth</h2>
<p>In a fourth step ...</p></body></html>"""


def add_toc(html):
    toc_tag = None
    headers = []
    soup = sanitized_soup(html)
    for tag in soup.children:
        if tag.name is None:
            # print(f"Oops: {repr(tag)}")
            continue
        tag_name = tag.name.lower()
        if tag_name == "div" and tag.get('id', None) == "contents":
            tag.clear()
            toc_tag = tag
            continue
        elif tag.string and tag.string.strip() == TOC_MARKER:
            tag.name = 'div'
            tag.clear()
            toc_tag = tag
            continue
        elif tag_name == "h1":
            headers.append(tag.string)
            # todo add an anchor and a backlink
            # if tag.contents[-1].name == "a"
            # <a class="headerlink" href="#kuhu-minna" title="Link to this heading">¶</a>

    if toc_tag is not None:
        toc_tag['id'] = "contents"
        ul = soup.new_tag('ul')
        for h in headers:
            ul.append(soup.new_tag('li', string=h))
            toc_tag.append(ul)

    return str(soup)


html2 = add_toc(html)
print(html2)
html3 = add_toc(html2)
if html2 != html3:
    print("Oops there are differences:")
    d = Differ()
    for ln in d.compare(html2.splitlines(), html3.splitlines()):
        print(ln)
