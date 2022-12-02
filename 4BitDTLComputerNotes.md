### Features
- 4-Bit ALU
- Variable Instruction size

### Left out for simplicity
- No Interrupts 
- ~~No Stack Handling~~

### Registers

| Name | Size in Bits | Purpose                                   |
| ---- | ------------ | ----------------------------------------- |
| A    | 4            | Accumulator and General Purpose Register  |
| B    | 4            | Auxilary and General Purpose Register     |
| PC   | 12           | Program Counter                           |
| SP   | 12           | Stack Pointer                             |
| Z    | 1            | Zero Flag, (exists by NANDing A Register) | 

### Instruction Set
- JMP to Address
- Move Contents from Register to Register
- Add Contents of A and B
- AND, OR, NOT Instruction

| Hex | Name | Function                                            | Parameter 1 | Parameter 2 | Total Instruction Length (Nibbles) |
| --- | ---- | --------------------------------------------------- | ----------- | ----------- | ---------------------------------- |
| 0x0 | NAND | Bitwise NAND A and B, Load into A                   | -           | -           | 1                                  |
| 0x1 | NOR  | Bitwise NOR A and B, Load into A                    | -           | -           | 1                                  |
| 0x2 | NOT  | Invert Contents of A, Load into A                   | -           | -           | 1                                  |
| 0x3 | ADD  | Add the Contents of A and B with Carry, Load into A | -           | -           | 1                                  |
| 0x4 | SL   | Shift Contents of A Left, Load into A               | -           | -           | 1                                  |
| 0x5 | SR   | Shift Contents of A Right, Load into A              | -           | -           | 1                                  |
| 0x6 | LDx  | Load Number into Register defined by Bitmask        | ABPS        | Num         | 3                                  |
| 0x7 | STx  | Store x to Address                                  | ABPS        | Addr        | 5                                  |
| 0x8 | LDAD | Load Contents of Address into A                     | ABPS        | Addr        | 5                                  |
| 0x9 | SWAP | Swap contents of A and B                            | -           | -           | 1                                  |
| 0xA | PUSH | Push x Register to Stack                            | ABPS        | -           | 2                                  |
| 0xB | POP  | Contents pointed at by SP into x                    | ABPS        | -           | 2                                  |
| 0xC | JSR  | Jump to Subroutine                                  | Addr        | -           | 4                                  |
| 0xD | RET  | Return from Subroutine                              | -           | -           | 1                                  |
| 0xE | JMPx | Jump if x Flag Set                                  | ZCP_        | -           | 2                                  |
| 0xF | JMP  | Unconditional Jump                                  | Addr        | -           | 4                                  | 

### Instruction Cycle
Using NAND Instruction as an Example

**Register Contents***
| Reg          | Content |
| ------------ | ------- |
| A Register   | 0101    |
| B Register   | 1111    |
| Instruction  | xxxx    |
| CycleCounter | xxxx    | 

**Instruction Step-through**
| Timing | Operation                                | A Reg | B Reg | Inst | CyCo |
| ------ | ---------------------------------------- | ----- | ----- | ---- | ---- |
| \_/⎺   | Load Address into PC                     | 1010  | 1111  | xxxx | xxxx |
| ⎺\\\_  | (time to let Address stabilize)          | 1010  | 1111  | xxxx | xxxx |
| \_/⎺   | Load Nibble into INST Register           | 1010  | 1111  | 0000 | xxxx |
| ⎺\\\_  | Load Necessary Cycles into Cycle Counter | 1010  | 1111  | 0000 | 0001 |
| \_/⎺   | Enable Control Line for Instruction      | 1010  | 1111  | 0000 | 0001 |
| ⎺\\\_  | Execute Instruction                      | 0101  | 1111  | 0000 | 0000 |

**Instruction Step-through (from Cycle Loading)**
| Timing | Operation                                | A Reg | B Reg | Inst | CyCo |
| ------ | ---------------------------------------- | ----- | ----- | ---- | ---- |
| ⎺\\\_  | Load Necessary Cycles into Cycle Counter | 1010  | 1111  | 0000 | 0110 |
| \_/⎺   | Enable Control Line for Instruction      | 1010  | 1111  | 0000 | 0101 |
| ⎺\\\_  | Execute Instruction                      | 0101  | 1111  | 0000 | 0100 |
| \_/⎺   | Load Address into PC                     | 1010  | 1111  | xxxx | 0011 |
| ⎺\\\_  | (time to let Address stabilize)          | 1010  | 1111  | xxxx | 0010 |
| \_/⎺   | Load Nibble into INST Register           | 1010  | 1111  | 0000 | 0001 |  

### Memory Map
| 0x000 - 0x3FF | 0x400 - 0x7FF | 0x800 - 0xBFF | 0xC00 - 0xFFF |
| ------------- | ------------- | ------------- | ------------- |
| Core Memory   |               |               |               |

**0x000-0x3FF**
| 0x000 - 0x0FF | 0x100 - 0x3FF |
| ------------- | ------------- |
|               |               |

### How to read Core Memory
1. Send pulse to X-Y Lines
2. Sense Pulse/Lack of Pulse
3. Schmitt-Trigger the Pulse for better loading
4. Store in D-Flip-Flop
5. Read Result