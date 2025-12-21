from Solution import Solution

def main():
    solution_instance=Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    ans = solution_instance.minWindow(s,t)
    print(ans)

if __name__ == '__main__':
    main()