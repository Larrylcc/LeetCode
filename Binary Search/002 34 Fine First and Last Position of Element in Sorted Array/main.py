from Solution import Solution

def main():
    solution_instance=Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    result = solution_instance.searchRange(nums, target)
    print(result)

if __name__ == '__main__':
    main()