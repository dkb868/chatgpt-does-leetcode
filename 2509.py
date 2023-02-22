"""solve in python3, just give a code block.

You are given an integer n. There is a complete binary tree with 2n - 1 nodes. The root of that tree is the node with the value 1, and every node with a value val in the range [1, 2n - 1 - 1] has two children where:

The left node has the value 2 * val, and
The right node has the value 2 * val + 1.
You are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each query, solve the following problem:

Add an edge between the nodes with values ai and bi.
Find the length of the cycle in the graph.
Remove the added edge between nodes with values ai and bi.
Note that:

A cycle is a path that starts and ends at the same node, and each edge in the path is visited only once.
The length of a cycle is the number of edges visited in the cycle.
There could be multiple edges between two nodes in the tree after adding the edge of the query.
Return an array answer of length m where answer[i] is the answer to the ith query.

 

Example 1:


Input: n = 3, queries = [[5,3],[4,7],[2,3]]
Output: [4,5,3]
Explanation: The diagrams above show the tree of 23 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 3 and 5, the graph contains a cycle of nodes [5,2,1,3]. Thus answer to the first query is 4. We delete the added edge and process the next query.
- After adding the edge between nodes 4 and 7, the graph contains a cycle of nodes [4,2,1,3,7]. Thus answer to the second query is 5. We delete the added edge and process the next query.
- After adding the edge between nodes 2 and 3, the graph contains a cycle of nodes [2,1,3]. Thus answer to the third query is 3. We delete the added edge.
Example 2:


Input: n = 2, queries = [[1,2]]
Output: [2]
Explanation: The diagram above shows the tree of 22 - 1 nodes. Nodes colored in red describe the nodes in the cycle after adding the edge.
- After adding the edge between nodes 1 and 2, the graph contains a cycle of nodes [2,1]. Thus answer for the first query is 2. We delete the added edge.
 

Constraints:

2 <= n <= 30
m == queries.length
1 <= m <= 105
queries[i].length == 2
1 <= ai, bi <= 2n - 1
ai != bi

---

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
"""


from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # build the binary tree graph
        graph = {}
        for i in range(1, 2 * n):
            graph[i] = []
            if i * 2 < 2 * n:
                graph[i].append(i * 2)
            if i * 2 + 1 < 2 * n:
                graph[i].append(i * 2 + 1)


        def search(start, target, visited):
            """
            Modified DFS to search for target and return the length of the cycle.
            """
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor == target and len(visited) > 2:
                    # found target for the second time, cycle detected
                    return len(visited) - 1
                if neighbor not in visited:
                    result = search(neighbor, target, visited.copy())
                    if result is not None:
                        return result
            return None


        result = []
        for query in queries:
            # add the edge
            graph[query[0]].append(query[1])
            graph[query[1]].append(query[0])
            # search for cycle
            length = search(query[0], query[0], set())
            # remove the edge
            graph[query[0]].remove(query[1])
            graph[query[1]].remove(query[0])
            result.append(length if length is not None else -1)
        return result


