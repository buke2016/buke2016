#include <stdio.h>
enum week{Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday};
int main(){
	printf("Value of Wednesday %d",Wednesday);
	enum week day;
	day=Saturday;
	printf("\n Value stored in the variable day %d",day);
	printf("\n The value of each enum constant: \n");
	for(int i=Monday;i<=Sunday;i++)
	{
		printf("%d \t",i);
	}
	return 0;
}