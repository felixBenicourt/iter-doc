
# Nodes


## Pages

1. [README](../../README.md)
2. [User Interface](../ui-overview.md)
3. [Using Nodes](../using-nodes.md)
   - [Node Graph Logic](../node-graph-logic.md)
   - [Node List](../node-list.md)
     - [Add value](../nodes/add_value.md)
     - [Check files](../nodes/check_files.md)
     - [Constant](../nodes/constant.md)
     - [duplicate file](../nodes/duplicate_file.md)
     - [Echo stream attributes](../nodes/echo_stream_attributes.md)
     - [Edit values](../nodes/edit_values.md)
     - [Execute command](../nodes/execute_command.md)
     - [expose_values](../nodes/expose_values.md)
     - [Filter attribute](../nodes/filter_attribute.md)
     - [If condition](../nodes/if_condition.md)
     - [Join path](../nodes/join_path.md)
     - [List](../nodes/list.md)
     - [merge](../nodes/merge.md)
     - [Python houdini](../nodes/python_houdini.md)
     - [Python iter](../nodes/python_iter.md)
     - [Python maya](../nodes/python_maya.md)
     - [Python server houdini](../nodes/python_server_houdini.md)
     - [Python server instances](../nodes/python_server_instances.md)
     - [Python server maya](../nodes/python_server_maya.md)
     - [Python unreal](../nodes/python_unreal.md)
     - [Read dictionary](../nodes/read_dictionary.md)
     - [Read file](../nodes/read_file.md)
     - [Rename key](../nodes/rename_key.md)
     - [Run node](../nodes/run_node.md)
     - [Switch](../nodes/switch.md)
     - [Transfert key](../nodes/transfert_key.md)

4. [Scripting with Python](../scripting-with-python.md)
5. [Node Graph Example](../basic-node-graph-example.md)
6. [License](../license.md)

---

## Python Server Maya Node

### Table of Contents
- [Description](#description)
- [Inputs](#inputs)
- [Required Attributes](#required-attributes)
- [Usage](#usage)

---

### Description

The **Python Server Maya Node** executes a Python script on the selected Maya instances. This node allows you to apply Python scripts to manipulate specific instances in a Maya scene, providing flexibility in working with instance-based data.

---

### Inputs

- **Input**: Main flux.

---

### Required Attributes

- **selected instances**: The instances in Maya that are selected for script execution.

---

### Usage

- You can manipulate the data of the selected Maya instances with the variable `variables` within the Python script.
- Write custom Python code to process or modify the instances based on the provided flux and attributes.
