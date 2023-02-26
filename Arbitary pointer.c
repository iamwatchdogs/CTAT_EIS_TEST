// Problem Statement:
// Given a linked list with next pointer and arbitrary pointer.Initially arbitrary pointer points to NULL. Make the arbitrary pointer to point to maximum value in right side of the list.Your task is to complete the fill_arb() function which recieves the starting address of the linked list as input.


// Input Format:
// No need to accept any input as it is already defined ,complete the function part.


// Output Format:
// No need print anything as it is predefined


// Constraints:
// 1 <= Num <= 10^5


// Sample Input 1:
// 30 52 13 69 97 35 87 44 37 24 60 74 61 91 18 -1


// Sample Output 1:
// 30 (97) -> 52 (97) -> 13 (97) -> 69 (97) -> 97 (NULL) -> 35 (91) -> 87 (91) -> 44 (91) -> 37 (91) -> 24 (91) -> 60 (91) -> 74 (91) -> 61 (91) -> 91 (NULL) -> 18 (NULL)


// Sample Input 2:
// 32 94 49 20 22 52 46 33 17 60 -1


// Sample Output 2:
// 32 (94) -> 94 (NULL) -> 49 (60) -> 20 (60) -> 22 (60) -> 52 (60) -> 46 (60) -> 33 (60) -> 17 (60) -> 60 (NULL)


// Sample Input 3:
// 76 50 34 18 87 15 48 31 60 57 14 61 92 90 32 19 79 74 82 59 41 91 13 84 63 49 93 64 72 53 27 44 46 17 42 55 45 40 47 16 81 56 83 43 62 -1


// Sample Output 3:
// 76 (93) -> 50 (93) -> 34 (93) -> 18 (93) -> 87 (93) -> 15 (93) -> 48 (93) -> 31 (93) -> 60 (93) -> 57 (93) -> 14 (93) -> 61 (93) -> 92 (93) -> 90 (93) -> 32 (93) -> 19 (93) -> 79 (93) -> 74 (93) -> 82 (93) -> 59 (93) -> 41 (93) -> 91 (93) -> 13 (93) -> 84 (93) -> 63 (93) -> 49 (93) -> 93 (NULL) -> 64 (83) -> 72 (83) -> 53 (83) -> 27 (83) -> 44 (83) -> 46 (83) -> 17 (83) -> 42 (83) -> 55 (83) -> 45 (83) -> 40 (83) -> 47 (83) -> 16 (83) -> 81 (83) -> 56 (83) -> 83 (NULL) -> 43 (62) -> 62 (NULL)

#include <stdio.h>
#include <stdlib.h>

struct Node {    
  int data;
  struct Node *next;
  struct Node *arbitrary;
};

void fill_arb(struct Node *head) {  
  struct Node *temp = head;
  while(temp) {
    struct Node *curr = temp->next;
    struct Node *max = NULL;
    while(curr) {
      if(curr->data > temp->data && (!max || curr->data > max->data)) { 
        max = curr;
      }
      curr = curr->next;
    }
    temp->arbitrary = max;
    temp = temp->next;
  }
}

void print_list(struct Node *head) { 
  while(head) {  
    printf("%d (", head->data); 
    if(head->arbitrary) {      
      printf("%d", head->arbitrary->data);
    } 
    else {
      printf("NULL");
    }
    printf(")");
    if(head->next) {
      printf(" -> ");
    }
    head = head->next;
  }
  printf("\n");
}

int main()
{    
  int num; 
  struct Node *head = NULL, *temp = NULL;  
  
  scanf("%d", &num); 
  
  while(num != -1) { 
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = num;    
    new_node->next = NULL;      
    new_node->arbitrary = NULL; 
    if(!head) {      
      head = new_node; 
      temp = new_node; 
    }
    else {    
      temp->next = new_node;     
      temp = new_node;    
    }
    scanf("%d", &num); 
  }   
  fill_arb(head);
  print_list(head);
  return 0;
}
