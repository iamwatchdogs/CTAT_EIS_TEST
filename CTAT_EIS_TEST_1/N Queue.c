// Problem Statement:
// The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.

// Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number.

// X  Q  X  X

// X  X  X  Q

// Q  X  X  X

// X  X  Q  X





// Example 1:

// Input:

// 4

// Output:

// [2 4 1 3 ] [3 1 4 2 ]

// Explaination:

// These are the 2 possible solutions.







// Example 2:

// Input:

// 2

// Output:

// -1

// Explaination:

// Two queen cannot be placed 




// Input Format:
//  Enter the integer as a input 


// Output Format:
// Display the output


// Constraints:
// 1 ≤ n ≤ 10


// Sample Input :
// 5


// Sample Output :
// [1 3 5 2 4 ] [1 4 2 5 3 ] [2 4 1 3 5 ] [2 5 3 1 4 ] [3 1 4 2 5 ] [3 5 2 4 1 ] [4 1 3 5 2 ] [4 2 5 3 1 ] [5 2 4 1 3 ] [5 3 1 4 2 ]

#include <stdio.h>
#include <stdlib.h>
#define MAX_N 20

int board[MAX_N], count;

int abs(int x) {    return (x < 0) ? -x : x;  }

int is_valid(int row, int col) { 
  int i;  
  for (i = 1; i <= row - 1; i++) {  
    if (board[i] == col || abs(board[i] - col) == abs(i - row)) { 
      return 0;    
    }  
  } 
  return 1;
}

  
void print_board(int n) { 
  int i; 
  printf("[");  
  for (i = 1; i <= n; i++) {    
    printf("%d ", board[i]);   
  } 
  printf("] ");
}  

void solve(int row, int n) { 
  int col;  
  for (col = 1; col <= n; col++) {       
    if (is_valid(row, col)) {   
      board[row] = col;   
      if (row == n) {     
        print_board(n);    
      } 
      else {    
        solve(row + 1, n); 
      }  
    }  
  }
}    

int main() {   
  int n; 
  scanf("%d", &n);  
  solve(1, n);     
  return 0;
};
