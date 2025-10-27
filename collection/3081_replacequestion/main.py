from typing import List

class Solution:
      def minimizeStringValue(self, s: str) -> str:
          freq = Counter(s)
          heap = []
          for i in range(26):
              ch = chr(i + ord('a'))
              heapq.heappush(heap, (freq[ch], ch))
          tmp = []
          for ch in s:
              if ch != '?': continue    
              f, ch = heapq.heappop(heap)
              tmp.append(ch)
              heapq.heappush(heap, (f + 1, ch))
          tmp.sort()
          idx = 0
          res = []
          for ch in s:
              if ch == '?':
                  res.append(tmp[idx])
                  idx += 1
              else:
                  res.append(ch)
          return "".join(res)
