class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        target_arr=[]
        source_arr=[]
        for num in nums:
            if num>=0:
                target_arr.append(num)
            else:
                source_arr.append(num)
        result = []
        i, j = 0, 0  # Pointers for target_arr and source_arr respectively

    # Weave the two lists together
        while i < len(target_arr) and j < len(source_arr):
            result.append(target_arr[i])  # Add element from target (even pos)
            result.append(source_arr[j])  # Add element from source (odd pos)
            i += 1
            j += 1
    
    # Add any remaining elements from either list
        result.extend(target_arr[i:])
        result.extend(source_arr[j:])
        return result

        