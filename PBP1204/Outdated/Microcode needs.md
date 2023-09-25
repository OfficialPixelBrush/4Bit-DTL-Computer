- Trigger update of Register
- Increment Register
- Reset Register
- Connect to Address Bus
- Read Databus
- Write Databus

| Bit | Function                        |
| --- | ------------------------------- |
| 0   | Register00                      |
| 1   | Register01                      |
| 2   | Register02                      |
| 3   | Register04                      |
| 4   | Read from Databus               |
| 5   | Write to Databus                |
| 6   | Connect Register to Address Bus |
| 7   | Trigger update of Register      |
| 8   | Increment Register              |
| 9   | Decrement Register              |

Registers:

| #    | Name             |
| ---- | ---------------- |
| 0000 | Instruction      |
| 0001 | Interrupt        |
| 0010 | AddressLow       |
| 0011 | AddressMid       |
| 0100 | AddressHigh      |
| 0101 | Program Counter  |
| 0110 | Stack Pointer    |
| 0111 | Address Register | 
| 1000 | A                |
| 1001 | B                |
| 1010 | ProgramLow       |
| 1011 | ProgramMid       |
| 1100 | ProgramHigh      |
| 1101 | StackLow         |
| 1110 | StackMid         |
| 1111 | StackHigh        |


