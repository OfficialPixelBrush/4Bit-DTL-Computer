| Hex | #    | Functions                                         |
| --- | ---- | ------------------------------------------------- |
| 0   | 0000 | Read from Databus                                 |
| 1   | 0001 | Write to Databus                                  | 
| 2   | 0010 | Write to Address Register                         |
| 3   | 0011 | Read from Buffer                                  |
| 4   | 0100 | Increment Register                                |
| 5   | 0101 | Decrement Register                                |
| 6   | 0110 | If Flag is false, continue until Counter is reset |
| 7   | 0111 | Reset Register to Default                         |
| 8   | 1000 | Read result of ALU NAND                           |
| 9   | 1001 | Read result of ALU NOR                            |
| A   | 1010 | Read result of ALU NOT                            |
| B   | 1011 | Read result of ALU ADD                            |
| C   | 1100 | Read result of ALU SL                             |
| D   | 1101 | Read result of ALU SR                             |
| E   | 1110 | Output Primary                                    |
| F   | 1111 | Output Secondary                                  |

| Hex | #    | Registers               | Group      |
| --- | ---- | ----------------------- | ---------- |
| 0   | 0000 | Instruction Register    | Functional |
| 1   | 0001 | Bitmask Register        | Functional |
| 2   | 0010 | Flags Register          | Flag       |
| 3   | 0011 | Test Flags Register     | Flag       |
| 4   | 0100 | Interrupt Mode Register | Mode       |
| 5   | 0101 | Buffer 00               | Functional |
| 6   | 0110 | Buffer 01               | Functional |
| 7   | 0111 | Buffer 02               | Functional |
| 8   | 1000 | A Register              | Arithmetic |
| 9   | 1001 | Program Counter 00      | Main       |
| A   | 1010 | Program Counter 01      | Main       |
| B   | 1011 | Program Counter 02      | Main       |
| C   | 1100 | B Register              | Arithmetic |
| D   | 1101 | Stack Pointer 00        | Main       |
| E   | 1110 | Stack Pointer 01        | Main       |
| F   | 1111 | Stack Pointer 02        | Main       |

### Example of ADD instruction

| Function                  | Register             | F#   | R#   | Hex |
| ------------------------- | -------------------- | ---- | ---- | --- |
| Read from Databus         | Instruction Register | 0000 | 0000 | 00  |
| Read result of ALU ADD    | Buffer 00            | 1011 | 0101 | B5  |
| Read from Buffer          | A Register           | 0011 | 1000 | 38  | 
| Increment Register        | Program Counter 00   | 0100 | 1001 | 49  |
| Reset Register to Default | Bitmask Register     | 0111 | 0001 | 71  |
