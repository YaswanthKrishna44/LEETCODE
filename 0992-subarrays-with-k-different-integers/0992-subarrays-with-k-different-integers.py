class Solution:

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMostK(k: int) -> int:
            if k <= 0:
                return 0
            freq = {}
            sub_counts = 0
            left = 0
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1
                # Use WHILE to shrink window until valid
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                sub_counts += right - left + 1
            return sub_counts
        # Exactly K = At Most K - At Most K-1
        return atMostK(k) - atMostK(k - 1)