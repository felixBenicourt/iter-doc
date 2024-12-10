
# Iter Node Tool Documentation


## Pages

1. [README](./README.md)
2. [User Interface](./docs/ui-overview.md)
3. [Using Nodes](./docs/using-nodes.md)
   - [Node Graph Logic](./docs/node-graph-logic.md)
   - [Node List](./docs/node-list.md)
     - [Add value](../docs/nodes/add_value.md)
     - [Check files](../docs/nodes/check_files.md)
     - [Constant](../docs/nodes/constant.md)
     - [duplicate file](../docs/nodes/duplicate_file.md)
     - [Echo stream attributes](../docs/nodes/echo_stream_attributes.md)
     - [Edit values](../docs/nodes/edit_values.md)
     - [Execute command](../docs/nodes/execute_command.md)
     - [expose_values](../docs/nodes/expose_values.md)
     - [Filter attribute](../docs/nodes/filter_attribute.md)
     - [If condition](../docs/nodes/if_condition.md)
     - [Join path](../docs/nodes/join_path.md)
     - [List](../docs/nodes/list.md)
     - [merge](../docs/nodes/merge.md)
     - [Python houdini](../docs/nodes/python_houdini.md)
     - [Python iter](../docs/nodes/python_iter.md)
     - [Python maya](../docs/nodes/python_maya.md)
     - [Python server houdini](../docs/nodes/python_server_houdini.md)
     - [Python server instances](../docs/nodes/python_server_instances.md)
     - [Python server maya](../docs/nodes/python_server_maya.md)
     - [Python unreal](../docs/nodes/python_unreal.md)
     - [Read dictionary](../docs/nodes/read_dictionary.md)
     - [Read file](../docs/nodes/read_file.md)
     - [Rename key](../docs/nodes/rename_key.md)
     - [Run node](../docs/nodes/run_node.md)
     - [Switch](../docs/nodes/switch.md)
     - [Transfert key](../docs/nodes/transfert_key.md)

4. [Scripting with Python](./docs/scripting-with-python.md)
5. [Node Graph Example](./docs/basic-node-graph-example.md)
6. [License](./docs/license.md)

---


# Iter Node Tool

## Intro
The Iter Node Tool is a versatile, node-based system designed to enhance productivity and streamline workflows for artists, developers, and technical directors working in various DCC  such as Maya, Unreal Engine, Houdini, and Blender.

This tool allows users to build, execute, and manage custom scripts, commands, and automation tasks through an intuitive node-based interface.



## Table of Contents

- [Overview](#Overview)
- [UI](#UI)
- [Nodes](#Nodes)
- [License](#license)



## Overview

[![Watch the video](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ExcWJpbmV4NmsxMHgyYjllamk3cTZzZjIybGNpbHppdG9xcHJ3NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tJdOBEFA3RNnu3IDwf/giphy.gif)](https://vimeo.com/899695629)


#### launch Iter
I use Rez to launch all my tools and DCCs to manage package dependencies.

```bash
rez env iter -- iter
```


## UI


#### Edit UI
![edit ui](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHY2YmZ0cGI3Z3NnYWJkbzNpeGM3azZhc2o5bG0wd2FiMWcxY2FkNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F63dKnXzlPTSUoaWB2/giphy.webp)

You can easily customize the layout of the UI by changing the positions of the windows and docking them wherever you prefer.

---

#### Manage Node Graph
![Manage graph](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTZtbTEwMmw0cTM0ejlzczFkdXQyazRubGk5c3dsbXB4NzdqN3ZwYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Yt6VCDIGFnl7PUFsze/giphy.webp)


## Menu Options


### File Menu
- **New:** `Ctrl+N`  
  Create a new node graph.
- **Open:** `Ctrl+O`  
  Open an existing `.json` node graph file.
- **Save:** `Ctrl+S`  
  Save your current node graph.
- **Save As:** `Ctrl+Shift+S`  
  Save your node graph as a `.json` file with a new name.
- **Exit:** `Ctrl+Q`  
  Exit the Iter Node Tool.

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


## Nodes


#### Create Node
![create node](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHluMWEwMHR1dzIxdDh5YTh4a2RvODZtczBsc2M1cmY2eWhobDljeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XsZHWd0oYdmj2MuTPf/giphy.webp)

To create a new node, right-click on the workspace and select the desired node from the context menu.

---

#### Node Info
![node info](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm1ldnB2cm1xdDhrZW1xcGN5Y3A0dHhmc3JjaDJsdzBsZTlhcXMxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6lemKlKrnvnxDbaIwD/giphy.webp)

To view the information of a node, right-click on the node and select **Node Info** from the menu.

---

#### Node Connection
![node connection](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWh0MnNsY3kxeTZmOWxnbHZuczV2ZzB4YTcxYTVjNDd5cnNnbXN5aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fjB3c6THxDxMIaUz7L/giphy.webp)

To connect a node, left-click on the output of one node and drag it to the input of another node.

---

#### Node Cut Connection
![node cut](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGkwZ3hoYmMycmd1ODdta3RucnBsdWlzYmdtaHhrd3l6aGg2cmcwcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/sz8nt5KvLW030VR033/giphy.webp)

To cut a node connection, hold **Ctrl** and left-click while dragging the cut tool to remove the connection between nodes.



## License
```text
Custom License Agreement

Copyright (c) 2024 Felix Benicourt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this documentation (the "Documentation"), to use, study, and modify the
Documentation for personal, educational, or internal purposes, subject to the
following conditions:

1. Redistribution and Resale:
   - Redistribution, sublicensing, or resale of the Documentation is allowed,
     provided the Documentation is not bundled with or distributed alongside
     the source code or any executable components of the software. The source 
     code and executable components of the Software remain closed and may not
     be redistributed without prior written consent from the author.

2. Attribution:
   - This copyright notice and permission notice shall be included in all copies
     or substantial portions of the Documentation.

3. No Warranty:
   - THE DOCUMENTATION IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL
     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING
     FROM, OUT OF, OR IN CONNECTION WITH THE DOCUMENTATION OR THE USE OR OTHER DEALINGS
     IN THE DOCUMENTATION.
```



