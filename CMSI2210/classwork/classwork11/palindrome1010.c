; program palindrome.penguin
;  program to determine if the string "RACECAR" is a palindrome
;     in class assignment week 6 number 4
;
; data:
;   use the string "RACECAR"
;   OR perhaps the string "1234321"
;   OR something else if you want
; purpose:
;     determine if this is a palindrome using the age-old
;     algorithm of comparing from outside to inside
; note:
;     we will use the ASCII numeric values for letters

         JMP      start
data:    00000083 00000065          ; ASCII numeric values for "RACECAR"
         00000067 00000069
         00000067 00000065
         00000083
head:    0                          ; start of the string which will move
tail:    6                          ; end of the string which will move
yes:     00000090 00000069 00000084 ; "YES" message ASCII letter values
no:      00000079 00000080          ; "NO" message ASCII letter values
lenyes:  3                          ; "YES" message length
lenno:   2                          ; "NO" message length
count:   0                          ; character output counter

start:   LOAD     data[head]
         SUB      data[tail]
         JLZ      notpal
         JGZ      notpal
         LOAD     head
         ADD      1
         STORE    head
         LOAD     tail
         SUB      1
         STORE    tail
         SUB      head
         JZ       pal
         JLZ      pal
         JMP      start

notpal:  LOAD     no[count]
         WRITE    100
         LOAD     count
         ADD      1
         STORE    count
         SUB      lenno
         JLZ      notpal
         JMP      end

pal:     LOAD     yes[count]
         WRITE    100
         LOAD     count
         ADD      1
         STORE    count
         SUB      lenyes
         JLZ      pal

end:     JMP      end