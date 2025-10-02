from Solution import Solution

def main():
    solution_instance=Solution()
    intervals =[[1,2],[2,3],[3,4],[1,3]]
    result = solution_instance.eraseOverlapIntervals(intervals)
    print(result)

if __name__ == '__main__':
    main()