from Solution import Solution
from Review import Review

def main():
    solution_instance=Review()
    head = [3,2,0,-4]
    pos = 1
    ans = solution_instance.detectCycle(head, pos)
    print(ans)

if __name__ == '__main__':
    main()