; gcd.nasm
global gcd

gcd:
    push rbp
    mov rbp, rsp
    
    mov rax, rdi ; first number
    mov rbx, rsi ; second number
    
gcd_loop:
    cmp rbx, 0
    je done
    cdq
    idiv rbx
    mov rax, rbx
    mov rbx, rdx
    jmp gcd_loop
    
done:    
    mov rax, rbx
    pop rbp
    ret