section .text
    global paritygen
paritygen:
    ; Input: AL = byte of data
    ; Output: AL = parity bit
    xor al, al  ; Clear AL
    .while:
        test ah, 1  ; Test the high bit
        jnz .toggle
        shr ah, 1  ; Shift right
        jmp .check
        .toggle:
            xor al, 1  ; Toggle parity bit
            shr ah, 1  ; Shift right
        .check:
            cmp ah, 0
            jnz .while
    ret