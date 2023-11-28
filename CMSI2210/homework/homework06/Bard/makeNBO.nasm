global _makeNBO

section .text

_makeNBO:
    mov ebx, [esp + 4] ; ebx contains the address of the number to convert

    xor eax, eax
    mov al, byte ptr [ebx] ; al contains the least significant byte
    mov ah, byte ptr [ebx + 1]
    mov bl, byte ptr [ebx + 2]
    mov bh, byte ptr [ebx + 3]

    mov byte ptr [ebx], bh ; replace the least significant byte with the most significant byte
    mov byte ptr [ebx + 1], bl ; replace the second least significant byte with the second most significant byte
    mov byte ptr [ebx + 2], ah ; replace the third least significant byte with the third most significant byte
    mov byte ptr [ebx + 3], al ; replace the most significant byte with the least significant byte

    ret

section .data
