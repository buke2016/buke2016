#include <iostream>
#Here are the changes I made:

#Replaced <iostream.h> with <iostream> since the <iostream.h> header is not standard and outdated.
#Changed cout and cin to std::cout and std::cin because they are part of the std namespace.
#Replaced NULL with nullptr for memory allocation error checking, which is the modern and safer way to check for null pointers.
#Added comments to explain the purpose of various parts of the code.
#Cleaned up formatting for readability.

int main()
{
    int i, n;
    int *p;
    std::cout << "How many numbers would you like to type? ";
    std::cin >> i;
    p = new int[i]; // Allocate memory at runtime from the Heap

    if (p == nullptr) // Use nullptr instead of NULL
    {
        std::cout << "Error: memory could not be allocated";
    }
    else
    {
        for (n = 0; n < i; n++)
        {
            std::cout << "Enter number: ";
            std::cin >> p[n];
        }
        int *k = p; // To hold the base address of the dynamic array
        std::cout << "You have entered: \n";
        for (n = 0; n < i; n++)
        {
            std::cout << *k << ", ";
            k++;
        }
        std::cout << "\n";
        delete[] p; // Release the memory to return it to the Heap
    }

    return 0;
}

