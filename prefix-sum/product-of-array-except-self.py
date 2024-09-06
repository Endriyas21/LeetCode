class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # Initialize the prefix and postfix product lists
        prefix_products = [1] * length
        postfix_products = [1] * length
        answer = [1] * length
        
        # Calculate prefix products
        for i in range(1, length):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
        
        # Calculate postfix products
        for i in range(length - 2, -1, -1):
            postfix_products[i] = postfix_products[i + 1] * nums[i + 1]
        
        # Calculate the answer array
        for i in range(length):
            answer[i] = prefix_products[i] * postfix_products[i]
        
        return answer