# ho-ieee-754

The goal of this mod is to provide an implementation floating-point numbers(according to the IEEE 754 standard) to the Hearts of Iron IV modding system, for use by other modders.

# Why?

HOI4's base modding script uses signed 32-bit fixed-point variables(referred to as pdxvars), ranging from -2,147,483.648 to 2,147,483.647, with accuracy limited to the thousandth-place. This means that while modding, much care has to be taken in order to prevent for potential overflow/underflow or potential truncation errors. So, I seek to implement a system of floating-point variables (FPVs) according to the IEEE 754 standard, which would allow for both a greater range of numbers and a greater precision, while maintaining a modder-friendly interface with the regular modding structure. Currently, I have doubts as to whether this project is 100% feasible, but that will become clear with further development and effort.

# Background

From [Wikipedia](https://en.wikipedia.org/wiki/IEEE_754):
> The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).

This standard allows for the storage of both extremely large and extremely small numbers with relatively good precision(proportionally, around 10<sup>-7</sup> in the case of single-precision). You can read the entire standard in this repo at `extras/IEEE_754.pdf`.

The plan is to use Hearts of Iron IV's built-in modding script to provide as complete of an implementation of the IEEE 754 standard as possible, using the bit-wise interpretation of the 32-bit *fixed-point* pdxvars as the foundation for a *floating-point* variable system. This means that while the math behind the scenes will be floating point, the variables will be able to be stored as usual in pdxvars, only being converted in the scripted effects that perform calculations. 

# Goals

This mod is hoped to be used in combination with other mods.  
This means that:
1. No fooling around with the game engine or base files. This mod has to work from within the modding framework that Hearts of Iron IV provides, so scripted effects, scripted triggers, scripted localisation, duct tape, and the like.
2. The mod has to provide a method of interfacing with itself to provide function for other mods. The end-goal will be a set of files, which can be added to any other mod as usual, that provide a system of creating, interacting with, accessing, and destroying floating-point variables.

# Roadmap

This mod is a work in progress at the moment, but for now the task map is:
- [x] Read through IEEE 754
- [x] Experiment with bit-wise operators
- [x] Creation and Destruction of floating-point variables (FPVs)
    - [x] Implement system of input to transform pdxvars to FPVs
- [ ] FPV Output
    - [ ] Implement localization of FPVs
    - [ ] Implement transformation back to pdxvars
- [ ] Addition and Subtraction
    - [ ] Exceptions and special cases (subnormals, infinities, NaNs)
- [ ] Multiplication and comparison
- [ ] Division (scary)
- [ ] Additional basic functions
- [ ] Recommended operations (consult Clause 9 of IEEE 754)

# Who?

This project is currently maintained by one modder, FunkyDe.

# Additional Details

Bit Arrays: In order to process floating-point numbers, this mod makes extensive use of bit arrays. These arrays are marked by their names `temp_array_###`, and their elements are restricted to being either 0 or 1. While the floating-point variables can be stored as usual in pdxvars, in the background they will be converted to bit arrays for actual use. Therefore, I recommend not to tamper with these temporary arrays. While errors (detailed below) may catch some of the effects of bit array manipulation, it may not notice all of them.

Digit Arrays: Localization and conversion from floating point back to pdxvars both present an interesting challenge. Since floats can exceed pdxvars' min and max values by orders of magnitude, I need to precalculate the decimal representations of the powers of 2 in order to compute floating-point values. An on action runs on startup which triggers a scripted effects which performs this precalculation, storing its results in global arrays and values. Be careful when using variables of the form `global.digit_power###` and arrays of the form `global.digit_array###`, where the `###` is a number.

Errors: This mod is complex, I have implemented a system of error logging for testing purposes. Generally, an error will do two things, raise a message in `game.log` and increment a temp var called `NAME_error_flag`. These flags are useful as they can accumulate the error number, so reading the counter after a bad function call counts the number of errors. However, due to the nature of scripted effects, these errors cannot affect control flow efficiently. This means that in the case errors do occur, their impact will propagate to anything else it interacts with.

Tests: Furthermore, I have implemented a series of tests in order to verify the function of code during development. If you want to examine the tests themselves, you can check out `scripted_effects/ieee_tests.txt` - each test is a scripted effect named `ieee_test_####`, which prints a short result to `game.log`. Additionally, you can execute all tests at once with the scripted effect `ieee_run_tests` (in-game terminal: `e ieee_run_tests`), which prints all of their results to `game.log`. Error messages may appear in the logs, but that is to be expected from testing the error catching portions of functions.

Assumptions: When modding scripts try to read a variable that has not been set yet, it will get 0. This may raise a bit of confusion, as the code treats both the modder forgetting to set a variable and them deliberately setting a variable to 0 equivalently. Notes have been taken in the comments to describe the outcome for uninitialized variables, but extra care should be taken with scripted effects that handle numerical input: to_bitwise, to_float, etc. Since their inputs are meant to be numbers, leaving inputs uninitialized as 0 will proceed with no errors, warnings, or notification. These 0-critical inputs will be marked in comments with the line `# If no input is given, the function will use 0 in place **and return no error**`.

# TODOlist:

- Add converter from FPVs to pdxvar
    - Edge cases and tests
- Localizer from hoieee and from bit array
    - Implement wrapper function
    - Implement 
- Addition
    - positive case
    - negative
    - subnormal
    - inf/NaN