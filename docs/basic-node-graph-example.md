# Examples and Tutorials

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


## Example: Creating a Scene and Accessing Node Variables

This example demonstrates how Iter manages scenes, allowing you to load, reuse, and refactor them to build complex setups from simple, reusable node graphs.

---

### Step 1: Create and Configure Nodes

1. Add multiple **Constant Nodes** and define their key-value pairs. 
2. Merge these nodes and manipulate their data as needed.
3. Include an **Echo Stream Attribute Node**, rename it for clarity (e.g., "Echo var").

![Step 1](https://i.imgur.com/9Oy0txQ.png)

---

### Step 2: Save the Node Graph

Save your node graph with a meaningful name. In this example, it is saved as **"CONSTANTS"**.

---

![Step 1](https://i.imgur.com/rcIcyiu.png)

### Step 3: Create a New Scene and Load the Constants

1. Create a new scene and add a **Read File Node**.
   - Use this node to specify the file path for the saved **CONSTANTS** graph.
   - Assign the file path to a custom attribute (e.g., `"path"`).
2. Add a **Python Iter Node** and a **Run Node**.
3. In the **Python Iter Node**, input the following code:

```python
from commands import iter_instance

# Load the saved node graph from the specified path
iter_instance.fileLoad(input_data['path'])

# Access the "Echo var" node by its custom name
echoNode = iter_instance.getNodeFromCustomName("Echo var")

# Print the attributes of the Echo node if found
if echoNode:
    print(echoNode.calcAttributes())
else:
    print({'test': None})
```




