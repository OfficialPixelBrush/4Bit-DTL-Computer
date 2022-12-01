### Features
- 4-Bit ALU
- Variable Instruction size

### Left out for simplicity
- No Interrupts 
- ~~No Stack Handling~~

### Instruction Set
- JMP to Address
- Move Contents from Register to Register
- Add Contents of A and B
- AND, OR, NOT Instruction

| Hex | Name | Function                                            | Parameters |
| --- | ---- | --------------------------------------------------- | ---------- |
| 0x0 | NAND | Bitwise NAND A and B, Load into A                   | -          |
| 0x1 | NOR  | Bitwise NOR A and B, Load into A                    | -          |
| 0x2 | NOT  | Invert Contents of A, Load into A                   | -          |
| 0x3 | ADD  | Add the Contents of A and B with Carry, Load into A | -          |
| 0x4 | SL   | Shift Contents of A Left, Load into A               | -          |
| 0x5 | SR   | Shift Contents of A Right, Load into A              | -          |
| 0x6 | LDA  | Load Parameter into A                               | Num        |
| 0x7 | STA  | Store A to Address                                  | Addr       |
| 0x8 | LDAD | Load Contents of Address into A                     | Addr       |
| 0x9 | SWAP | Swap contents of A and B                            | -          |
| 0xA | PUSH | Push A Register to Stack                            | -          |
| 0xB | POP  | Contents of SP into A                               | -          |
| 0xC | JSR  | Jump to Subroutine                                  | Addr       |
| 0xD | RET  | Return from Subroutine                              | -          |
| 0xE | JMPZ | Jump if Zero Flag Set                               | Addr       |
| 0xF | JMP  | Unconditional Jump                                  | Addr       | 

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