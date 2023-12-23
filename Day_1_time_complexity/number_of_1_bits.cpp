// Write a function that takes an integer and returns the number of 1 bits present in its binary representation.


// Problem Constraints
// 1 <= A <= 109


// Input Format
// First and only argument contains integer A


// Output Format
// Return an integer


// Example Input
// Input 1:
// 11
// Input 2:
// 6


// Example Output
// Output 1:
// 3
// Output 2:
// 2


// Example Explanation
// Explaination 1:
// 11 is represented as 1011 in binary.
// Explaination 2:
// 6 is represented as 110 in binary.

//##########################################
int numSetBits(int A) {
    int count=0;
    while(A>0){
        if(A&1)
            count++;
        A>>=1;
    }
    return count;
}

int main(){
    cout<<numSetBits(11)<<endl;
    return 0;
}