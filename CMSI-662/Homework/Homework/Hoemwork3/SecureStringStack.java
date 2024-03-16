import java.util.ArrayList;
import java.util.EmptyStackException;

class SecureStringStack {
    private ArrayList<String> stackList;

    public SecureStringStack() {
        this.stackList = new ArrayList<>();
    }

    // Pushes a new string onto the stack
    public void push(String item) {
        stackList.add(item);
    }

    
    public String pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return stackList.remove(stackList.size() - 1);
    }

    
    public String peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return stackList.get(stackList.size() - 1);
    }

    // Checks if the stack is empty
    public boolean isEmpty() {
        return stackList.isEmpty();
    }

    // Returns the size of the stack
    public int size() {
        return stackList.size();
    }

    public static void main(String[] args) {
        SecureStringStack stack = new SecureStringStack();
        try {
            stack.push("Bye");
            stack.push("Peter");

            System.out.println("Top of the stack: " + stack.peek()); 
            
            System.out.println("Popped from the stack: " + stack.pop()); 
            System.out.println("Popped from the stack: " + stack.pop()); 

            
            System.out.println("Popped from the stack: " + stack.pop());
        } catch (EmptyStackException e) {
            System.out.println("Attempted to pop from an empty stack.");
        }
    }
}
