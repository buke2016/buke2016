; demo.stpn
   ; program to output the powers of 2 up to 1,000,000
   ; output goes to port 100  [hex 0x64]
   ; copied from cmsi 284/2210 web pages

   0         JMP     start    ; begin by jumping over the data area
   1 pow:    1                ; store the current power value here
   2 limit:  1000000          ; we'll be computing powers up to this amount
   3 start:  LOAD    pow      ; bring the value into accumulator to use
   4         WRITE   100      ; output the current power
   5         ADD     pow      ; adding to itself makes the next power!
   6         STORE   pow      ; store it (for next time)
   7         SUB     limit    ; we need to compare with limit, subtracting helps
   8         JLZ     start    ; if not yet past limit, keep going
   9 end:    JMP     end      ; this "stops" the program!