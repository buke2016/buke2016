; Define variables in the data section
section  .data
hello:      db       'Hello world!',10    ; String to print with a newline character
helloLen:   equ      $-hello              ; Calculate the length of the string

; Code goes in the text section
section  .text
global   _main                            ; Entry point for the program

_main:
    mov      eax,  4                        ; 'write' system call number (4)
    mov      ebx,  1                        ; File descriptor 1 = STDOUT
    mov      ecx,  hello                    ; Address of the string to write
    mov      edx,  helloLen                 ; Length of the string to write
    int      80h                            ; Call the Linux kernel's system call

; Terminate program
    mov      eax,  1                        ; 'exit' system call number (1)
    mov      ebx,  0                        ; Exit with error code 0
    int      80h                            ; Call the Linux kernel's system call
