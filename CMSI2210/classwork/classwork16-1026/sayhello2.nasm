; Define variables in the data section
            section  .data
hello:      db       'Hello world!',10
helloLen:   equ      $-hello

; Code goes in the text section
            section  .text
            global   _main

_main:      mov      eax,  4            ; 'write' system call = 4
            mov      ebx,  1            ; file descriptor 1 = STDOUT
            mov      ecx,  hello        ; string to write
            mov      edx,  helloLen     ; length of string to write
            int      80h                ; call the BIOS interrupt

; Terminate program
            mov      eax,  1            ; 'exit' system call
            mov      ebx,  0            ; exit with error cod
            int      80h                ; call the BIOS interrupt