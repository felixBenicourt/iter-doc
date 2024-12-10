
# Nodes


## Pages

1. [README](../../README.md)
2. [User Interface](./ui-overview.md)
3. [Using Nodes](./using-nodes.md)
   - [Node Graph Logic](./node-graph-logic.md)
   - [Node List](./node-list.md)
     - [Add value](./nodes/add_value.md)
     - [Check files](./nodes/check_files.md)
     - [Constant](./nodes/constant.md)
     - [duplicate file](./nodes/duplicate_file.md)
     - [Echo stream attributes](./nodes/echo_stream_attributes.md)
     - [Edit values](./nodes/edit_values.md)
     - [Execute command](./nodes/execute_command.md)
     - [expose_values](./nodes/expose_values.md)
     - [Filter attribute](./nodes/filter_attribute.md)
     - [If condition](./nodes/if_condition.md)
     - [Join path](./nodes/join_path.md)
     - [List](./nodes/list.md)
     - [merge](./nodes/merge.md)
     - [Python houdini](./nodes/python_houdini.md)
     - [Python iter](./nodes/python_iter.md)
     - [Python maya](./nodes/python_maya.md)
     - [Python server houdini](./nodes/python_server_houdini.md)
     - [Python server instances](./nodes/python_server_instances.md)
     - [Python server maya](./nodes/python_server_maya.md)
     - [Python unreal](./nodes/python_unreal.md)
     - [Read dictionary](./nodes/read_dictionary.md)
     - [Read file](./nodes/read_file.md)
     - [Rename key](./nodes/rename_key.md)
     - [Run node](./nodes/run_node.md)
     - [Switch](./nodes/switch.md)
     - [Transfert key](./nodes/transfert_key.md)

4. [Scripting with Python](./scripting-with-python.md)
5. [Node Graph Example](./basic-node-graph-example.md)
6. [License](./license.md)

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


## Attributes

The **Stream Attributes List** in the Iter Node Tool dynamically displays the attributes of the selected node. These attributes are presented in a key-value structure, much like Python dictionaries, providing a clear and organized view.

### Viewing Attributes
Each node's attributes are listed with their keys and corresponding values, enabling users to review and, if needed, modify them directly. The displayed attributes update automatically based on the selected node.

### Attributes in Node Connections
When you connect nodes, the **Stream Attributes List** expands to show all the attributes being passed as inputs to the connected nodes. This feature facilitates smooth data transfer and ensures the accurate flow of information between nodes.



