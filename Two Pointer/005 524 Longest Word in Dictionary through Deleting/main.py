from Solution import Solution

def main():
    solution_instance=Solution()
    s="abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    ans = solution_instance.findLongestWord(s, dictionary)
    print(ans)

if __name__ == '__main__':
    main()