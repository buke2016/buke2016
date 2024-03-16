#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 4

typedef struct {
    char** items;
    int size;
    int capacity;
} StringStack;

// Function prototypes
StringStack* create_stack();
void free_stack(StringStack* stack);
void push(StringStack* stack, const char* item);
char* pop(StringStack* stack);
static void expand_capacity(StringStack* stack);

StringStack* create_stack() {
    StringStack* stack = (StringStack*)malloc(sizeof(StringStack));
    if (!stack) {
        fprintf(stderr, "Fatal error: Memory allocation failed for stack.\n");
        exit(EXIT_FAILURE);
    }
    stack->items = (char**)malloc(sizeof(char*) * INITIAL_CAPACITY);
    if (!stack->items) {
        fprintf(stderr, "Fatal error: Memory allocation failed for stack items.\n");
        free(stack);
        exit(EXIT_FAILURE);
    }
    stack->size = 0;
    stack->capacity = INITIAL_CAPACITY;
    return stack;
}

void free_stack(StringStack* stack) {
    for (int i = 0; i < stack->size; i++) {
        free(stack->items[i]);
    }
    free(stack->items);
    free(stack);
}

void push(StringStack* stack, const char* item) {
    if (stack->size == stack->capacity) {
        expand_capacity(stack);
    }
    stack->items[stack->size] = strdup(item);
    if (!stack->items[stack->size]) {
        fprintf(stderr, "Fatal error: Memory allocation failed for string duplication.\n");
        exit(EXIT_FAILURE);
    }
    stack->size++;
}

char* pop(StringStack* stack) {
    if (stack->size == 0) {
        fprintf(stderr, "Fatal error: Stack underflow.\n");
        exit(EXIT_FAILURE); 
    }
    stack->size--;
    char* item = stack->items[stack->size];
    stack->items[stack->size] = NULL; 
    return item;
}

static void expand_capacity(StringStack* stack) {
    int new_capacity = stack->capacity * 2;
    char** new_items = (char**)realloc(stack->items, sizeof(char*) * new_capacity);
    if (!new_items) {
        fprintf(stderr, "Fatal error: Memory allocation failed for stack expansion.\n");
        exit(EXIT_FAILURE);
    }
    stack->items = new_items;
    stack->capacity = new_capacity;
}

int main() {
    StringStack* stack = create_stack();
    push(stack, "Hello");
    push(stack, "World");

    char* item = pop(stack);
    printf("Popped: %s\n", item);
    free(item); 

    free_stack(stack);
    return 0;
}
