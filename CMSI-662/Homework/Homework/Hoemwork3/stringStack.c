#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 4

typedef enum {
    SUCCESS,
    MEMORY_ALLOCATION_FAILED,
    STACK_UNDERFLOW,
    STACK_OVERFLOW 
} OperationResult;

typedef struct {
    char** items;
    int size;
    int capacity;
} StringStack;

typedef struct {
    OperationResult result;
    char* value; 
} OperationResponse;

// Function prototypes
StringStack* create_stack(void);
void free_stack(StringStack* stack);
OperationResponse push(StringStack* stack, const char* item);
OperationResponse pop(StringStack* stack);
OperationResult expand_capacity(StringStack* stack);

StringStack* create_stack(void) {
    StringStack* stack = (StringStack*)malloc(sizeof(StringStack));
    if (stack == NULL) {
        fprintf(stderr, "Error: Memory allocation failed for stack creation.\n");
        return NULL; 
    }
    stack->items = (char**)malloc(sizeof(char*) * INITIAL_CAPACITY);
    if (stack->items == NULL) {
        free(stack);
        fprintf(stderr, "Error: Memory allocation failed for stack items.\n");
        return NULL; 
    }
    stack->size = 0;
    stack->capacity = INITIAL_CAPACITY;
    return stack;
}

void free_stack(StringStack* stack) {
    if (stack) {
        for (int i = 0; i < stack->size; i++) {
            free(stack->items[i]);
        }
        free(stack->items);
        free(stack);
    }
}

OperationResponse push(StringStack* stack, const char* item) {
    OperationResponse response = {.result = SUCCESS, .value = NULL};
    if (stack == NULL || item == NULL) {
        response.result = MEMORY_ALLOCATION_FAILED;
        return response;
    }
    if (stack->size == stack->capacity) {
        OperationResult expand_result = expand_capacity(stack);
        if (expand_result != SUCCESS) {
            response.result = expand_result;
            return response;
        }
    }
    char* item_copy = strdup(item);
    if (item_copy == NULL) {
        response.result = MEMORY_ALLOCATION_FAILED;
        return response;
    }
    stack->items[stack->size++] = item_copy;
    return response;
}

OperationResponse pop(StringStack* stack) {
    OperationResponse response = {.result = SUCCESS, .value = NULL};
    if (stack == NULL || stack->size == 0) {
        response.result = STACK_UNDERFLOW;
        return response;
    }
    response.value = stack->items[--stack->size];
    stack->items[stack->size] = NULL; 
    return response;
}

OperationResult expand_capacity(StringStack* stack) {
    if (stack == NULL) {
        return MEMORY_ALLOCATION_FAILED;
    }
    int new_capacity = stack->capacity * 2;
    char** new_items = (char**)realloc(stack->items, sizeof(char*) * new_capacity);
    if (new_items == NULL) {
        return MEMORY_ALLOCATION_FAILED;
    }
    stack->items = new_items;
    stack->capacity = new_capacity;
    return SUCCESS;
}

int main() {
    StringStack* stack = create_stack();
    if (stack == NULL) {
        fprintf(stderr, "Failed to create stack.\n");
        return MEMORY_ALLOCATION_FAILED;
    }

    OperationResponse response = push(stack, "Bye");
    if (response.result != SUCCESS) {
        fprintf(stderr, "Push failed with error code: %d\n", response.result);
        free_stack(stack);
        return response.result;
    }

    response = pop(stack);
    if (response.result == SUCCESS) {
        printf("Popped: %s\n", response.value);
        free(response.value); 
    } else {
        fprintf(stderr, "Pop failed with error code: %d\n", response.result);
    }

    free_stack(stack);
    return 0;
}
