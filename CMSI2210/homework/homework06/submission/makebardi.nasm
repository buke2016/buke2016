global makeNBON
extern makeNBO

section .data
input1 db 12345678h ; Input value 1
input2 db 0xABCDEF01h ; Input value 2
input3 db 0x12345678DEADBEEFh ; Input value 3
input4 db 0xCAFED00D ; Input value 4
input5 db 0xDEADBEEF ; Input value 5

section .text
global _start

_start:
  ; Call makeNBO for each input value and print the results

  mov eax, input1 ; Load input value 1 into eax
  call makeNBO ; Call the C function makeNBO
  mov ebx, eax ; Save the swapped value in ebx

  mov ecx, input2 ; Load input value 2 into ecx
  call makeNBO ; Call the C function makeNBO
  mov edi, eax ; Save the swapped value in edi

  mov esi, input3 ; Load input value 3 into esi
  call makeNBO ; Call the C function makeNBO
  xor eax, eax ; Clear eax

  mov edx, input4 ; Load input value 4 into edx
  call makeNBO ; Call the C function makeNBO
  mov ebx, eax ; Save the swapped value in ebx

  mov ecx, input5 ; Load input value 5 into ecx
  call makeNBO ; Call the C function makeNBO
  mov edi, eax ; Save the swapped value in edi

  ; Print the original and swapped values

  mov eax, input1 ; Load input value 1 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 10 ; Print format: "%u"
  int 80h ; Print the original value

  mov eax, ebx ; Load the swapped value of input1 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 8 ; Print format: "%x"
  int 80h ; Print the swapped value

  ; Print the original and swapped values for the remaining inputs

  mov eax, input2 ; Load input value 2 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 10 ; Print format: "%u"
  int 80h ; Print the original value

  mov eax, edi ; Load the swapped value of input2 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 8 ; Print format: "%x"
  int 80h ; Print the swapped value

  ; Print the original and swapped values for the remaining inputs

  mov eax, input3 ; Load input value 3 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 10 ; Print format: "%u"
  int 80h ; Print the original value

  mov eax, xor eax, eax ; Load the swapped value of input3 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 8 ; Print format: "%x"
  int 80h ; Print the swapped value

  ; Print the original and swapped values for the remaining inputs

  mov eax, input4 ; Load input value 4 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 10 ; Print format: "%u"
  int 80h ; Print the original value

  mov eax, ebx ; Load the swapped value of input4 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 8 ; Print format: "%x"
  int 80h ; Print the swapped value

  ; Print the original and swapped values for the remaining inputs

  mov eax, input5 ; Load input value 5 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 10 ; Print format: "%u"
  int 80h ; Print the original value

  mov eax, edi ; Load the swapped value of input5 into eax
  mov edx, 0 ; Clear edx
  mov ecx, 8 ; Print format: "%x"
  int 80h ; Print the swapped value

  mov eax, 1 ; Exit code
  int 80h ; Exit the program
