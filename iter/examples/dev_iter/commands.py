

# from iter_sub_window import IterSubWindow modules for developement purpuses
# The import is : from commands import iter_instance
# Work in the Script Editor window

# commands.py

import os, sys
sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))
from iter_console_window import *
from iter_sub_window import IterSubWindow


class Build(IterSubWindow):
    def __init__(self):
        super().__init__()

    def doEvalImplementationNodesType(self, typeNode: str):
        for node in self.scene.nodes:
            if node.__class__.__name__ == typeNode:
                node.evalImplementation()

    def doEvalImplementationNodeId(self, nodeId: int):
        for node in self.scene.nodes:
            if node.id == nodeId:
                node.evalImplementation()

    def doEvalImplementationNodeCustomName(self, customName: str):
        for node in self.scene.nodes:
            if node.customTitle == customName:
                node.evalImplementation()

    def getSceneInstances(self):
        return self.scene

    def getNodesInstances(self):
        return self.scene.nodes
    
    def getNodeFromId(self, nodeId: int):
        for node in self.scene.nodes:
            if node.id == nodeId:
                return node
            
    def getNodeFromCustomName(self, customName: str):
        for node in self.scene.nodes:
            if node.customTitle == customName:
                return node

    def listNodesInScene(self):
        return self.scene.nodes


iter_instance = Build()

