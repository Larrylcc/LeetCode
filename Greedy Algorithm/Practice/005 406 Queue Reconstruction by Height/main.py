from Solution import Solution

def main():
    solution_instance=Solution()
    var=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    result = solution_instance.reconstructQueue(var)
    print(result)

if __name__ == '__main__':
    main()