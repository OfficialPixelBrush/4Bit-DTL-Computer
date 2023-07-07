x = modified
\- = involved
Instructions that need:

| Inst  | A   | B   | PC  | SP  | Flags |
| ----- | --- | --- | --- | --- | ----- |
| NAND  | x   | -   |     |     |       |
| NOR   | x   | -   |     |     |       |
| NOT   | x   |     |     |     |       |
| ADD   | x   | -   |     |     | x-    |
| SL    | x   |     |     |     | x     |
| SR    | x   |     |     |     | x     |
| LD    | x   | x   | x   | x   |       |
| ST    | -   | -   | -   | -   |       |
| LDD   | x   | x   | x   | x   |       |
| SWP   | x   | x   |     |     |       |
| PSH   | -   | -   | -   | x   |       |
| POP   | -   | -   | -   | x   |       |
| JSR   |     |     | x   | x   | -     |
| RET   |     |     | x   | x   |       |
| JMP f |     |     | x   |     | -     |
| CLR f |     |     |     |     | -     |

| Cycle   | Description                                         |
| ------- | --------------------------------------------------- |
| Fetch   | Update Inst Register                                |
| Decode  | Demux Instruction (NAND), A and B are already there |
|         | Check if Parameter required                         |
| Execute | A and B's NAND goes through                         |
| Store   | Update A                                            |

- Find corelation between cycle and instruction.
- Cycle + Inst = ADDRESS for Control Lines
  
Control Lines go to:
- Instruction Register
- Registers
	- A
	- B
	- PC
	- SP
- Flags (excluding Zero and Parity, as they're done based on A)
	- Carry
	- Borrow
`cccc iiii` => `ABPS` + Carry + Borrow + Inst Reg

Cycle Counter = 4 bit (for multi-nibble things, like storing SP or PC)
### Example (using PSH PC)

| Counter | Operation                                      | Cycle   |
| ------- | ---------------------------------------------- | ------- |
| 0000    | Load Instruction into Instruction Register     | Fetch   |
| 0001    | Decode Instruction                             | Decode  |
| 0010    | Increment PC                                   |         |
| 0011    | Load Register Bitmask in                       |         |
| 0100    | Put SP on Address Bus                          | Execute |
| 0101    | Write first Nibble of PC out through Data Bus  |         |
| 0110    | Increment SP                                   |         |
| 0111    | Write second Nibble of PC out through Data Bus |         |
| 1000    | Increment SP                                   |         |
| 1001    | Write third Nibble of PC out through Data Bus  |         |
| 1010    | Increment SP                                   |         |
| 1011    | Trigger update of SP                           | Store   | 
| 1100    | Increment PC                                   |         |
| 1101    | Reset Counter                                  |         |
| 1110    |                                                |         |
| 1111    |                                                |         |

### Example (using ADD)

| Counter | Operation                                  | Cycle   |
| ------- | ------------------------------------------ | ------- |
| 0000    | Load Instruction into Instruction Register | Fetch   |
| 0001    | Decode Instruction                         | Decode  |
| 0010    | Add A and B                                | Execute |
| 0011    | Trigger update of Flags                    | Store   | 
| 0100    | Trigger update of A Register               |         |
| 0101    | Increment PC                               |         |
| 0110    | Reset Counter                              |         |
| 0111    |                                            |         |
| 1000    |                                            |         |
| 1001    |                                            |         |
| 1010    |                                            |         |
| 1011    |                                            |         |
| 1100    |                                            |         |
| 1101    |                                            |         |
| 1110    |                                            |         |
| 1111    |                                            |         |


### Example (using LDD SP,0x005)

| Counter | Operation                                  | Cycle   |
| ------- | ------------------------------------------ | ------- |
| 0000    | Load Instruction into Instruction Register | Fetch   |
| 0001    | Decode Instruction                         | Decode  |
| 0010    | Increment PC                               | Execute |
| 0011    | Load Register Bitmask in                   |         |
| 0100    | Increment PC                               |         |
| 0101    | Load first Nibble into SP                  |         |
| 0110    | Increment PC                               |         |
| 0111    | Load second Nibble into SP                 |         |
| 1000    | Increment PC                               |         |
| 1001    | Load third Nibble into SP                  |         |
| 1010    | Trigger update of SP                       | Store   | 
| 1011    | Increment PC                               |         |
| 1100    | Reset Counter                              |         |
| 1101    |                                            |         |
| 1110    |                                            |         |
| 1111    |                                            |         |
~~Note: Update Trigger of SP can be omitted here because it's not part of the instruction~~
Should be triggered anyways for consistency and ease

### Example (using LDD PC,0x005)

| Counter | Operation                                  | Cycle   |
| ------- | ------------------------------------------ | ------- |
| 0000    | Load Instruction into Instruction Register | Fetch   |
| 0001    | Decode Instruction                         | Decode  |
| 0010    | Increment PC                               | Execute |
| 0011    | Load Register Bitmask in                   |         |
| 0100    | Increment PC                               |         |
| 0101    | Load first Nibble into SP                  |         |
| 0110    | Increment PC                               |         |
| 0111    | Load second Nibble into SP                 |         |
| 1000    | Increment PC                               |         |
| 1001    | Load third Nibble into SP                  |         |
| 1010    | Trigger update of PC                       | Store   | 
| 1011    | Increment PC                               |         |
| 1100    | Reset Counter                              |         |
| 1101    |                                            |         |
| 1110    |                                            |         |
| 1111    |                                            |         |