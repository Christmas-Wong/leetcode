def exchange(nums):
    if nums is None or len(nums) < 1:
        return nums
    m, n = 0, len(nums)-1
    while m < n:
        while m < n and not judge(nums[m]):
            m += 1
        while m < n and judge(nums[n]):
            n -= 1
        if m < n:
            mid_num = nums[m]
            nums[m] = nums[n]
            nums[n] = mid_num
            m += 1
            n -= 1
    return nums


def judge(num):
    return num % 2 == 0


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(exchange(num_list))