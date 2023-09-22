## What is everything we need it to do?
![[Z80_arch.svg]]
### How can Registers interact with Memory?
Memory <-> Buffer <-> Register

### Timing
Rising Edge: Used to let Data Stabilize
Falling Edge: Used to let contents of Registers be updated

### Internal Registers
| Index | Name                   | Short | Use                                                               |
| ----- | ---------------------- | ----- | ----------------------------------------------------------------- |
| 0000  | Bitmask                | BM    | Stores to-be Addressed Register                                          |
| 0001  | Low Buffer             | LB    | ALU Temp, In-between for Memory and Registers                     |
| 0010  | Middle Buffer          | MB    | In-between for Memory and Address Registers                       |
| 0011  | High Buffer            | HB    | In-between for Memory and Address Registers                       |
| 0100  | Instruction            | IR    | Holds current Instruction                                         |
| 0101  | A                      | AR    | General Purpose Register (Accumulator)                            |
| 0110  | B                      | BR    | General Purpose Register (Auxiliary)                              |
| 0111  | Flags                  | FR    | Contains the 4 Flags, ZCBP                                        |
| 1000  | Instruction Counter    | IC    | Tracking which Microcode Instruction is being run                 |
| 1001  | Low Program Counter    | LPC   | Lowest Nibble ofProgram Counter                                                   |
| 1010  | Middle Program Counter | MPC   | Medium Nibble ofProgram Counter                                                   |
| 1011  | High Program Counter   | HPC   | Highest Nibble of Program Counter                                                   |
| 1100  | Test Flags             | TF    | Contains which Flags will be tested for, in case of a conditional |
| 1101  | Low Stack Pointer      | LSP   | Lowest Nibble of Stack Pointer                                                     |
| 1110  | Middle Stack Pointer   | MSP   | Medium Nibble of Stack Pointer                                                     |
| 1111  | High Stack Pointer     | HSP   | Highest Nibble of Stack Pointer                                                     |

### Internal Instructions
| Index | Name                      | Function                                            | Used by        |
| ----- | ------------------------- | --------------------------------------------------- | -------------- |
| 0000  | Read from Databus         | Read directly from Databus                          | Buffer00-02    |
| 0001  | Write to Databus          | Output data to the Databus                          | Buffer00       |
| 0010  | Read from Buffer          | Read contents from the Buffer                       | AR,BR,TF,PC,SP |
| 0011  | Update Address Register   | Updates Address Register with contents of  PC or SP | AD             |
| 0100  | Increment Register        | Used to Increment PC or SP                          | PC,SP          |
| 0101  | Decrement Register        | Used to Decrement SP                                | SP             |
| 0110  | Check Flag                | If TF && F == 1, write Buffers to PC.               | PC             |
| 0111  | Reset Register to Default | Clears/Fills the relevant Register                  | any            | 
| 1000  |                           |                                                     |                |
| 1001  |                           |                                                     |                |
| 1010  |                           |                                                     |                |
| 1011  |                           |                                                     |                |
| 1100  |                           |                                                     |                |
| 1101  |                           |                                                     |                |
| 1110  |                           |                                                     |                |
| 1111  |                           |                                                     |                |