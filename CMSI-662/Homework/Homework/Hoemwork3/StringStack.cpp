#include <iostream>
#include <memory>
#include <stdexcept>
#include <vector>

using namespace std;

class StringStack {
private:
    vector<string> stackArray; 

public:
    StringStack() = default; 

    void push(const string& item) {
        stackArray.push_back(item); 
    }

    string pop() {
        if (isEmpty()) {
            throw out_of_range("Stack is empty"); 
        }
        string item = move(stackArray.back()); 
        stackArray.pop_back(); 
        return item;
    }

    string peek() const {
        if (isEmpty()) {
            throw out_of_range("Stack is empty");
        }
        return stackArray.back(); 
    }

    bool isEmpty() const {
        return stackArray.empty(); 
    }

    size_t size() const {
        return stackArray.size(); 
    }
};

int main() {
    try {
        StringStack stack;
        stack.push("Bye");
        stack.push("Peter");

        cout << "Top of the stack: " << stack.peek() << endl;
        cout << "Stack size before pop: " << stack.size() << endl;

        cout << "Popped: " << stack.pop() << endl;
        cout << "Top of the stack after pop: " << stack.peek() << endl;
        cout << "Stack size after pop: " << stack.size() << endl;
    } catch (const exception& e) {
        cerr << "Exception caught: " << e.what() << endl;
    }

    return 0;
}
