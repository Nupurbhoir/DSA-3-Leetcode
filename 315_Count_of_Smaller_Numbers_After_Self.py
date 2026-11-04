class Solution:
    def countSmaller(self, nums):

        n = len(nums)
        result = [0] * n

        indices = list(range(n))

        def mergeSort(left, right):

            if right - left <= 1:
                return

            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid, right)

            merged = []
            i = left
            j = mid
            right_count = 0

            while i < mid and j < right:

                if nums[indices[j]] < nums[indices[i]]:
                    merged.append(indices[j])
                    right_count += 1
                    j += 1

                else:
                    result[indices[i]] += right_count
                    merged.append(indices[i])
                    i += 1

            while i < mid:
                result[indices[i]] += right_count
                merged.append(indices[i])
                i += 1

            while j < right:
                merged.append(indices[j])
                j += 1

            indices[left:right] = merged

        mergeSort(0, n)

        return result
