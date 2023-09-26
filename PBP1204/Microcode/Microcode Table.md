## What is everything we need it to do?
[[Z80_arch.svg]]
https://www.electronicsteacher.com/digital/counters/synchronous-counters.php
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
| 0100  | 4   | Reset Flag                | RSF   | Reset the relevant Flags                                                     |             |                 |
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
| Index | #   | Name                      | Short | Use                                                               |
| ----- | --- | ------------------------- | ----- | ----------------------------------------------------------------- |
| 0000  | 0   | Instruction               | IR    | Holds current Instruction                                         |
| 0001  | 1   | Low Buffer                | LB    | ALU Temp, In-between for Memory and Registers                     |
| 0010  | 2   | Middle Buffer             | MB    | In-between for Memory and Address Registers                       |
| 0011  | 3   | High Buffer               | HB    | In-between for Memory and Address Registers                       |
| 0100  | 4   | A                         | AR    | General Purpose Register (Accumulator)                            |
| 0101  | 5   | B                         | BR    | General Purpose Register (Auxiliary)                              |
| 0110  | 6   | Test Flags/Address Buffer | TF/AB | Contains which Flags will be tested for, in case of a conditional |
| 0111  | 7   | Register Select           | RS    | Stores to-be Addressed Register                                   |
| 1000  | 8   | Low Program Counter       | LPC   | Lowest Nibble of Program Counter                                  |
| 1001  | 9   | Middle Program Counter    | MPC   | Medium Nibble of Program Counter                                  |
| 1010  | A   | High Program Counter      | HPC   | Highest Nibble of Program Counter                                 |
| 1011  | B   | Interrupt Register        | INT   | To keep track of where to jump if an interrupt occurs             |
| 1100  | C   | Low Stack Pointer         | LSP   | Lowest Nibble of Stack Pointer                                    |
| 1101  | D   | Middle Stack Pointer      | MSP   | Medium Nibble of Stack Pointer                                    |
| 1110  | E   | High Stack Pointer        | HSP   | Highest Nibble of Stack Pointer                                   |
| 1111  | F   | RS Pointed                | RSP   | Will act as whichever Register RS Points to                       |

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
| 1000  | 8   | No Flag                      |       | 
| 1001  | 9   | "                            |       |
| 1010  | A   | "                            |       |
| 1011  | B   | "                            |       |
| 1100  | C   | "                            |       |
| 1101  | D   | "                            |       |
| 1110  | E   | "                            |       |
| 1111  | F   | "                            |       |