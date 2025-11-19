from Solution import Solution


def main():
    solution_instance = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    str = solution_instance.minWindow(s, t)
    print(str)


if __name__ == "__main__":
    main()
