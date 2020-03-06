    def new_solution(nums):
        output = []
        if len(nums) < 3:
            return output
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p, q = i+1, len(nums) - 1
            while p < q:
                result = nums[i] + nums[p] + nums[q]
                if result < 0:
                    p += 1
                elif result > 0:
                    q -= 1
                else:
                    output.append([nums[i], nums[p], nums[q]])
                    while p < q and nums[p] == nums[p+1]:
                        p += 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1
                    p += 1
                    q -= 1
        return output