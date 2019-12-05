def multiply(nums1, nums2):
    sign = -1 if (nums1[0] < 0) ^ (nums2[0] < 0) else 1

    nums1[0], nums2[0] = abs(nums1[0]), abs(nums2[0])

    result = [0] * (len(nums1) + len(nums2))

    for i in reversed(range(len(nums1))):
        for j in reversed(range(len(nums2))):
            result[i + j + 1] += nums1[i] * nums2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # remove leading zeroes
    result = result[next((i for i, x in enumerate(
        result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(multiply([3, 0, 0], [5, 1, 1]))
