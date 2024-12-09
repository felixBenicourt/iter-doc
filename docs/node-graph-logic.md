
# Node Graph Logic

## Table of Contents

0. [README](README.md)
1. [User Interface](./docs/ui-overview.md)
   - [Customizing the Layout](./docs/customizing-the-layout.md)
   - [Managing Node Graphs](./docs/managing-node-graphs.md)
2. [Using Nodes](./docs/using-nodes.md)
   - [Node Graph Logic](./docs/node-graph-logic.md)
   - [Nodes](./docs/node-list.md)
3. [Window Options](./docs/window-options.md)
4. [Advanced Features](./docs/advanced-features.md)
   - [Scripting with Python](./docs/scripting-with-python.md)
   - [Iter Python API](./docs/iter-python-api.md)
5. [Examples and Tutorials](./docs/examples-and-tutorials.md)
   - [Basic Node Graph Example](./docs/basic-node-graph-example.md)
   - [Advanced Workflow](./docs/advanced-workflow.md)
6. [License](./docs/license.md)

---


# Nodes

## Table of Contents
- [Nodes Logic](#nodes-logic)
- [Attributes](#attributes)

## Nodes Logic

The evaluation of nodes follows a **left-to-right** process. For nodes with multiple entries, the first entries represent the inputs, which are positioned at the top-left side of the node.

In the context of a graph with multiple nodes, each node with multiple inputs is evaluated sequentially. The node positioned at the top-left is evaluated first, followed by the node directly beneath it, continuing until all nodes have been evaluated.

### How to Evaluate a Node?

Evaluating a node is simple:
1. **Click** on the node.
2. The parameters of the node will be displayed.
3. The **Stream Attributes List Window** will update to show the relevant data associated with that node.

Each node has a specific purpose, and when combined with other nodes, they can form complex systems to perform more advanced operations.

---

By following this logical evaluation process, you can build intricate and dynamic systems by simply combining different nodes and their respective functions.


