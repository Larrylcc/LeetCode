from Solution import Solution

def main():
    solution_instance=Solution()
    g=[1,2,3]
    s=[1,1]
    result = solution_instance.findContentChildren(g,s)
    print(result)

if __name__ == '__main__':
    main()