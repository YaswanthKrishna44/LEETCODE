class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores indices in decreasing order of value
        result = []

        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()

        # 2. Maintain monotonic decreasing order
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

        # 3. Append maximum of current window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result