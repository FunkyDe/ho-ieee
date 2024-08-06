# ho-ieee-754

The goal of this mod is to provide a framework for implementing the IEEE-754 standard of floating-point numbers (or at least a best approximant) to the Hearts of Iron IV modding system.

# Why?

In the base modding script, variables(referred to as pdxvars) can only be fixed-point, ranging from -2,147,483.648 to 2,147,483.647 inclusive, with accuracy limited to the thousandth-place. This means that much care while modding has to be taken in order to accommodate for potential overflow/underflow or potential truncation errors. So far, this is only an experiment, and from my current knowledge of both the Hearts of Iron IV modding script and IEEE 754, I have doubts as to how (and if) this is possible.

# Background

From [Wikipedia](https://en.wikipedia.org/wiki/IEEE_754):
> The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).

This standard allows for the storage of both extremely large and extremely small numbers with relatively good precision(proportionally, around 10<sup>-7</sup> in the case of single-precision). The plan is to use Hearts of Iron IV's built-in modding script to provide a partial-to-complete implementation of the IEEE 754 standard using the bit-wise interpretation of the 32-bit *fixed-point* pdxvars as the foundation for a *floating-point* variable system using a combination of scripted effects, scripted localization, and duct tape.

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
    1. Implement system of input to transform pdxvars to FPVs
4. FPV Output
    1. Implement localization of FPVs
    2. Implement transformation back to pdxvars
5. Addition and Subtraction
6. Multiplication and comparison
7. Division (scary)
8. Additional basic functions
9. Exceptions and special cases (subnormals, infinities)
10. Recommended operations (consult Clause 9 of IEEE 754)

# Who?

This project is currently maintained by one modder, FunkyDe.

# Additional Details

Bit Arrays: In order to process floating-point numbers, this mod makes extensive use of bit arrays. These arrays are marked by their names `temp_array_###`, and their elements are restricted to being either 0 or 1. While the floating-point variables can be stored as usual in pdxvars, in the background they will be converted to bit arrays for actual use. Therefore, I recommend not to tamper with these temporary arrays. While errors (detailed below) may catch some of the effects of bit array manipulation, it may not notice all of them.

Errors: This mod is complex, I have implemented a system of error logging for testing purposes. Generally, an error will do two things, raise a message in `game.log` and increment a temp var called `NAME_error_flag`. These flags are useful as they can accumulate the error number, so reading the counter after a bad function call counts the number of errors. However, due to the nature of scripted effects, these errors cannot affect control flow efficiently. This means that in the case errors do occur, their impact will propagate to anything else it interacts with.

Tests: Furthermore, I have implemented a series of tests in order to verify the function of code during development. If you want to examine the tests themselves, you can check out `scripted_effects/ieee_tests.txt` - each test is a scripted effect named `ieee_test_####`, which prints a short result to `game.log`. Additionally, you can execute all tests at once with the scripted effect `ieee_run_tests` (in-game terminal: `e ieee_run_tests`), which prints all of their results to `game.log`. Error messages may appear in the logs, but that is to be expected from testing the error catching portions of functions.