# Work in progress

# Iter Node Tool

## Overview
The Iter Node Tool is a versatile, node-based system designed to enhance productivity and streamline workflows for artists, developers, and technical directors working in various DCC  such as Maya, Unreal Engine, Houdini, and Blender.

This tool allows users to build, execute, and manage custom scripts, commands, and automation tasks through an intuitive node-based interface.


---

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

---
### Iter Node Editor Tool - QT-Python Overview
---

[![Watch the video](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ExcWJpbmV4NmsxMHgyYjllamk3cTZzZjIybGNpbHppdG9xcHJ3NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tJdOBEFA3RNnu3IDwf/giphy.gif)](https://vimeo.com/899695629)


#### launch Iter
![rez cmd](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmdwMTJidzJ3bm04dnM5OGZybTczeTdoY3hhbnY2OHEzdG5zZ3Q1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NlnKLDnvbK1cYyzarP/giphy.gif)


```bash
rez env iter -- iter
```

---
#### UI
---

#### Edit UI
![edit ui](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHY2YmZ0cGI3Z3NnYWJkbzNpeGM3azZhc2o5bG0wd2FiMWcxY2FkNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F63dKnXzlPTSUoaWB2/giphy.webp)

You can easily customize the layout of the UI by changing the positions of the windows and docking them wherever you prefer.

---

#### Manage Node Graph
![Manage graph](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTZtbTEwMmw0cTM0ejlzczFkdXQyazRubGk5c3dsbXB4NzdqN3ZwYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Yt6VCDIGFnl7PUFsze/giphy.webp)

In the **File Menu**:
- **New:** `Ctrl+N` to create a new node graph.
- **Open:** `Ctrl+O` to open an existing `.Json` node graph file.
- **Save:** `Ctrl+S` to save your current node graph.
- **Save As:** `Ctrl+Shift+S` to save your node graph as a `.Json` file with a new name.
- **Exit:** `Ctrl+Q` to exit the Iter tool.

In the **Edit Menu**:
- **Undo:** `Ctrl+Z` to undo your last operation.
- **Redo:** `Ctrl+Shift+Z` to redo the previously undone operation.
- **Cut:** `Ctrl+X` to cut the selected nodes.
- **Copy:** `Ctrl+C` to copy the selected nodes.
- **Paste:** `Ctrl+V` to paste the copied or cut nodes.
- **Delete:** `Del` to delete the selected nodes.

---

#### Nodes

---

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
of this software and associated documentation files (the "Software"), to use,
study, and modify the Software for personal, educational, or internal purposes,
subject to the following conditions:

1. Redistribution and Resale:
   - Redistribution, sublicensing, or resale of the Software, in whole or in part, 
     is strictly prohibited without prior written consent from the author.

2. Attribution:
   - This copyright notice and permission notice shall be included in all copies 
     or substantial portions of the Software.

3. No Warranty:
   - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
     FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL 
     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER 
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING 
     FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
     IN THE SOFTWARE.

```





