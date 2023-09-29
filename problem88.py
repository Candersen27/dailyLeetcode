class Solution:
    def merge(self, nums1, m, nums2, n):
        print('Under construction')

        
        for i in range(n):
            nums1.pop()
        
        nums1.extend(nums2)
        nums1.sort()




S = Solution

n1 = [-1,0,0,3,3,3,0,0,0]
n2 = [1,2,2]
S.merge(S, n1, 9, n2, 3)
print('---')
print(n1)