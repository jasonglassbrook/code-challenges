#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

#-----------------------------------------------------------


class Solution:

    MAIN = "isSubtree"

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        pass

    ############################################################
    #   Strategies
    ############################################################

    def isSubtree__recursive(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Uses recursion.
        """

        pass

    def isSubtree__iterative__depth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        from collections import deque as Deck

        pass

    def isSubtree__iterative__breadth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        pass

    ############################################################
    #   Common Tools
    ############################################################

    def is_same_branch(
        self,
        p: Union[TreeNode, None],
        q: Union[TreeNode, None],
    ) -> Union[bool, None]:

        # If both are empty trees, they are the same.
        if not p and not q:
            return True

        # Now, if only one is empty, they are not the same.
        # If we got here, then we ruled out both being empty.
        if not p or not q:
            return False

        # Now, both must be non-empty...

        # If their values are not equal, they are not the same. (Duh!)
        if p.val != q.val:
            return False

        # Inconclusive.
        # We must test if both their left and right branches are equal.
        return None


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    def test_example_1(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, 2], 5]),
                tree_from_data([4, 1, 2]),
            ],
            answer=True,
        )

    def test_example_2(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, [2, 0, None]], 5]),
                tree_from_data([4, 1, 2]),
            ],
            answer=False,
        )

    def test_empty_trees(self):

        return self.run_test(
            args=[
                tree_from_data([]),
                tree_from_data([]),
            ],
            answer=True,
        )

    def test_equal_trees_of_depth_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, None, None]),
                tree_from_data([1, None, None]),
            ],
            answer=True,
        )

    def test_unequal_trees_of_depth_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, None, None]),
                tree_from_data([2, None, None]),
            ],
            answer=False,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)
