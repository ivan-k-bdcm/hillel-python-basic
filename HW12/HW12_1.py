import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    result = []
    in_tag = False
    for c in html:
        if c == '<':
            in_tag = True
        elif c == '>':
            in_tag = False
        elif not in_tag:
            result.append(c)

    text = ''.join(result)
    clean_html = [line for line in text.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(clean_html))


delete_html_tags("draft.html")
