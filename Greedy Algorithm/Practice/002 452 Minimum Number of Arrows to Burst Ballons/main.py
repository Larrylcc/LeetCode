from Solution import Solution

def main():
    solution_instance=Solution()
    array =[[1,2],[2,3],[3,4],[4,5]]
    result = solution_instance.findMinArrowShots(array)
    print(result)

if __name__ == '__main__':
    main()