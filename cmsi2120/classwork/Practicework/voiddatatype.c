#include <stdio.h>
void addition(int a, int b);
int main(){
	int x=10;
	int y=20;
	addition(x,y);
	void *ptr;
	ptr=&x;
	printf("\n Value stored in pointer(ptr) after dereferencing %d",*((int *)ptr));
	return 0;
}
void addition(int a,int b){
	int sum=a+b;
	printf("The sum of x and y is %d",sum);
}