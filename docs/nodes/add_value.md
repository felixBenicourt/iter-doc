
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

## Add Value Node

### Table of Contents
- [Description](#description)
- [Inputs](#inputs)
- [Parameters](#parameters)

---

### Description

The **Add Value Node** is designed to merge chosen attribute values within the node graph. It allows you to add a value to an existing attribute and customize the result with optional prefixes and suffixes.

---

### Inputs

- **Top Input**:  
  The main data flow (flux) that carries the attributes.

- **Bottom Input**:  
  The attribute value you want to add to the main data flow. This can override the default value specified in the parameters.

---

### Parameters

- **Attribute**:  
  The name of the attribute you want to merge. This serves as the key in the data flow.

- **Value**:  
  The value to add to the current value of the specified attribute. This can be overridden by the value from the bottom input.

- **Pre Value**:  
  A string to prepend to the final value.

- **Post Value**:  
  A string to append to the final value.
