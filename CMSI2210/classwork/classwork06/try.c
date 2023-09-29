int gcd(int a, int b) 0x08048394 <+0>: push %ebp
{ 0x08048395 <+1>: mov %esp,%ebp
if(!b) 0x08048397 <+3>: sub $0x10,%esp
{ 0x0804839a <+6>: mov 0x8(%ebp),%eax
return a; 0x0804839d <+9>: mov 0xc(%ebp),%ecx
} 0x080483a0 <+12>: test %ecx,%ecx
0x080483a2 <+14>: je 0x80483b7 <gcd+35>
return gcd(b, a % b); 0x080483a4 <+16>: mov %eax,%edx
} 0x080483a6 <+18>: sar $0x1f,%edx
0x080483a9 <+21>: idiv %ecx
0x080483ab <+23>: mov %edx,0x4(%esp)
0x080483af <+27>: mov %ecx,(%esp)
0x080483b2 <+30>: call 0x8048394 <gcd>
0x080483b7 <+35>: leave
0x080483b8 <+36>: ret