import bs4
from html5print import HTMLBeautifier

def prettify(raw_html):
    soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    pretty1 = soup.prettify(encoding='utf-8')
    return HTMLBeautifier.beautify(pretty1, 4)


def concat_all(outfile):
    index_template = open('tmp/index_template.html').read()
    
    index_raw_content = index_template.format(
        carte_pizzas=open('tmp/pizzas.html').read()
    )

    index_content = prettify(index_raw_content)
    with open(outfile, 'w') as out:
        out.write(index_content)
