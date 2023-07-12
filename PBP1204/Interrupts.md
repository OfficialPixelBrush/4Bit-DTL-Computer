| #   | Mode                                                        |
| --- | ----------------------------------------------------------- |
| 00  | No Interrupts                                               |
| 01  | Choose Interrupt Location based on what is found on Databus |
| 10  | Load Instruction from Databus                               |
| 11  | Jump to Zeropage based on Upper bits of Interrupt Register  | 

| Counter | Operation                                                     |
| ------- | ------------------------------------------------------------- |
| 0000    | Put SP on Address Bus                                         |
| 0001    | Write first Nibble of PC out through Data Bus                 |
| 0010    | Increment SP                                                  |
| 0011    | Write second Nibble of PC out through Data Bus                |
| 0100    | Increment SP                                                  |
| 0101    | Write third Nibble of PC out through Data Bus                 |
| 0110    | Increment SP                                                  |
| 0111    | Reset First Nibble of PC                                      |
| 1000    | Reset Third Nibble of PC                                      |
|         | Load Instruction Vector into Second Nibble of PC via Data Bus |
|         | Update PC and put on Address Bus                              |
|         | Reset Counter                                                 |
