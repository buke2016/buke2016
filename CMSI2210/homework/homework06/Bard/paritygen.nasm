global _paritygen

section .text

_paritygen:
    mov cl, byte ptr [esp + 4] ; cl contains the byte to check parity for

    xor al, al
    xor ah, ah

    loop1:
        inc cl
        shl ah, 1
        jnc loop1

    shl ah, 1

    and al, 1
    jnz setbit

    ret

    setbit:
        or ah, 1
        ret

section .data
