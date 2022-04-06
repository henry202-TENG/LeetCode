#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
import queue


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 從0開始走，往外一圈如果不是0則加一，並與該位置已有的距離值比較，選小的
        m = len(mat)
        n = len(mat[0])

        def BFS(A, q):
            while q:
                r, c = q.pop(0)
                d = A[r][c] + 1
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < m and 0 <= nc < n and A[nr][nc] > d:
                        A[nr][nc] = d
                        q.append([nr, nc])
            return A


        res = [[1000000 for _ in range(n)] for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
                    res[i][j] = 0
        res = BFS(res, q)

        return res

    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        def BFS(deep, queue):
            #print(queue, deep)
            if deep >= self.smallest_deep:
                return
            q_len = len(queue)

            for _ in range(q_len):
                node = queue.pop(0)
                i = node[0]
                j = node[1]

                hash.append([i, j])

                if mat[i][j] == 0:
                    self.smallest_deep = min(deep, self.smallest_deep)
                    return
                if (0 <= i+1 < m) and (0 <= j < n) and [i+1, j] not in hash:
                    queue.append([i+1, j])
                if (0 <= i-1 < m) and (0 <= j < n) and [i-1, j] not in hash:
                    queue.append([i-1, j])
                if (0 <= i < m) and (0 <= j+1 < n) and [i, j+1] not in hash:
                    queue.append([i, j+1])
                if (0 <= i < m) and (0 <= j-1 < n) and [i, j-1] not in hash:
                    queue.append([i, j-1])
            BFS(deep+1, queue)

        res = [[1000000 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
        for i in range(m):
            for j in range(n):
                # 每個位置走一次BFS太花時間，需要結合DP的概念，可以減少一半
                if res[i][j]:
                    self.smallest_deep = res[i][j]
                    hash = []
                    BFS(0, [[i, j, 0, 0]])
                    res[i][j] = self.smallest_deep

        return res
    '''
        
# @lc code=end

