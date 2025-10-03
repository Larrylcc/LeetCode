from Solution import Solution

def main():
    solution_instance=Solution()
    array =[1,0,0,0,1]
    result = solution_instance.canPlaceFlowers(array,2)
    print(result)

if __name__ == '__main__':
    main()