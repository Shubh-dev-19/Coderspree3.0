//{ Driver Code Starts
#include <iostream>

using namespace std;

// } Driver Code Ends
class Solution{
public:
	
	void printTriangle(int n) {
	    // code here
	     for(int i=n;i>=1;i--){
         for(int j=1;j<=i;j++)
           cout<<j<<" ";
         cout<<endl;
        }
	}
};