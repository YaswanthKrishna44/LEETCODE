class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        queue=deque([0])
        visited={0}
        coin_count=0
        while queue:
            coin_count+=1
            for _ in range(len(queue)):
                curr=queue.popleft()
                for coin in coins:
                    nxt=curr+coin
                    if nxt==amount:
                        return coin_count
                    if nxt<amount and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return -1

        