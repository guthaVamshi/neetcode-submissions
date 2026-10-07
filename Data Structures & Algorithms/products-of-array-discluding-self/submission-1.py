class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
    # Initialize the output array with ones
        res = [1] * n
    
    # Calculate left products and store them in the result array
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
        
    # Calculate right products on the fly and multiply with the left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
    # Return the final product array
        return res
        






        