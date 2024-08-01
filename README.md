# ho-ieee-754

The goal of this mod is to provide a framework for implementing the IEEE-754 standard (or at least a best approximant) to the Hearts of Iron IV modding system.

# Why?

In the base modding system, variables can only be fixed point, ranging from -2,147,483.648 to 2,147,483.647 inclusive, with accuracy limited to the thousandth-place. This means that much care has to be taken in order to accommodate for potential overflow/underflow or potential truncation errors. So far, this is only an experiment, and from my current knowledge of both the Hearts of Iron IV modding script and IEEE-754, I have doubts as to how (and if) this is possible.

# Who?

This project is currently maintained by one modder, FunkyDe.
