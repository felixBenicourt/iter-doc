# Advanced Features

## Pages

1. [README](../README.md)
2. [User Interface](./ui-overview.md)
3. [Managing Node Graphs](./managing-node-graphs.md)
4. [Using Nodes](./using-nodes.md)
   - [Node Graph Logic](./node-graph-logic.md)
   - [Nodes](./node-list.md)
5. [Scripting with Python](./scripting-with-python.md)
6. [Examples and Tutorials](./examples-and-tutorials.md)
   - [Basic Node Graph Example](./basic-node-graph-example.md)
7. [License](./license.md)

---



### Using the Iter API in script editor.
To start using the Iter API in your scripts, you need to import the API module. Here's an example:

![python_example](https://i.imgur.com/qoiDeFd.png)


```python
from iter_instance import itr
```

Example :

```python
from  iter_instance import itr
echoNode = itr.getNodeFromName(name='Echo stream attributes')
print(echoNode.calcAttributes())
```

The printed echo :

```
{'test': 'value', 'another test': 'another value'}
```

