
# Nodes

## Pages

1. [README](../README.md)
2. [User Interface](./docs/ui-overview.md)
3. [Managing Node Graphs](./docs/managing-node-graphs.md)
4. [Using Nodes](./docs/using-nodes.md)
   - [Node Graph Logic](./docs/node-graph-logic.md)
   - [Nodes](./docs/node-list.md)
5. [Window Options](./docs/window-options.md)
6. [Advanced Features](./docs/advanced-features.md)
   - [Scripting with Python](./docs/scripting-with-python.md)
   - [Iter Python API](./docs/iter-python-api.md)
7. [Examples and Tutorials](./docs/examples-and-tutorials.md)
   - [Basic Node Graph Example](./docs/basic-node-graph-example.md)
   - [Advanced Workflow](./docs/advanced-workflow.md)
8. [License](./docs/license.md)

---


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

### Core Systems of Nodes

Please keep in mind that each node can have up to **two core systems**:

1. **Real-Time Feedback System**  
   This core system allows nodes to manipulate information and provide quick feedback when clicked. It enables you to set up and manipulate your graph dynamically, with live data adjustments as you interact with the node.

2. **Heavy Operation System**  
   This system is designed for more time-consuming tasks that require heavier computational operations. These operations are triggered when you run your graph through the **Run Node**, which processes the graph in a batch or more intensive manner.




