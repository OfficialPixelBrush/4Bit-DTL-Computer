
| #    | Registers               | Group      |
| ---- | ----------------------- | ---------- |
| 0000 | Instruction Register    | Functional |
| 0001 | Bitmask Register        | Functional |
| 0010 | Buffer Register         | Functional |
| 0011 | Interrupt Mode Register | Mode       |
| 0100 | Zero                    | Flag       |
| 0101 | Carry                   | Flag       |
| 0110 | Borrow                  | Flag       |
| 0111 | Odd Parity              | Flag       |
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
| 0011 | Trigger Update of Register                        |
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