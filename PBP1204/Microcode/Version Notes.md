# Microcode 1.1
It kinda works, but is just unmanagable and lacks some functionality, plus it's not nearly modular enough.
Best case, all the Registers would share increment, decrement, reading, writing, etc functionality, even allowing for some hidden instructions!
With the current system, one could theoretically overwrite the instruction or bitmask register.

Best case I come up with a modular system that uses a Demux to select a register, but all the other update logic is shared between all of them, reducing component costs and messiness.

Additionally, I really have to rethink the functions. Right now they're a huge mess, not to mention the awfulness that the current ALU is.

I think it'd be best if I design the ALU separately to drop in once it's finalized.

# Microcode 2.0

| #    | Registers                 | Group      |
| ---- | ------------------------- | ---------- |
| 0000 | Instruction Register      | Functional |
| 0001 | Bitmask Register          | Functional |
| 0010 | Program Counter           | Shorts     |
| 0011 | Stack Pointer             | Shorts     |
| 0100 | Shared Temporary Register | Functional |
| 0101 | Interrupt Mode Register   | Mode       |
|      |                           |            |
| 1000 | A Register                | Arithmetic |
| 1001 | Program Counter 00        | Main       |
| 1010 | Program Counter 01        | Main       |
| 1011 | Program Counter 02        | Main       |
| 1100 | B Register                | Arithmetic |
| 1101 | Stack Pointer 00          | Main       |
| 1110 | Stack Pointer 01          | Main       |
| 1111 | Stack Pointer 02          | Main       | 

| #    | Functions                  |
| ---- | -------------------------- |
| 0000 | Read from Databus          |
| 0001 | Write to Databus           |
| 0010 | Write to Address Register  |
| 0011 | Trigger Update of Register |
| 0100 | Increment Register         |
| 0101 | Decrement Register         | 
| 0110 | Clear Carry Flag           |
| 0111 | Clear Borrow Flag          |
| 1000 | Read result of ALU NAND    |
| 1001 | Read result of ALU NOR     |
| 1010 | Read result of ALU NOT     |
| 1011 | Read result of ALU ADD     |
| 1100 | Read result of ALU SL      |
| 1101 | Read result of ALU SR      |
| 1110 | reserved for swap          |
| 1111 | reserved for swap          |

Still needs some work. Weird increment/decrement oscillation due to constant switching between the two.