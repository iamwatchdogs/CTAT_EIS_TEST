// Problem Statement:
// Given a binary search tree, Check whether the left side of  tree can be mirrored by changing the right side part alone. Your task is to complete the can_mirror() function  which receives root of binary search tree.If mirroring can be done return 1, else return 0. Draw the sample for better understanding. Structure for binary search tree is predefined, refer it for coding. 

// inp:          

//               1      

//        2                 3

// 6        9        10        12 

// out:Yes 

// inp:            

//                   1    

//          2              3 

//  9                10        11 

// out:No



// Input Format:
// No need to accept any input as it is predefined ,complete the function part.


// Output Format:
// Return 1 if right side of the tree can be mirrored , else return 0


// Constraints:
// 1 <= Num <= 10^5


// Sample Input 1:
// 30 20 50 10 25 40 -1


// Sample Output 1:
// NO


// Sample Input 2:
// 5 3 8 10 1 -1


// Sample Output 2:
// YES

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct node{
  int data;
  struct node* left;   
  struct node* right;
};

struct node* new_node(int data){   
  struct node* node = (struct node*)malloc(sizeof(struct node));   
  node->data = data;   
  node->left = NULL; 
  node->right = NULL; 
  return(node);
}

struct node* insert_node(struct node* node, int data){  
  if (node == NULL)
    return new_node(data);  
  if (data < node->data)
    node->left = insert_node(node->left, data);
  else
    node->right = insert_node(node->right, data);
  return node;
}

struct node* clone_tree (struct node* root) {
  if(root == NULL)
    return NULL;
  struct node* newNode = new_node(root->data);
  newNode->left = clone_tree(root->left);
  newNode->right = clone_tree(root->right);
  return newNode;
}

bool are_mirror(struct node* a, struct node* b){
  if (a == NULL && b == NULL)
    return true;
  if (a == NULL || b == NULL)
    return false;
  return are_mirror(a->left, b->right) && are_mirror(a->right, b->left);
}

bool can_mirror(struct node* root){ 
  if ( root == NULL )
    return true;
  struct node* cloned_root = clone_tree(root);
  return are_mirror(root,cloned_root);
}

int main(){   
  struct node* root = NULL;
  int data, flag = 0, len = 0;  
  int arr[50];   
  while (scanf("%d", &data) != EOF) {   
    if (data == -1)  
      break;     
    root = insert_node(root, data);    
    arr[len++] = data;  
  }
  if (can_mirror(root))  
    printf("YES\n");   
  else
    printf("NO\n");
  return 0;
}
