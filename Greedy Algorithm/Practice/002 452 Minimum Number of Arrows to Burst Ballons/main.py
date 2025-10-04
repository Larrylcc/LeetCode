from Solution import Solution

def main():
    solution_instance=Solution()
    array =[[10,16],[2,8],[1,6],[7,12]]
    result = solution_instance.findMinArrowShots(array)
    print(result)

if __name__ == '__main__':
    main()