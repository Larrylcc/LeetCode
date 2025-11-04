from Solution import Solution

def main():
    solution_instance=Solution()
    numbers=[2,7,11,15]
    target=9
    result = solution_instance.twoSum(numbers, target)
    print(result)

if __name__ == '__main__':
    main()