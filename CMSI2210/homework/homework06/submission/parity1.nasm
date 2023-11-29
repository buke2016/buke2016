section .data
  format db "Parity Bit: %d", 10, 0  ; Format string for printing

section .text
  bits 64  ; Specify 64-bit mode
  global paritygen
  extern printf

paritygen:
  ; Function prologue
  push   rbp
  mov    rbp, rsp
  sub    rsp, 16  ; Adjust stack if needed

  ; Initialize counters
  mov    rcx, 0   ; Counter for set bits

  ; Bit counting loop
count_bits:
    mov    al, byte ptr [rbp + 16]  ; Initialize al with input value
    test    al, 1
    jnz    increment_counter

    shr    al, 1
    cmp    al, 0
    jne    count_bits  ; Continue loop if not all bits processed

  jmp    check_end

increment_counter:
  inc    rcx
  jmp    count_bits

check_end:
  ; Calculate parity bit
  test    rcx, 1
  jz      set_parity_bit
  mov    rcx, 1

set_parity_bit:
  ; Print result
  lea    rax, [format]
  mov    rdi, rcx
  call    printf

  leave
  ret
