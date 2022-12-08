### Addition until 15
```pbp1204asm
LDA 0     ; zero A Reg

loop:     ; calculation loop
LDB 1     ; Set B to 1
ADD       ; 1 in A Reg, 1 in B Reg
SWAP      ; swap contents of A and B
LDA 15    ; 15 in A Reg, 1 in B Reg
NAND      ; 0001 in A Reg, 1 in B Reg
JMPZ exit ; jump to exit if A = 0 (not true unless A and B == 15)
SWAP      ; swap contents of A and B
LDPC loop ; load address to loop into PC

exit:     ; end loop
LDPC exit ; load address to exit into PC
```
