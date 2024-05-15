// Problem Description
// Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

// Problem Constraints
// 1 <= |A| <= 100000

// Input Format
// First and only argument is the vector A

// Output Format
// Return one integer, the answer to the question

// Example Input
// Input 1:
// A = [0, 1, 0, 2]
// Input 2:
// A = [1, 2]

// Example Output
// Output 1:
// 1
// Output 2:
// 0


// Example Explanation
// Explanation 1:
// 1 unit is trapped on top of the 3rd element.

// Explanation 2:
// No water is trapped.

//################################################
int trap(vector<int> &A) {
    int prefixMax[A.size()];
    int suffixMax[A.size()];

    prefixMax[0]=A[0];
    suffixMax[A.size()-1] = A[A.size()-1];

    for(int i=1;i<A.size();i++){
        prefixMax[i] = max(A[i],prefixMax[i-1]);
    }

    for(int i=A.size()-2;i>=0;i--){
        suffixMax[i] = max(A[i],suffixMax[i+1]);
    }

    int water=0;
    for(int i=1;i<A.size()-1;i++)
    {
        water += (min(prefixMax[i],suffixMax[i]) - A[i]);
    }
    return water;
}
