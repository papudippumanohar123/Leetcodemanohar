#User function Template for python3

class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        return (a+b)%(10**9+7)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        ob=Solution()
        print(ob.sumUnderModulo(a,b))

# } Driver Code Ends