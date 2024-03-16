// DCL60-CPP. Obey the one-definition rule
// compliant Example:
#include <iostream>
#include <initializer_list>
template<typename T>
void printAll(std::initializer_list<T> list) {
    for (const auto& item : list) {
        std::cout << item << ' ';
    }
    std::cout << '\n';
}
int main() {
    printAll({1, 2, 3, 4});
}

// Non-compliant Example:
#include <iostream>

// Non-compliant: No use of template or initializer list
void printAll(int list[ ], int size) { // Assumes int array
  for (int i = 0; i < size; ++i) {
    std::cout << list[i] << ' ';
  }
  std::cout << '\n';
}
int main() {
  int numbers[ ] = {1, 2, 3, 4};
  printAll(numbers, sizeof(numbers) / sizeof(numbers[0])); // Hardcoded array size
}

// EXP54-CPP. Do not access an object outside of its lifetime
//  Compliant Example:
#include <fstream>
void write_to_file(const char* filename) {
    std::ofstream file(filename);
    if (file.is_open()) {
        file << "Hello, World!";
        // File is automatically closed when the object goes out of scope
    }
}

//Non-compliant Example:
#include <fstream>
void write_to_file(const char* filename) {
  FILE* file = fopen(filename, "w"); // Use C-style file handling
  if (file != nullptr) {
    fprintf(file, "Hello, World!");
    // Manually close the file before going out of scope
    // Otherwise, leak occurs due to unclosed handle
    fclose(file);
  }
}

// CON50-CPP. Do not destroy a mutex while it is locked
// Compliant Example:
		#include <utility>
#include <string>
int main() {
    std::string str1 = "Hello, World!";
    std::string str2 = std::move(str1);
    // str1 should not be accessed in a way that assumes it contains valid data
    str1.clear();  // Make str1 explicitly empty, safe to use now
}

// Non-compliant Example:
// Accessing moved-from object directly:
#include <utility>
#include <string>

int main() {
    std::string str1 = "Hello, World!";
    std::string str2 = std::move(str1);

    // Non-compliant: Accessing str1 as if it still holds data
    char firstChar = str1[0]; // Undefined behavior!
    str1.clear(); // Clearing after potential usage is unnecessary
}
