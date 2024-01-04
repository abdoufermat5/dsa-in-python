# chapter 8 trees

A tree is an abstract data type that stores elements hierarchically. 
With the exception of the top element, each element in a tree has a parent element and zero or
more children elements.

![tree](https://raw.githubusercontent.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/master/book/images/image31.jpg)


## Binary Tree

A binary tree is an ordered tree with the following properties:
1. Every node has at most two children.
2. Each child node is labeled as being either a left child or a right child.
3. A left child precedes a right child in the order of children of a node.

![binary tree](https://www.tutorialcup.com/wp-content/uploads/2020/05/bt.png)

#### Properties
Let T be a nonempty binary tree, and let $n$, $n_E$, $n_I$ and $h$ denote the number of nodes, number of external nodes,
number of internal nodes, and height of T, respectively. Then the following are true:

1. $h+1 \leq n \leq 2^{h+1} - 1$
2. $1 \leq n_E \leq 2^h$
3. $h \leq n_I \leq 2^h - 1$
4. $log(n+1) - 1 \leq h \leq n - 1$

if T is a proper binary tree, then the following are true:

1. $2h + 1 \leq n \leq 2^{h+1} - 1$
2. $h + 1 \leq n_E \leq 2^h$
3. $h \leq n_I \leq 2^h - 1$
4. $log(n+1) - 1 \leq h \leq \frac{n-1}{2}$

In a nonempty proper binary tree T, with $n_E$ external nodes and
$n_I$ internal nodes, we have $n_E$ = $n_I+1$


## Tree Traversal Algorithms

### Preorder, Postorder traversals of general trees

#### Preorder Traversal

In a preorder traversal of a tree T, the root of T is visited first and then the subtrees rooted at its children 
are traversed recursively. If the tree is ordered, the subtrees are traversed according to the order of the children.

- Pseudocode
```text
Algorithm preorder(T, p):
    perform the "visit" action for position p
    for each child c in T.children(p) do
        preorder(T, c)
```

This traversal is often used for:
- Creating a copy of a tree: Since the root node is visited first, it can be used to copy the tree into a new one.
- Finding the depth of the tree: The depth of a tree is the maximum number of edges from the root node to any leaf node.
Since the root node is visited first, the depth can be calculated by counting the number of levels.

#### Postorder Traversal

In a postorder traversal of a tree T, the subtrees rooted at the children of the root are traversed recursively,
and then the root is visited.

- Pseudocode
```text
Algorithm postorder(T, p):
    for each child c in T.children(p) do
        postorder(T, c)
    perform the "visit" action for position p
```

This traversal is often used for:
- Deleting a tree: Since the root node is visited last, it can be used to safely delete the tree without 
any dangling pointers.
- Evaluating arithmetic expressions: Since the root node is visited last, it can be used to evaluate arithmetic 
expressions in postfix notation.

### Breadth-First Traversal

Although the preorder and postorder traversals are common ways of visiting the
positions of a tree, another common approach is to traverse a tree so that we visit
all the positions at depth d before we visit the positions at depth d + 1. Such an
algorithm is known as a breadth-first traversal

- Pseudocode
```text
Algorithm breadthfirst(T):
    let Q be a queue initialized with T.root()
    while Q is not empty do
        p = Q.dequeue()         { FIFO queue }
        perform the "visit" action for position p
        for each child c in T.children(p) do
            Q.enqueue(c)
```

BFS is a fundamental algorithm in computer science with many applications, including:

- Finding the shortest path between two nodes: BFS can be used to find the shortest path between two nodes in an 
unweighted graph. This is because it explores nodes in a level-order manner, ensuring that the nodes closer to 
the start node are explored before those that are further away.
- Detecting cycles in graphs: BFS can be used to detect cycles in graphs. If a cycle is present, 
the algorithm will eventually visit the same node twice.
- Topological sorting: BFS can be used to perform topological sorting on directed acyclic graphs (DAGs). 
A topological sort is a linear ordering of the vertices such that for every directed edge (u, v), 
vertex u comes before vertex v in the ordering.

### Inorder Traversal of Binary Tree

The standard preorder, postorder, and breadth-first traversals that were introduced
for general trees, can be directly applied to binary trees. In this section, we introduce another common traversal 
algorithm specifically for a binary tree.

During an inorder traversal, we visit a position between the recursive traversals of its left and right subtrees. 
The inorder traversal of a binary tree T can be informally viewed as visiting the nodes of T “from left to right.” 
Indeed, for every position p, the inorder traversal visits p after all the positions in the left subtree of
p and before all the positions in the right subtree of p.

- Pseudocode
```text
Algorithm inorder(p):
    if p has a left child lc then
        inorder(lc)
    perform the "visit" action for position p
    if p has a right child rc then
        inorder(rc)
```

Inorder traversal is used for several purposes, including:

- Sorting: Inorder traversal of a binary search tree (BST) visits the nodes in ascending order by their values. 
Therefore, it can be used to sort the elements in the BST.
- Searching: Inorder traversal can be used to search for a specific value in a BST. If the value is found, 
the algorithm will return the corresponding node.
- Iterating: Inorder traversal can be used to iterate over the elements of a binary tree. This can be useful 
for tasks such as printing the elements of the tree or performing operations on each element.