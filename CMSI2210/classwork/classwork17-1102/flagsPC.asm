; ----------------------------------------------------------------------------------------
; This is a Win32 console program that displays the contents of the flags register on
;     the display.  In addition, if the carry flag is set, it outputs a message to that
;     effect, and if the overflow flag gets set, it outputs that message as well.
;
;  to assemble:   nasm -fwin32 flagsPC.nasm
;  to link:       gcc -m32 flagsPC.obj -o flagsPC.exe
;  to run:        flagsPC
; ----------------------------------------------------------------------------------------

            global      _main
            extern      _printf
            default     rel

            section     .text
_main:      push        EBX               ; save this one
            pushf                         ; push the value of the flags onto the stack
            pop         EAX               ; pop flags and load into EDX
            mov         EBX,  0x6543210   ; initialize the ECX register

display1:   ; display the starting value of the flags
            ; display the starting value of the EAX register

addloop:    
	    add EAX, EBX; add the EBX value to current value	    

carrychk:   pushf                         ; get the flag values
            pop         EDX               ;  and save 'em
            test EDX, 1; mask off the carry flag [bit zero]
            ; check if the carry flag is set
            je          display2          ; it's set, so output the message
            jmp         ovrflwchk         ; it's not, so check for overflow flag

display2:   ; display the carry flag set message
	    push    EAX              ; Push EAX (value with carry flag set) for printf
            push    carry_msg        ; Push the address of the carry message
            call    _printf          ; Call printf
            add     esp, 8           ; Clean up the stack

ovrflwchk:  pushf                         ; get the flag values again
            pop         EDX               ;  and save 'em
            test EDX, 0x800; mask off the overflow flag [bit eleven]
            ; check if the overflow flag is set
            jne display3; it's set, so output the message
            jmp         addloop           ; time to go again!

display3:   ; display the overflow flag set message
            push    EAX              ; Push EAX (value with overflow flag set) for printf
    	      push    overflow_msg     ; Push the address of the overflow message
            call    _printf         ; Call printf
            add         esp,  4

terminate                                 ; Terminate program
            pop         EBX               ; restore this one
            ret

            section     .data
carry_msg db "Carry flag is set",0
overflow_msg db "Overflow flag is set", 0