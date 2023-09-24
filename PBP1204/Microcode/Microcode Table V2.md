## What is everything we need it to do?
![[Z80_arch.svg]]

### How can Registers interact with Memory?
Memory <-> Buffer <-> Register

### Timing
Rising Edge: Used to let Data Stabilize, Decoding of Microinstruction
Falling Edge: Used to let contents of Registers be updated

### Internal Instructions/Actions
| Index | #   | Name                      | Short | Function                                                                     | Goes from   | Goes To/Affects |
| ----- | --- | ------------------------- | ----- | ---------------------------------------------------------------------------- | ----------- | --------------- |
| 0000  | 0   | Read from Data bus        | RDB   | Read directly from Data bus                                                  | DB          | LB,MB,HB,IR     |
| 0001  | 1   | Write to Data bus         | WDB   | Output data to the Data bus                                                  | LB,MB,HB    | DB              |
| 0010  | 2   | Read from Buffer Register | RBR   | Read contents from the Buffer to Register                                    | LB,MB,HB    | AR,BR,TF,PC,SP  |
| 0011  | 3   | Write to Buffer Register  | WBR   | Write contents of Register to Buffer                                         | AR,BR,PC,SP | LB,MB,HB        |
| 0100  | 4   |                           |       |                                                                              |             |                 |
| 0101  | 5   | Update Address Register   | UAR   | Updates Address Register with contents of  PC or SP                          | PC,SP       | AB              |
| 0110  | 6   | Check Flags               | CTF   | If the Flag that TF asks for is true, update PC with value stored in Buffers | LB,MB,HB    | PC              |
| 0111  | 7   | Reset Register to Default | RRD   | Clears/Fills the relevant Register                                           |             | any             |
| 1000  | 8   | Read result of ALU NAND   | ANA   |                                                                              | ALU         | LB              |
| 1001  | 9   | Read result of ALU NOR    | ANO   |                                                                              | ALU         | LB              |
| 1010  | A   | Read result of ALU NOT    | ANT   |                                                                              | ALU         | LB              |
| 1011  | B   | Read result of ALU ADD    | AAD   |                                                                              | ALU         | LB              |
| 1100  | C   | Read result of ALU SL     | ASL   |                                                                              | ALU         | LB              |
| 1101  | D   | Read result of ALU SR     | ASR   |                                                                              | ALU         | LB              |
| 1110  | E   | Increment Register        | INC   | Used to Increment PC or SP                                                   |             | PC,SP           |
| 1111  | F   | Decrement Register        | DEC   | Used to Decrement SP                                                         |             | SP              |

### Internal Registers/Locations
| Index | #   | Name                   | Short | Use                                                               |
| ----- | --- | ---------------------- | ----- | ----------------------------------------------------------------- |
| 0000  | 0   | Instruction            | IR    | Holds current Instruction                                         |
| 0001  | 1   | Low Buffer             | LB    | ALU Temp, In-between for Memory and Registers                     |
| 0010  | 2   | Middle Buffer          | MB    | In-between for Memory and Address Registers                       |
| 0011  | 3   | High Buffer            | HB    | In-between for Memory and Address Registers                       |
| 0100  | 4   | A                      | AR    | General Purpose Register (Accumulator)                            |
| 0101  | 5   | B                      | BR    | General Purpose Register (Auxiliary)                              |
| 0110  | 6   | Test Flags             | TF    | Contains which Flags will be tested for, in case of a conditional |
| 0111  | 7   | Bitmask                | BM    | Stores to-be Addressed Register                                   |
| 1000  | 8   | Low Program Counter    | LPC   | Lowest Nibble of Program Counter                                  |
| 1001  | 9   | Middle Program Counter | MPC   | Medium Nibble of Program Counter                                  |
| 1010  | A   | High Program Counter   | HPC   | Highest Nibble of Program Counter                                 |
| 1011  | B   | Interrupt Register     | INT   | To keep track of where to jump if an interrupt occurs             |
| 1100  | C   | Low Stack Pointer      | LSP   | Lowest Nibble of Stack Pointer                                    |
| 1101  | D   | Middle Stack Pointer   | MSP   | Medium Nibble of Stack Pointer                                    |
| 1110  | E   | High Stack Pointer     | HSP   | Highest Nibble of Stack Pointer                                   |
| 1111  | F   | Bitmask Pointed        | BMP   | Will act as whichever Register BM Points to                       |

**Note: Are separate Lines for PC & SP needed?** -> Yes, because SP and PC must be written per-nibble
**Can't IR and IC use the same line? (since IC can be made to only trigger with RRD)** -> Yup, works flawlessly!

**Also important**

| Name            | Short | Use                                 |
| --------------- | ----- | ----------------------------------- |
| Data bus        | DB    | Connects to external Memory         |
| Address bus     | AB    | External Address Connection         |
| Program Counter | PC    | Combination of LPC,MPC,HPC into one |
| Stack Pointer   | SP    | Combination of LSP,MSP,HSP into one |

## Testable Flags

| Index | #   | Name                         | Short |
| ----- | --- | ---------------------------- | ----- |
| 0000  | 0   | Zero                         | Z     |
| 0001  | 1   | Carry                        | C     |
| 0010  | 2   | Borrow                       | B     |
| 0011  | 3   | Even Parity                  | EP    |
| 0100  | 4   | Not Zero                     | NZ    |
| 0101  | 5   | Not Carry                    | NC    |
| 0110  | 6   | Not Borrow                   | NB    |
| 0111  | 7   | Not Even Parity (Odd Parity) | OP    |
| 1000  | 8   |                              |       |
| 1001  | 9   |                              |       |
| 1010  | A   |                              |       |
| 1011  | B   |                              |       |
| 1100  | C   |                              |       |
| 1101  | D   |                              |       |
| 1110  | E   |                              |       |
| 1111  | F   |                              |       |


# Example Microcode for ADD
1. Read from Data bus -> IR
2. Read result of ALU ADD -> LB
3. Read from Buffer Register -> AR
4. Increment Register -> LPC
5. Reset Register to Default -> IC

**or as PBP1204 Microcode Assembly**
1. RDB IR
2. AAD LB
3. RBR AR
4. INC LPC
5. RRD IC

**or in Hex**
00 1B 42 9E 95 C7

# Another Example Program
```
LD A,0
LD B,1
loop:
ADD
SWP
ST A,0x800
JMP NC,loop
halt:
LD PC,halt
```

# Example Program

```
LD A,5
LD B,6
ADD
LD PC,0
; LD PC,0 works as an unconditional jump, as it doesn't require flags (while JMP does)
```

**Assembled**
```
0 4 5
0 5 6
B
0 8 0 0 0
```

## Microcode Conversion
### LD A,5
1. RDB IR -> 00
2. INC LPC -> 8E
3. UAR LPC -> 85
4. RDB BM -> 70
5. INC LPC -> 8E
6. UAR LPC -> 85
7. RDB LB -> 10
8. RBR BMP -> F2 
9. INC LPC -> 8E
10. UAR LPC -> 85
11. RRD IR -> 07

### LD B,6
(Same as LD A,5)

### ADD
1. RDB IR -> 00
2. AAD LB -> 1B
3. RBR AR -> 42
4. INC LPC -> 8E
5. UAR LPC -> 85
6. RRD IC -> 07

### LD PC,0
(1-4 are the same as loading of single-nibble)
5. INC LPC -> 8E
6. UAR LPC -> 85
7. RDB LB -> 10
8. INC BM -> 7E
9. INC LPC -> 8E
10. UAR LPC -> 85
11. RDB MB -> 20
12. INC BM -> 7E
13. INC LPC -> 8E
14. UAR LPC -> 85
15. RDB MB -> 30
16. RBR BMP -> F2 
17. UAR LPC -> 85
18. RRD IR -> 07
