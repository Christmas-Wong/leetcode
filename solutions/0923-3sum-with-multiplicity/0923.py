class Solution:
    def threeSumMulti(self, num_list: List[int], target: int) -> int:
        mod = 10**9+7
        num_list.sort(reverse=False)
        return_num = 0
        start = 0
        length = len(num_list)
        if num_list[0] == num_list[-1]:
            count = length * (length-1)/6
            count %= mod
            count *= (length-2)
            count %= mod
            return int(count)
        while start <= length-2:
            middle = start+1
            end = length-1
            while middle < end:
                mid_num = 0
                end_num = 0
                three_sum = num_list[start] + num_list[middle] + num_list[end]
                if three_sum < target:
                    middle += 1
                    continue
                if three_sum > target:
                    end -= 1
                    continue
                elif num_list[middle] != num_list[end]:
                    mid_num += 1
                    end_num += 1
                    while middle+1 < end and num_list[middle] == num_list[middle+1]:
                        mid_num += 1
                        middle += 1
                    while end-1 > middle and num_list[end] == num_list[end-1]:
                        end_num += 1
                        end -= 1
                    return_num += mid_num*end_num
                    return_num %= mod
                    middle += 1
                    end -= 1
                else:
                    count = end - middle + 1
                    return_num += count * (count - 1) / 2
                    return_num %= mod
                    break
            start += 1
        return int(return_num)