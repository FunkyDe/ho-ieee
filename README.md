# ho-ieee-754

The goal of this mod is to provide a framework for implementing the IEEE-754 standard of floating-point numbers (or at least a best approximant) to the Hearts of Iron IV modding system.

# Why?

In the base modding script, variables can only be fixed-point, ranging from -2,147,483.648 to 2,147,483.647 inclusive, with accuracy limited to the thousandth-place. This means that much care while modding has to be taken in order to accommodate for potential overflow/underflow or potential truncation errors. So far, this is only an experiment, and from my current knowledge of both the Hearts of Iron IV modding script and IEEE 754, I have doubts as to how (and if) this is possible.

# Background

From [Wikipedia](https://en.wikipedia.org/wiki/IEEE_754):
> The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).

This standard allows for the storage of both extremely large and extremely small numbers with relatively good precision(proportionally, around 10<sup>-7</sup> in the case of single-precision). The plan is to use Hearts of Iron IV's built-in modding script to provide a partial-to-complete implementation of the IEEE 754 standard using the bit-wise interpretation of the 32-bit *fixed-point* variables as the foundation for a *floating-point* variable system using a combination of scripted effects, scripted localization, and scoping.

You can read the entire standard in this repo at `extras/IEEE_754.pdf`.

# Constraints

This mod is hoped to be used in combination with other mods.  
This means that:
1. No fooling around with the game engine or base files. This mod has to work from within the modding framework that Hearts of Iron IV provides (finicky may it be).
2. The mod has to provide a method of interfacing with itself to provide function for other mods. The end-goal will be a set of files, which can be added to any other mod as usual, that provide a system of creating, interacting with, accessing, and destroying floating-point variables.

# Order of Operations

This mod is a pipe dream at the moment, but for now the tentative task map is:
1. Read through IEEE 754
2. Experiment with bit-wise operators
3. Creation and Destruction of floating-point variables (FPVs)
    1. Figure out scope declare/assign/reassign/undeclare scheme
    2. Implement system of input to transform regular variables to FPVs
4. FPV Output
    1. Implement localization of FPVs
    2. Implement transformation back to regular variables
    3. Implement error notification system (regular variable overflow, etc.)
5. Addition and Subtraction
6. Multiplication and comparison
7. Division (scary)
8. Additional basic functions
9. Exceptions and special cases (subnormals, infinities)
10. Recommended operations (consult Clause 9 of IEEE 754)

- Important but not on the list: Memory/variable management system (Not IEEE 754, useful for at-scale applications)

# Who?

This project is currently maintained by one modder, FunkyDe.
