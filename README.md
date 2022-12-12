 A Diode-Transistor Logic Computer with a 4-Bit Processor

# Design Goals
The main purpose of this Computer is to make a decently compact, decently fast and decently capable 4-Bit Computer using mostly components that were available around the mid-60s.

The Instruction Set was designed with a CISC Mindset,  ~~partly out of spite for RISC architectures~~ partly due to not having much experience with RISC architectures, but mainly due to Memory Limitations imposed by only having a 12-Bit Address Bus, and utilizing Core Memory, as opposed to using DRAM or similar technologies, as those wouldn't be invented until the late 60s, and not become widespread until the early 70s.

# Components
## PBP-1204
**P**ixel **B**rush **P**rocessor, **12**-Bit Addressable Memory, **4**-Bit Data Processing
The PBP-1204 will be responsible for most of the heavy lifting with it's 16 variable-width Instructions, capable of addressing a whopping 4096 Nibbles of Data via it's 12-Bit Address Bus and 4-Bit Data Bus.
While it lacks Interrupts, it will likely be capable of stack operations, like pushing and popping data.

## PBCM-1604N
**P**ixel **B**rush **C**ore **M**emory, **16**x**16** Core Grid, **4** Layers Tall, Nibbles
The PBCM-1604 will provide the Computer with a total of 1 Kilonibbles per Module.

# Future Plans
Well, hopefully I'll get to build the thing someday! Right now the Processor is taking center stage, this involves refining, tweaking, overhauling the instruction set, for instance. Right now it's slowly moving towards actually designing the actual hardware needed to make this thing work as intended, which is easier said than done, especially when you lack any and all experience in designing an ungodly fusion of CISC and RISC, while only having a vague understanding of the Fetch, Decode, Execute Cycle.

Once the Processor is fully working reliably, with a low part count and all that, I'd like to get work done on the Core Memory. I've already been experimenting with it from time to time, with very disappointing results, mainly due to a lack of information and experts on the topic, at least online.