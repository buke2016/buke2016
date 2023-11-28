section .text
    global findGCD
findGCD:
    ; Input: EAX = first number, EBX = second number
    ; Output: EAX = GCD
    ; Euclidean algorithm to find GCD
    .while:
        cmp eax, ebx
        jl .swap
        sub eax, ebx
        jmp .while
        .swap:
            xchg eax, ebx
    ret