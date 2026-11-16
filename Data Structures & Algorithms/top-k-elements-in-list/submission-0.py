class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        bucket = [[] for x in range(len(nums) + 1)]
        result = []
        for number,freq in count.items():
            bucket[freq].append(number)

        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result