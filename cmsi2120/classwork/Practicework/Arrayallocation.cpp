// array allocation to set the size of its array at runtime.
#include <iostream>
int main ()
{
int i,n;
int *p;
 cout << "How many numbers would you like to type? ";
 cin >> i;
 p= new int[i]; // it takes memory at run-time from Heap
if (p == NULL)
 cout << "Error: memory could not be allocated";
else
 {
for (n=0; n<i; n++)
 {
 cout << "Enter number: ";
 cin >> p[n];
 }
int *k=p; // to hold the base address of dynamic array
cout << "You have entered: \n";
for (n=0; n<i; n++)
{ cout << *k<< ", "; k++;}
 cout<<"\n";
 delete[] p; // it release the memory to send it back to Heap
 }
 return 0;
}