# Microcode 1.1
It kinda works, but is just unmanagable and lacks some functionality, plus it's not nearly modular enough.
Best case, all the Registers would share increment, decrement, reading, writing, etc functionality, even allowing for some hidden instructions!
With the current system, one could theoretically overwrite the instruction or bitmask register.

Best case I come up with a modular system that uses a Demux to select a register, but all the other update logic is shared between all of them, reducing component costs and messiness.

Additionally, I really have to rethink the functions. Right now they're a huge mess, not to mention the awfulness that the current ALU is.

I think it'd be best if I design the ALU separately to drop in once it's finalized.
