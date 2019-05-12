/******************************************************************************/
/******************************************************************************/
#include<iostream>
using namespace std ;

struct node{
    int data ; 
    node* next; 
} ; 

class list {
  private:
  node *head, *tail ; 
    public:
    int i ; 
    list(){
        head = NULL ; 
        tail = NULL ; 
    }
     
    

// Add item to end of  list
void create(int value)     
{
    node *temp = new node ;
    temp -> data = value ; 
    temp->next = NULL ; 
    if(head == NULL)
    {
        head = temp ; 
        tail = temp ; 
        temp = NULL ; 
    }
    else 
    {
       tail->next = temp ; 
        tail = temp; 
    }
}

void display(){
    node *temp = new node ;
    temp = head ; 
    while(temp != NULL){
        cout << temp->data << " " ; 
        temp = temp-> next ; 
    }
}

//insert data at start of list 
void insert_start(int value){
    node* temp = new node ; 
    temp->data = value ; 
    temp->next= head; 
    head = temp ; 
}

// insert node at position
void insert_pos(int value, int pos){
    node *pre = new node ; 
    node *cur = new node ; 
    node *temp = new node ; 
    cur = head; 
    for(i= 0 ; i< pos ; i++){
        pre = cur ; 
        cur = cur->next; 
    }
    temp->data = value ;
    pre->next = temp ;
    temp->next = cur ; 
     }

//delete first node 
void delete_first(){
    node * temp = new node ;
    temp = head; 
    head = head->next; 
    delete temp ; 
}

//delete last node
void delete_last(){
    node *pre = new node ; 
    node *cur = new node; 
    cur = head ; 
    while(cur->next != NULL){
        pre = cur; 
        cur = cur-> next; 
    }
    tail = pre; 
    pre->next = NULL ; 
    delete cur ; 
}
// Delete node at position
void delete_pos(int pos){
    node *pre = new node ; 
    node *cur = new node; 
    cur = head ; 
    for(i=0; i<pos ; i++){
    pre = cur  ; 
    cur = cur-> next ; 
    }
    pre->next = cur->next; 
    delete cur ; 
}

} ; 

int main(){
    list samp ; 
    samp.create(10) ; 
    samp.create(20) ; 
    samp.create(30) ; 
    samp.create(40) ; 
    cout << "\nDislay nodes in list " << "\t"       ; 
    samp.display() ; 
    cout << "\ninsert start "   << "\t"       ;  
    samp.insert_start(5) ; 
    samp.display() ; 
    cout << "\ninsert pos at 2 " << "\t"       ; 
    samp.insert_pos(105, 2)  ; 
    samp.display() ; 
    cout << "\ninsert pos at 4 " << "\t"       ; 
    samp.insert_pos(110, 4) ; 
    samp.display() ; 
    cout << "\ndelete pos at 2 " << "\t"       ; 
    samp.delete_pos(2) ; 
    samp.display() ; 
    cout << "\ndelete first " << "\t"       ; 
    samp.delete_first() ; 
    samp.display() ;
    cout << "\ndelete last " << "\t"       ; 
    samp.delete_last() ; 
    samp.display() ;
    
    return 0 ; 
}

/*
----------Output------------
Dislay nodes in list 	10 20 30 40 
insert start 	5 10 20 30 40 
insert pos 2 	5 10 105 20 30 40 
insert pos 4 	5 10 105 20 110 30 40 
delete pos 2 	5 10 20 110 30 40 
delete first 	10 20 110 30 40 
delete last 	10 20 110 30 

*/

