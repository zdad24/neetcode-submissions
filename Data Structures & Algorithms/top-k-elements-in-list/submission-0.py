class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        freq = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for key, value in count.items():
            freq.append((value, key))
        
        freq.sort(reverse = True)

        for key, value in freq:
            if k == 0:
                break
            answer.append(value)
            k-=1
        
        return answer