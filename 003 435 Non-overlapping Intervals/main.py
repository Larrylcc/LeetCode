from Solution import Solution

def main():
    solution_instance=Solution()
    intervals =[1, 0, 2]
    result = solution_instance.eraseOverlapIntervals(intervals)
    print(result)

if __name__ == '__main__':
    main()