#include <stdio.h>
int main() {
	int ar[]={7,5,3,8,9};
	int i,j;
	float sum=0,average=0;
	printf("The array elements are: \n");
	for(i=0;i<5;i++){
		printf("%d \t",ar[i]);
	}
	int marks[5];
	printf("\nEnter Marks: \n");
	for(j=0;j<5;j++) {
		scanf("%d",&marks[i]);
		sum =sum + marks[i];
	}
	average=(sum/5);
	printf("The average is %f",average);
	return 0;
}