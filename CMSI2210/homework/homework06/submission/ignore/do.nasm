; Parity Checker Program                   (parityChecker.asm)
INCLUDE Irvine32.inc
;http://kipirvine.com/asm/gettingStartedVS2015/index.htm
TRUE = 1
FASLE = 0

.data 
	
	evenp BYTE 10 DUP(0ffh) 
	oddp BYTE 0ffh,0ffh,0ffh,0ffh,0ffh,0ffh,0ffh,0ffh,0ffh,0fbh,	;array 10 bytes odd parity

.code 
main PROC 
	mov esi, OFFSET oddp
	mov ecx, LENGTHOF evenp
	call checkParity

	mov esi, OFFSET evenp
	
	mov ecx, LEnGTHOF oddp
	call checkParity

exit
main ENDP 



;----------------------------------------------------
checkParity PROC 
; 
; Checks Parity by using XOR to set the parity falg and jumping to a label to get  a count 
; 
; Receives: nothing 
; Returns: nothing 
;----------------------------------------------------
.data
	evenMSG  BYTE "Parity is even! ",0 
	oddMSG  BYTE "Parity is odd! ",0 
	count BYTE ?
.code
	mov count, 0
l1: 
	mov bl, [esi]			;compare each byte in order 

	pushfd
	inc esi
	cmp count, 9
	je checkp
	inc count
	popfd
	xor bl, [esi]
	
	
	loop l1
checkp:
	popfd
	jp evenParity
	jnp oddParity	
			
evenParity:
	mov eax, TRUE
	mov edx, OFFSET evenMSG
	call WriteString
	jmp final	

oddParity: 
	mov eax, FALSE
	mov edx, OFFSET oddMSG
	call WriteString
	jmp final

	
final:
ret 
checkParity ENDP 


END main