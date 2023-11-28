section .data
    result dd 0

section .text
    global findGCD

findGCD:
    ; Input: eax=num1, ebx=num2
    ; Output: result=gcd(num1, num2)

    ; Calculate GCD using Euclid's algorithm
    cmp ebx, 0
    je done

    ; Swap if num1 < num2
    cmp eax, ebx
    jge continue
    xchg eax, ebx

continue:
    ; Calculate remainder and recurse
    mov edx, eax
    div ebx
    mov eax, ebx
    mov ebx, edx
    call findGCD

done:
    ; Set result to the current value of eax
    mov [result], eax
    ret
