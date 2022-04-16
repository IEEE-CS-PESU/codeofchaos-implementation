#include<conio.h>
#include<stdio.h>
#include<stdlib.h>

struct node{
	char data; // int changed to char
	struct node *next;
	};
struct node *head=NULL;

struct node* createNode()
{
	struct node *newNode = (struct node *)malloc(sizeof(struct node*)); // 'struct node' changed to 'struct node*' inside sizeof
	return (newNode);
}

void insertNodeAtEnd()
{
	struct node *temp,*ptr;
	temp=createNode();
	printf("enter the data you want to insert:");
	scanf("%d",&temp->data);
	temp->next=NULL;
	if(head==NULL)
		head=temp;
	else{
		ptr=head;
		while(ptr->next!=NULL){
			ptr=ptr->next;
		}
	       ptr->next=temp;
	     }
}

void viewList(){
	struct node* temp=head;
	if(temp==NULL){
		printf("Empty list \n");
	}
	else{
	    printf("Our list is : \n");
		while(temp->next!=NULL)
		{
			printf("%d\t",temp->data);
			temp=temp->next;
		}
		printf("%d \t",temp->data);
	}
}
void reverseList(){
    struct node *prev, *current;
	if(head!=NULL){
		prev = head;
		current = head->next;
		// head = head->next; removed from this space
		prev->next=NULL;
		while(head!=NULL)
		{
			head=head->next;
			current->next=prev;
			prev = current;
			current=prev; // 'current = head' changed to 'current = prev'
		 }
		 head=prev;
}       


if(head!=NULL){
    printf("after reverse the list is :\n");
while(head->next!=NULL)
		{
			printf("%d\t",head->data);
			head=head->next;
		}
		printf("%d \t",head->data);

}else{
    printf("List is empty. Please insert some data in list \n");
}
}


int menu(){
	int choice;
	printf("\n 1.Append to list");
	printf("\n 2.View List");
	printf("\n 3.Reverse list ");
	printf("\n 4.exit");
	printf("\n Enter your choice: \t");
	scanf("%d",&choice);
	return(choice);
}

 void main(){
	while(1){
		switch(menu()){
			case 1:
				insertNodeAtEnd();
				break;
			case 2:
			    viewList();
			    break;
			case 3:
			    reverseList();
			    break;
			case 4:
				exit(0);
			default:
				printf("invalid choice");
		      }
			getch();
		  }

	}
