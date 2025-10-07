from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        def add(a1, a2):
            for i in range(len(a1)):
                a1[i] += a2[i]

        def dfs(node):
            visited.add(node)
            cnt = [0] * 26
            li = ord(labels[node]) - ord('a')
            for child in tree[node]:
                if child in visited:
                    continue
                child_cnt = dfs(child)
                add(cnt, child_cnt)
            cnt[li] += 1
            res[node] = cnt[li]
            return cnt

        # Build a tree
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        # Use during dfx
        visited = set()
        res = [0] * n
        dfs(0)

        return res
