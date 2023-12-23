def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p"""

    subtotal = p.element().space()  # we assume a space method implemented

    for c in T.children(p):
        subtotal += disk_space(T, c)

    return subtotal
