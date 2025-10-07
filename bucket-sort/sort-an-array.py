class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l,m,r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i,j,k = 0,0,l
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            
            while i < len(left):
                arr[k] = left[i]
                i, k = i+1, k+1
            while j < len(right):
                arr[k] = right[j]
                j, k = j+1, k+1

        def mergSort(arr,l,r):
            if l == r:
                return arr
            m = (l+r)//2
            mergSort(arr,l,m)
            mergSort(arr,m+1,r)
            merge(arr, l,m,r)
            return arr
        return mergSort(nums, 0, len(nums)-1)