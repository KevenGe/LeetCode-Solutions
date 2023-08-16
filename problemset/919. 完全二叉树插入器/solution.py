# 919. 完全二叉树插入器
# https://leetcode.cn/problems/complete-binary-tree-inserter/

# Definition for a binary tree node.
from typing import Any, Callable, List, Tuple
from xml.etree.ElementPath import ops


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root: TreeNode = root
        
        def init_root(root:TreeNode) -> Tuple[List[TreeNode], List[TreeNode]]:
            
            par_nodes = [root]
            chi_nodes = []

            while True:
                for pn in par_nodes:
                    if pn.left is not None:
                        chi_nodes.append(pn.left)
                        if pn.right is not None:
                            chi_nodes.append(pn.right)
                    else:
                        break
                
                if len(chi_nodes) == 2 * len(par_nodes):
                    par_nodes = chi_nodes
                    chi_nodes = []
                else:
                    break
            
            return par_nodes, chi_nodes

        self.par_nodes, self.chi_nodes = init_root(root)

    def insert(self, val: int) -> int:
        if len(self.chi_nodes) == 2 * len(self.par_nodes):
            self.par_nodes = self.chi_nodes
            self.chi_nodes = []

        par_node = self.par_nodes[len(self.chi_nodes) // 2]
        chi_node = TreeNode(val)
        if len(self.chi_nodes) % 2 == 0:
            par_node.left = chi_node
        else:
            par_node.right = chi_node
        self.chi_nodes.append(chi_node)
        
        return par_node.val

    def get_root(self) -> TreeNode:
        return self.root



class CodeRun:
    def __init__(self, ops:List[Callable[[List[any]], Any]], vals:List[List[Any]]) -> None:
        self.ops = ops
        self.vals = vals

    def run(self):
        obj = eval(self.ops[0])(self.build_from_list(*self.vals[0]))
        print(obj)
        
        for op,val in zip(self.ops[1:], self.vals[1:]):
            print(getattr(obj, op)(*val))

    def build_from_list(self, root_vals:List[int]) -> TreeNode:
        if len(root_vals) == 0:
            return None

        c = CBTInserter(TreeNode(root_vals[0]))
        for root_val in root_vals[1:]:
            c.insert(root_val)
        
        return c.get_root()

if __name__ == "__main__":
    cr = CodeRun(["CBTInserter","insert","insert","get_root"],[[[1,2]],[3],[4],[]])
    cr.run()

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
