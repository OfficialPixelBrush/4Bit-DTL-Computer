
| #    | Registers               | Group      |
| ---- | ----------------------- | ---------- |
| 0000 | Instruction Register    | Functional |
| 0001 | Bitmask Register        | Functional |
| 0010 | Flags Register          | Flag       |
| 0011 | Test Flags Register     | Flag       |
| 0100 | Interrupt Mode Register | Mode       |
| 0101 | Buffer 00               | Functional |
| 0110 | Buffer 01               | Functional |
| 0111 | Buffer 02               | Functional |
| 1000 | A Register              | Arithmetic |
| 1001 | Program Counter 00      | Main       |
| 1010 | Program Counter 01      | Main       |
| 1011 | Program Counter 02      | Main       |
| 1100 | B Register              | Arithmetic |
| 1101 | Stack Pointer 00        | Main       |
| 1110 | Stack Pointer 01        | Main       |
| 1111 | Stack Pointer 02        | Main       |

| #    | Functions                                         |
| ---- | ------------------------------------------------- |
| 0000 | Read from Databus                                 |
| 0001 | Write to Databus                                  |
| 0010 | Write to Address Register                         |
| 0011 | Read from Buffer                                  |
| 0100 | Increment Register                                |
| 0101 | Decrement Register                                |
| 0110 | If Flag is false, continue until Counter is reset |
| 0111 | Reset Register to Default                         |
| 1000 | Read result of ALU NAND                           |
| 1001 | Read result of ALU NOR                            |
| 1010 | Read result of ALU NOT                            |
| 1011 | Read result of ALU ADD                            |
| 1100 | Read result of ALU SL                             |
| 1101 | Read result of ALU SR                             |
| 1110 | Output Primary                                    |
| 1111 | Output Secondary                                  |

### Example of ADD instruction

| Function                  | Register             | F#   | R#   | Hex |
| ------------------------- | -------------------- | ---- | ---- | --- |
| Read from Databus         | Instruction Register | 0000 | 0000 | 00  |
| Read result of ALU ADD    | Buffer 00            | 1011 | 0101 | B5  |
| Read from Buffer          | A Register           | 0011 | 1000 | 38  | 
| Increment Register        | Program Counter 00   | 0100 | 1001 | 49  |
| Reset Register to Default | Bitmask Register     | 0111 | 0001 | 71  |
