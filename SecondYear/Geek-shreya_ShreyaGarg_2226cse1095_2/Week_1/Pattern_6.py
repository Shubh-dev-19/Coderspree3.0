#User function Template for python3

class Solution:
    def printTriangle(self, N):
        k=0
        for i in range(1,N+1):
            for j in range(1,(N-i)+1):
                print(end = " ")
            while k!=(2*i-1):
                print("*", end="")
                k += 1
   
            k = 0
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends