class Solution:

  def findNumberOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return 0

    length = [1] * n
    count = [1] * n

    for i in range(n):
      for j in range(i):
        if nums[i] > nums[j]:
          if length[j] + 1 > length[i]:
            # Found a strictly longer subsequence ending at i
            length[i] = length[j] + 1
            count[i] = count[j]
          elif length[j] + 1 == length[i]:
            # Found another valid subsequence of the same maximum length
            count[i] += count[j]

    max_len = max(length)
    # Sum up counts of all indices that achieve the max_len
    return sum(c for l, c in zip(length, count) if l == max_len)