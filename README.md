 A Diode-Transistor Logic Computer with a 4-Bit Processor

# Design Goals
The main purpose of this Computer is to make a decently compact, decently fast and decently capable 4-Bit Computer using mostly components that were available around the mid-60s.

The Instruction Set was designed with a CISC Mindset,  ~~partly out of spite for RISC architectures~~ partly due to not having much experience with RISC architectures, but mainly due to Memory Limitations imposed by only having a 12-Bit Address Bus, and utilizing Core Memory, as opposed to using DRAM or similar technologies, as those wouldn't be invented until the late 60s, and not become widespread until the early 70s.

I am aware that technologies like Williams tubes, delay-line memory and SRAM did exist back then, but these will be avoided for a number of logistical, monetary or just practicality reasons I won't elaborate on in this section.

# Components
This section will describe the various Modules and Boards of this Computer. 
More information on said Hardware can be found under [Hardware Components](Hardware%20Components.md).

## PBP-1204
**P**ixel **B**rush **P**rocessor, **12**-Bit Addressable Memory, **4**-Bit Data Processing
The PBP-1204 will be responsible for most of the heavy lifting with it's 16 variable-width Instructions, capable of addressing a whopping 4096 Nibbles of Data via it's 12-Bit Address Bus and 4-Bit Data Bus.
While it lacks Interrupts, it will likely be capable of stack operations, like pushing and popping data.

More info on the PBP's Instruction Set and features can be found in [PBP-1204](PBP1204/PBP1204.md)

## PBCM-1604N
**P**ixel **B**rush **C**ore **M**emory, **16**x**16** Core Grid, **4** Layers Tall, Nibbles
The PBCM-1604 will provide the Computer with a total of 1 Kilonibbles per Module.

# Example Software
**NOTE:**
None of the following example Programs work, as the actual Binaries for the Processor have changed as I've designed the Microcode and actual circuitry. I'll update these programs and the assembler once all of that has been finalized!

~~Example Code and Programs can be found in the Example Subdirectory. 
I try to keep the code as well-commented and understandable as possible, so even a novice Programmer can read and write PBP-1204 Assembly Code.~~

Some of the Programs include:

### Counting Program
A simple Program that counts from 0 to 15, then enters an infinite loop, [found here](Example/count.pbp)

### Fibonacci Sequence
A simple Program that calculates the Fibonacci Sequence in 4 Bits, [found here](Example/fibo.pbp)

# What this Project won't be
### This thing will be slow and inefficient
This Computer absolutely won't be the fastest, and while I could absolutely opt to use MOSFETs and save myself a bunch of Resistors and Diodes to make this work, I've decided to stick to true Diode-Transistor Logic, meaning I've been using good ol' Bipolar Junction Transistors for my work, and will likely continue doing so in the near future.

To add onto this, I'm just one dude that knows a little bit of Z80 Assembly. My instruction set is far from perfect, but it's just supposed to be easy to understand and decently easy to implement.

# Future Plans
Well, hopefully I'll get to build the thing someday! Right now the Processor is taking center stage, this involves refining, tweaking, overhauling the instruction set, for instance. Right now it's slowly moving towards actually designing the actual hardware needed to make this thing work as intended, which is easier said than done, especially when you lack any and all experience in designing an ungodly fusion of CISC and RISC*, while only having a vague understanding of the Fetch, Decode, Execute Cycle.

*(Edit: I have since found out this is exactly what Microcode is, so my "ungodly fusion" isn't too ungodly!)

Once the Processor is fully working reliably, with a low part count and all that, I'd like to get work done on the Core Memory. I've already been experimenting with it from time to time, with very disappointing results, mainly due to a lack of information and experts on the topic, at least online.
