//https://youtu.be/V97oYgN9cIE?list=PLIY8eNdw5tW_zX3OCzX7NJ8bL1p6pWfgG
//Binary Search Tree (BST) | Implementation(with Full Code) | Part 1 - Setup
#include<iostream>
#define SPACE 10

using namespace std;

class TreeNode
{
    public:
      int value;
      TreeNode *left;
      TreeNode *right;
      
      TreeNode()
      {
          value = 0;
          left = NULL;
          right = NULL;
      }
      TreeNode(int v)
      {
          value = v;
          left = NULL;
          right = NULL;
      }
};

class BST{
    public:
    TreeNode *root;
    bool isEmpty()
    {
        if(root==NULL)
          return true;
        else
          return false;
    }
    
};

void insertNode(TreeNode *new_Node)
{
    
}

void print2D(TreeNode *r, int space)
{
    if (r == NULL) // Base case
        return;
    space += SPACE; // Increase distance between levels
    print2D(r->right, space); // Process right child first
    cout<<endl;
    for(int i = SPACE; i < space; i++) // Print current node after space count
        cout<<"";
    cout<<r->value<<"\n";
    print2D(r->left, space); // Process left child
}

int main()
{
    int option;
    
    
    do
    {
        cout<<"What operation do you want to perform "
        <<"Select Option number. Enter 0 to exit."<<endl;
        cout<<"1.Insert Node"<<endl;
        cout<<"2.Search Node"<<endl;
        cout<<"3.Delete Node"<<endl;
        cout<<"4.Print BST values"<<endl;
        cout<<"5.Clear Screen"<<endl;
        cout<<"0.Exit Program"<<endl;
        
        cin>>option;
        
        switch(option)
        {
            case 0:
                break;
            case 1:
                cout<<"INSERT"<<endl;
                break;
            case 2:
                cout<<"SEARCH"<<endl;
                break;
            case 3:
                cout<<"DELETE"<<endl;
                break;
            case 4:
                cout<<"PRINT and Traverse"<<endl;
                break;
            case 5:
                //cout<<"CLR SCR"<<endl;
                system("cls");
                break;
            default:
                cout<<"Enter Proper Option Number"<<endl;

        }
    }
    while(option!=0);
    return 0;
}
