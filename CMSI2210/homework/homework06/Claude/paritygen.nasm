; paritygen.nasm

global paritygen

section .text

paritygen:
    ; Function expects data byte in al  
    mov cl, al
    xor ch, ch    ; Clear ch to use as counter
    
    ; Count 1 bits
    cmp al, 0
    je done_count
loop_count: 
    shr al, 1
    adc ch, 0    
    jnz loop_count

done_count:

    ; Set parity bit in ah 
    mov al, ch
    and al, 1
    xor al, 1   ; Flip bit for odd parity
    mov ah, al

    ret