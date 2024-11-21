// Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.
// Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.
// Test Cases:
// Test Case 1:
// Input:
// 5
// Expected Result Value:
// 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
// 275
// Test Case 2:
// Input:
// 12
// Expected Result Value:
// 12, 24, 36, 48, 60, 72, 84, 96, 108, 120
// 660


#include <stdio.h> 

int main() 
{
    int num, i, sum = 0;
    printf("Enter a number: ");
    scanf("%d", &num);
    for(i = 1; i <= 10; i++)
    {
        printf("%d, ", num * i);
        sum += num * i;
    }
    printf("\n%d", sum);
    return 0;
}