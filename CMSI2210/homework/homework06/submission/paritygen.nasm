global _parity_check

section .text

_parity_check:
  ; Get the data byte
  mov al, [esp + 4]

  ; Initialize the parity bit to 0
  xor ah, ah

  ; Count the number of 1 bits in the data byte
  loop1:
    inc cl
    shl ah, 1
    and al, 1
    jnz incr_parity

    jmp end_loop

  incr_parity:
    inc ah

  end_loop:

  ; Check if the parity is even or odd
  cmp ah, 0
  je even_parity

  jmp odd_parity

  even_parity:
    ; Set the parity bit to 1
    or ah, 1

  odd_parity:
  ; Parity calculation is complete
  ret

section .data
