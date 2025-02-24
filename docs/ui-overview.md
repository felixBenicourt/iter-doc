

# User Interface


## Pages

1. [README](../README.md)
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

![script_editor](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExemJsM3VmcDZnaXRtdHF0b2hwOGxvYWxybnd5dWxmeGQyYXJrZzhsNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ADr67DBYqmQHAk1Zh6/giphy.gif)

### Script Editor Toolbar

The **Script Editor Toolbar** provides quick access to essential actions for managing your Python scripts.

- **Run Icon**: Executes the current Python script in the editor.
- **Open Folder Icon**: Loads an existing Python script into the editor.
- **Disk Icon**: Saves the current script as a Python file.

These tools streamline your workflow, making it easy to edit, save, and execute scripts directly within the Iter Node Tool.






