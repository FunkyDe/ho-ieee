# Operations Progress
This Markdown page provides a view of the progress towards the implementation of all the operations deemed necessary by the IEEE 754 Standard. The operations are not given in the exact order as listed in the IEEE 754 document, but each operation is in its correct clause.

## 5.3 - Homogeneous General-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| roundToIntegralTiesToEven | <span style="color:red"><span style="color:red">Not Done</span></span> | ##### | Converts float -> float |
| roundToIntegralTiesToAway | <span style="color:red">Not Done</span> | ##### | Converts float -> float |
| roundToIntegralTowardZero | <span style="color:red">Not Done</span> | ##### | Converts float -> float |
| roundToIntegralTowardPositive | <span style="color:red">Not Done</span> | ##### | Converts float -> float |
| roundToIntegralTowardNegative | <span style="color:red">Not Done</span> | ##### | Converts float -> float |
| roundToIntegralExact | <span style="color:red">Not Done</span> | ##### | Converts float -> float, signals if inexact |
| nextUp | <span style="color:red">Not Done</span> | ##### | The least float greater than the input |
| nextDown | <span style="color:red">Not Done</span> | ##### | Defined as -nextUp(-x) |
| remainder | <span style="color:red">Not Done</span> | ##### | remainder(x, y) = x-y*n, n is an integer |
| scaleB | <span style="color:red">Not Done</span> | ##### | x(2)<sup>y</sup>, y is an integer |
| logB | <span style="color:red">Not Done</span> | ##### | floor(log<sub>2</sub>(x)) |

## 5.4 formatOf General-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| addition | <span style="color:red">Not Done</span> | ##### | ##### |
| subtraction | <span style="color:red">Not Done</span> | ##### | ##### |
| multiplication | <span style="color:red">Not Done</span> | ##### | ##### |
| division | <span style="color:red">Not Done</span> | ##### | ##### |
| squareRoot | <span style="color:red">Not Done</span> | ##### | ##### |
| fusedMultiplyAdd | <span style="color:red">Not Done</span> | ##### | fMA(x, y, z) = x*y + z, rounded only at end |
| convertFromInt | <span style="color:blue">Done</span> | **pdxvar_to_float** | modified to convertFromPdx, converts from pdxvar instead of integer |
| convertToIntegerTiesToEven | <span style="color:blue">Done</span> | **float_to_pdxvar** | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTiesToAway | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardZero | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardPositive | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardNegative | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerExactTiesToEven | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTiesToAway | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardZero | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardPositive | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardNegative | <span style="color:red">Not Done</span> | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToDecimalCharacter | <span style="color:blue">Done</span> | **Various localization scripts** | 5 styles given: full accuracy, truncated at decimal, truncated at thousandth, rounded, and scientific notation |

## 5.5 Quiet-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| copy | <span style="color:blue">Done</span> | **set_temp_variable** / **set_variable** | Already implemented by pdxscript |
| negate | <span style="color:red">Not Done</span> | ##### |  |
| abs | <span style="color:red">Not Done</span> | ##### |  |
| copySign | <span style="color:red">Not Done</span> | ##### |  |

## 5.6 Signaling-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| compareQuietEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietGreater | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietGreaterEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietLess | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietLessEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietNotEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietNotGreater | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietNotGreaterEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietNotLess | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietNotLessEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareQuietOrdered | <span style="color:red">Not Done</span> | ##### | No signaling counterpart because they would raise an error upon receiving a NaN argument |
| compareQuietNotOrdered | <span style="color:red">Not Done</span> | ##### | No signaling counterpart because they would raise an error upon receiving a NaN argument |
| compareSignalingEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingGreater | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingGreaterEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingLess | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingLessEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingNotEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingNotGreater | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingNotGreaterEqual | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingNotLess | <span style="color:red">Not Done</span> | ##### |  |
| compareSignalingNotLessEqual | <span style="color:red">Not Done</span> | ##### |  |

## 5.7 Non-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| is754version1985 | <span style="color:red">Not Done</span> | ##### | Always false |
| is754version2008 | <span style="color:red">Not Done</span> | ##### | Always false |
| is754version2019 | <span style="color:red">Not Done</span> | ##### | Always true |
| class | <span style="color:red">Not Done</span> | ##### |  |
| isSignMinus | <span style="color:red">Not Done</span> | ##### |  |
| isZero | <span style="color:red">Not Done</span> | ##### |  |
| isNormal | <span style="color:red">Not Done</span> | ##### |  |
| isSubnormal | <span style="color:red">Not Done</span> | ##### |  |
| isFinite | <span style="color:red">Not Done</span> | ##### |  |
| isInfinite | <span style="color:red">Not Done</span> | ##### |  |
| isNaN | <span style="color:red">Not Done</span> | ##### |  |
| isSignaling | <span style="color:red">Not Done</span> | ##### | Always false, see ../README.md as to why signaling NaNs are not implemented |
| isCanonical | <span style="color:red">Not Done</span> | ##### |  |
| radix | <span style="color:red">Not Done</span> | ##### | Always 2, no decimal formats implemented |
| totalOrder | <span style="color:blue">Done</span> | ##### |  |
| totalOrderMag | <span style="color:red">Not Done</span> | ##### | totalOrder(abs(x), abs(y)) |

### 5.7.4 Non-computational Operations, Flags
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| lowerFlags | <span style="color:red">Not Done</span> | ##### |  |
| raiseFlags | <span style="color:red">Not Done</span> | ##### |  |
| testFlags | <span style="color:red">Not Done</span> | ##### |  |
| testSavedFlags | <span style="color:red">Not Done</span> | ##### |  |
| restoreFlags | <span style="color:red">Not Done</span> | ##### |  |
| saveAllFlags | <span style="color:red">Not Done</span> | ##### |  |

## Skipped Operations
Some operations mentioned in the requirements are not listed above, as they are uniquely difficult to implement, pertain to decimal floating-point formats, or are simply impossible. Please consult the clause(s) listed in each row for more details.

| Operation | Clause | Notes |
| :--- | :--- | :--- |
| quantize | 5.3.2 | Pertains to decimal floating-point formats |
| quantum | 5.3.2 | Pertains to decimal floating-point formats |
| convertFormat | 5.4.2 | unused because only one format used and no signaling NaNs nor exceptions |
| convertFromDecimalCharacter | 5.4.2 | Impossible to handle string inputs in pdxscript |
| convertFromHexCharacter | 5.4.3 | Impossible to handle string inputs in pdxscript |
| convertToHexCharacter | 5.4.3 | Uniquely difficult to create strings in pdxscript. Might consider doing this as a bonus at the end. |
| encodeDecimal | 5.5.2 | Pertains to decimal floating-point formats |
| decodeDecimal | 5.5.2 | Pertains to decimal floating-point formats |
| encodeBinary | 5.5.2 | Pertains to decimal floating-point formats |
| decodeBinary | 5.5.2 | Pertains to decimal floating-point formats |
| sameQuantum | 5.7.3 | Pertains to decimal floating-point formats |