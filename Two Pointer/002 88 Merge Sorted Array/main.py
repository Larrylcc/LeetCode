from Solution import Solution

def main():
    solution_instance=Solution()
    nums1=[2,0]
    m=1
    nums2=[1]
    n=1
    solution_instance.merge(nums1,m,nums2,n)
    print(nums1)

if __name__ == '__main__':
    main()