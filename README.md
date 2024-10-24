# ho-ieee-754

The goal of this mod is to provide an implementation floating-point numbers, according to the IEEE 754 standard, to the Hearts of Iron IV modding system, for use by other modders.

# Why?

HOI4's base modding script uses signed 32-bit fixed-point variables(referred to later as pdxvars), ranging from -2,147,483.648 to 2,147,483.647, with accuracy to the thousandth-place. This means that variables can overflow or are truncated, losing data. So, I am working on an implementation floating-point variables according to the IEEE 754 standard, which would allow for both a greater range of numbers and a greater precision, while maintaining a modder-friendly interface within Paradox's provided modding script. Currently, this project is a work-in-progress, and likely will be for the near future as there is still much to do.

# Background

From [Wikipedia](https://en.wikipedia.org/wiki/IEEE_754):
> The IEEE Standard for Floating-Point Arithmetic (IEEE 754) is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).

This standard allows for the storage of real numbers of both extremely large and extremely small magnitudes(10<sup>±38</sup> in the single-precision format used here) while maintaining relatively good precision(around 10<sup>-7</sup> proportionally). You can read the entire standard in this repo at `extras/IEEE_754.pdf`.

The plan is to use Hearts of Iron IV's built-in modding script to provide as complete of an implementation of the IEEE 754 standard as possible, using the pdxvars themselves to store the data of floating-point variables. Since pdxvars are basically 32-bit signed integers that are divided by 1000, the same 32 bits of data can be used to store a single-precision floating-point variable according to the IEEE standard. This means that while the math behind the scenes will be floating point, the variables will be able to be stored as usual in pdxvars, only being converted in the scripts that perform calculations. 

# Goals

This mod is designed to be used in combination with other mods.  
This means that:
1. This mod works within the modding framework that Hearts of Iron IV provides, so scripted effects, scripted triggers, scripted localisation, duct tape, and the like.
2. The mod provides a method of interfacing with itself with other mods. The ultimate goal will be a set of files, which can be added to any other mod, that provide a system of creating, interacting with, accessing, and outputting floating-point variables.

# Roadmap

The tentative task map is:
- [x] Read through IEEE 754/get familiar with standard
- [x] Experiment with bit-wise operators
- [x] Creation and Destruction of floating-point variables (FPVs)
    - [x] Implement system of input to transform pdxvars to FPVs
- [x] FPV Output
    - [x] Implement localization of FPVs
    - [x] Implement transformation back to pdxvars
- [x] Comparison
- [ ] Addition and Subtraction
    - [x] Test cases
    - [ ] Positive+Positive base case
    - [ ] Addition with negatives / Subtraction
    - [ ] Exceptions and special cases (subnormals, infinities, NaNs)
- [ ] Multiplication
- [ ] Division
- [ ] Square Root
- [ ] Additional basic functions
- [ ] Recommended operations (consult Clause 9 of IEEE 754)

A more detailed progress chart can be found at `extras/progress.md`, which displays which of the functions deemed necessary by the IEEE 754 standard have been implemented.

# Who?

This project is currently maintained by one modder, FunkyDe.

# Additional Details

Documentation: There is a lot of information to parse when using this mod for the first time. Every function has documentation above it highlighting the functionality, errors, and notes associated with the function. As the developer, I strongly recommend at least skimming the docs for the float_to_pdxvar and pdxvar_to_float functions, since those handle the basic translation between floats and pdxvars. Furthermore, I am considering opening channels for further communication and assistance, perhaps through Discord, but that is a matter for when the mod is ready for public release.

Triggers: Localization only allows triggers to be utilized beforehand, meaning that the scripted effects that are necessary to pre-process variables and arrays are not available. Therefore, certain scripted effects have been converted to a scripted trigger. There should be no difference between them, but for ease of use a wrapper scripted effect is also available.

Bit Arrays: In order to process floating-point numbers, this mod makes extensive use of bit arrays. These arrays are marked by their names `temp_array_###`, and their elements are restricted to being either 0 or 1. While the floating-point variables can be stored as usual in pdxvars, in the background they will be converted to bit arrays for actual use. Therefore, I recommend not to tamper with these temporary arrays. While errors (detailed below) may catch some of the effects of bit array manipulation, it may not notice all of them.

Digit Arrays: Localization and conversion from floating point back to pdxvars both present an interesting challenge. Since floats can exceed pdxvars' min and max values by orders of magnitude, I need to precalculate the decimal representations of the powers of 2 in order to compute floating-point values. An on action runs on startup which triggers a scripted effects which performs this precalculation, storing its results in global arrays and values. Be careful when using variables of the form `global.digit_power@var:###` and arrays of the form `global.digit_array@var:###`, where the `###` is a variable with an integer value.

Errors: This mod is complex, so I have implemented a system of error logging for testing purposes. Generally, an error will do two things, raise a message in `game.log` and increment a temp var called `NAME_error_flag`. These variables are useful as they can accumulate the error number, so reading the counter after a bad function call counts the number of errors. However, due to the nature of scripted effects, these errors cannot affect control flow efficiently. This means that in the case errors do occur, but their impact will propagate to anything else it interacts with.

Tests: I have implemented a series of tests in order to verify the function of functions during development. If you want to examine the tests themselves, you can check out `scripted_effects/ieee_tests.txt` - each test is a scripted effect named `ieee_test_####`, which prints a short result to `game.log`. These tests run on game startup and generate a report in `game.log` for each test and any failures. Additionally, you can execute all tests at once with the scripted effect `ieee_run_tests` (in-game terminal: `e ieee_run_tests`). Error messages may appear in `game.log` after executing tests, but that is to be expected from testing the functions' error handlers.

Assumptions: When modding scripts try to access a variable that has not been set yet, it will read 0. This may raise a bit of confusion, as the script treats both the modder forgetting to set a variable/parameter and them deliberately setting a variable to 0 equivalently. Notes have been taken in the comments to describe the outcome for uninitialized variables, but extra care should be taken with scripted effects that handle numerical input: to_bitwise, to_float, etc. Since their inputs are meant to be numbers, leaving inputs uninitialized as 0 will proceed with no errors, warnings, or notification. These 0-critical inputs will be marked in comments with the line `# If no input is given, the function will use 0 in place **and return no error**` in the comments above each function.

NaN: It is very difficult to create exceptions in Hearts of Iron IV, as there is no way to break the execution of a scripted effect or trigger as far as I can tell. This means that signaling NaNs are effectively impossible as sNaNs require an exception to be raised immediately. Therefore, all NaNs implemented in ho-ieee-754 are effectively quiet NaNs. Since exceptions are impossible, the only difference between quiet and signaling functions is whether or not a warning is displayed and a flag incremented.

# TODOlist:

- Addition
    - positive case
    - negative
    - subnormal
    - inf/NaN
- Add mention of defines.lua change and what to keep