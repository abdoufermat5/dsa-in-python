from base import Tree


def preorder_indent(T, p, d):
    """Print preorder representation of subtree of T rooted at at p at depth d."""
    print(2 * d * " " + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)


def preorder_label(T, p, d, path):
    """Print labeled representation of T rooted at at p at depth d"""
    label = ". ".join(str(j + 1) for j in path)
    print(2 * d * " " + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop(0)

# will print something like:
# Electronics R’Us
#   1 R&D
#   2 Sales
#       2.1 Domestic
#       2.2 International
#           2.2.1 Canada
#           2.2.2 S. America


def parenthesize(T, p):
    """Print parenthesized representation of a subtree T rooted at at p"""

    print(p.element(), end="")
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = " (" if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthesize(T, c)
        print(")", end="")

# will print something like:
# Electronics R’Us (R&D, Sales (Domestic, International (Canada,
# S. America, Overseas (Africa, Europe, Asia, Australia))),
# Purchasing, Manufacturing (TV, CD, Tuner))
