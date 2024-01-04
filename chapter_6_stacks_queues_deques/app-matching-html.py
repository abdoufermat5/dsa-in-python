from array_stack import ArrayStack


def is_matched_html(ram_html: str):
    """Return True if all HTML tags are properly matched, False otherwise"""

    S = ArrayStack()
    j = ram_html.find('<')  # find first "<" tag index in raw_html string

    while j != -1:
        k = ram_html.find('>', j+1)  # find the second ">" tag index in raw_html
        if k == -1:
            return False

        tag = ram_html[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:]!=S.pop():
                return False
        j = ram_html.find('<', k+1)
    return S.is_empty()


if __name__ == '__main__':
    raw = """<body>
    <center>
    <h1> The Little Boat </h1>
    </center>
    <p> The storm tossed the little
    boat like a cheap sneaker in an
    old washing machine. The three
    drunken fishermen were used to
    such treatment, of course, but
    not the tree salesman, who even as
    a stowaway now felt that he
    had overpaid for the voyage. </p>
    <ol>
    <li> Will the salesman die? </li>
    <li> What color is the boat? </li>
    <li> And what about Naomi? </li>
    </ol>
    </body>"""
    print(is_matched_html(raw))
