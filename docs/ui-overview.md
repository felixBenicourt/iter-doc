

# User Interface


## Pages

1. [README](../README.md)
2. [User Interface](./ui-overview.md)
3. [Managing Node Graphs](./managing-node-graphs.md)
4. [Using Nodes](./using-nodes.md)
   - [Node Graph Logic](./node-graph-logic.md)
   - [Nodes](./node-list.md)
5. [Advanced Features](./advanced-features.md)
   - [Scripting with Python](./scripting-with-python.md)
   - [Iter Python API](./iter-python-api.md)
6. [Examples and Tutorials](./examples-and-tutorials.md)
   - [Basic Node Graph Example](./basic-node-graph-example.md)
   - [Advanced Workflow](./advanced-workflow.md)
7. [License](./license.md)

---



### Edit Menu
- **Undo:** `Ctrl+Z`  
  Undo your last operation.
- **Redo:** `Ctrl+Shift+Z`  
  Redo the previously undone operation.
- **Cut:** `Ctrl+X`  
  Cut the selected nodes.
- **Copy:** `Ctrl+C`  
  Copy the selected nodes.
- **Paste:** `Ctrl+V`  
  Paste the copied or cut nodes.
- **Delete:** `Del`  
  Delete the selected nodes.

### Window Menu
- **Stream Attributes List Window:**  
  Display the attributes of the nodes.
- **Node Properties Window:**  
  View and edit parameters of the selected node.
- **Script Editor Window:**  
  Access the Iter Python Script Editor.
- **Close:**  
  Close the current node graph.
- **Close All:**  
  Close all open node graphs.
- **Tile:**  
  Detach the node graph from the dock.
- **Cascade:**  
  Add a node graph within the current workspace.
- **Next:** `Ctrl+Tab`  
  Move to the next node graph to the right.
- **Previous:** `Ctrl+Shift+Backtab`  
  Move to the previous node graph to the left.

### Help Menu
- **About:**  
  Navigate to the documentation (you’re here!).


## Stream Attributes List

![stream_attributes_list](https://i.imgur.com/HitlwGC.png)

When you click on a node in the Iter Node Tool, the **Stream Attributes List** will display all the available attributes associated with that node. Each attribute is represented by a key and a corresponding value, similar to how Python dictionaries are structured.

### Attribute Format
The attributes are shown in a key-value format, allowing you to easily view and modify them. These attributes are dynamic, and their values can be changed based on the context of the node.

### Node Connections
When nodes are connected, the **Stream Attributes List** will display all the attributes as inputs for the connected nodes. This allows you to easily pass data between nodes and ensure that the correct attributes are being transferred.

![stream_attributes_list](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXBraXp0YWZzaXFlbzZ6cTE0MHYxa3d2Y3o3OXkzam9xM2k0ZzZnaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PYQjnY7haYad92nNWg/giphy.gif)


## Script Editor

The **Script Editor** in the Iter Node Tool allows you to write and execute Python scripts directly within the application. This feature is particularly useful for creating macros and automating workflows using the Iter API.

![script_editor](https://i.imgur.com/yGgwulH.gif)

### Using the Iter API
To start using the Iter API in your scripts, you need to import the API module. Here's an example:

```python
from iter_instance import itr
```

### Script Editor Toolbar

The **Script Editor Toolbar** provides quick access to essential actions for managing your Python scripts.

- **Run Icon**: Executes the current Python script in the editor.
- **Open Folder Icon**: Loads an existing Python script into the editor.
- **Disk Icon**: Saves the current script as a Python file.

These tools streamline your workflow, making it easy to edit, save, and execute scripts directly within the Iter Node Tool.






