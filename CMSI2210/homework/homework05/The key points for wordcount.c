The key points are:

- Check command line arguments to get filename
- Open file in read mode 
- Read file character by character using fgetc()
- Increment count when current char is whitespace and next char is not
- Handle EOF condition
- Close file when done
- Print final word count

This counts words separated by any whitespace like space, newline etc. Let me know if you need any clarification!


Code Explanation

Here is a step-by-step explanation of the word count program:

1. Include stdio.h and stdlib.h header files for file I/O and other functions

2. Define main() with command line arguments argc and argv

3. Check if argc is 2, otherwise print usage message and return 1 for error

4. Open the file in read mode using fopen(). Check for NULL in case file doesn't exist.

5. Initialize count to 0 to store number of words  

6. Read the file character by character using fgetc() in a loop

7. Check if current character c is whitespace (space, newline, tab)

8. If yes, read the next character using fgetc()

9. Check if next character is not whitespace and not EOF

10. If above condition is true, it means we have encountered a word boundary. Increment count.

11. Update c to next character and continue loop.

12. When we reach EOF, exit loop. 

13. Close the file using fclose().

14. Print the final word count.

15. Return 0 to indicate successful program execution.

The key steps are checking for word boundaries using whitespace characters and incrementing count when we transition from whitespace to non-whitespace. Let me know if any part is unclear!