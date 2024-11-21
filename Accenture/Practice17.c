// Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.
// Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.
// Test Cases:
// TestCase 1:
// Input :
// 10 , 80
// Expected Result:
// 11 , 22 , 33 , 44 , 55 , 66 , 77.
// Test Case 2:
// Input:
// 100,200
// Expected Result:
// 101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.


#include <stdio.h>

int isPalindrome(int num){
    int temp = num, rev = 0;
    while(temp != 0){
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    return rev == num;
}

int main(){
    int lower, upper;
    printf("Enter the lower limit: ");
    scanf("%d", &lower);
    printf("Enter the upper limit: ");
    scanf("%d", &upper);

    for(int i = lower; i <= upper; i++){
        if(isPalindrome(i)){
            printf("%d, ", i);
        }
    }
}