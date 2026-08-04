from exercise import Solution

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")
    print()
    
    # Test case 2
    nums = [3, 2, 4]
    target = 6
    result = sol.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [1, 2]")
    print()
    
    # Test case 3
    nums = [3, 3]
    target = 6
    result = sol.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Expected: [0, 1]")