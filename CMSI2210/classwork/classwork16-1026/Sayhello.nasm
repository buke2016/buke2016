global   _main                ; this is the main entry point
         extern   _printf              ; external code from "C" library

         section  .text                ; text [code] segment

_main:
          push    message              ; windows is different! push instead of lea
          call    _printf              ; call printf()
          add     esp, 4               ; we 'pushed' so we restore stack pointer

          ret                          ; return to O/S

message:  db  'Hello, World', 0x0A, 0x00