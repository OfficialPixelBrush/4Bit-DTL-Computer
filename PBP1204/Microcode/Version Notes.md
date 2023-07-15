# Microcode 1.1
![[microcodeV1.1.svg]]
It kinda works, but is just unmanagable and lacks some functionality, plus it's not nearly modular enough.
Best case, all the Registers would share increment, decrement, reading, writing, etc functionality, even allowing for some hidden instructions!
With the current system, one could theoretically overwrite the instruction or bitmask register.

Best case I come up with a modular system that uses a Demux to select a register, but all the other update logic is shared between all of them, reducing component costs and messiness.

Additionally, I really have to rethink the functions. Right now they're a huge mess, not to mention the awfulness that the current ALU is.

I think it'd be best if I design the ALU separately to drop in once it's finalized.

# Microcode 2.0

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
![[microcodeV2.0.svg]]
Still needs some work. Weird increment/decrement oscillation due to constant switching between the two.
- Has been fixed after latching with SR Latch

## 2.1
![[microcodeV2.1.svg]]

## 2.2
Note: Resetting of Bitmask Register will indicate start of a new Cycle. This includes resetting a few other registers, like the instruction counter and "HasBitmaskBeenSet" Register
Meanwhile, Resetting the Instruction Register will indicate a full hardware reset
![[microcodeV2.2.svg]]

- Maybe have the first 4 Register Enables serve double-duty as inverted outputs of flags, only used for Checking them?

| #    | Registers                             | Group      |
| ---- | ------------------------------------- | ---------- |
| 0000 | Instruction Register / Not Zero       | Functional |
| 0001 | Bitmask Register / Not Carry          | Functional |
| 0010 | Buffer Register / Not Borrow          | Functional |
| 0011 | Interrupt Mode Register / Even Parity | Mode       |
| 0100 | Zero                                  | Flag       |
| 0101 | Carry                                 | Flag       |
| 0110 | Borrow                                | Flag       |
| 0111 | Odd Parity                            | Flag       | 

# Microcode 2.3

![[microcodeV2.3.svg]]

A simple count program worked!

# Microcode 2.4
- Bitmask addressing is completely fucked
- It instantly switches to the selected register and overwrites it, plus it completely disables incrementing other registers

# Microcode 2.5
- How is the Decoder supposed to know if a Register is 12-Bit or 4-Bit?
- How can the Decoder determine how many loads it does?