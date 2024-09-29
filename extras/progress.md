# Operations Progress
This Markdown page provides a view of the progress towards the implementation of all the operations deemed necessary by the IEEE 754 Standard. The operations are not given in the exact order as listed in the IEEE 754 document, but each operation is in its correct clause.

## 5.3 - Homogeneous General-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| roundToIntegralTiesToEven | Not Done | ##### | Converts float -> float |
| roundToIntegralTiesToAway | Not Done | ##### | Converts float -> float |
| roundToIntegralTowardZero | Not Done | ##### | Converts float -> float |
| roundToIntegralTowardPositive | Not Done | ##### | Converts float -> float |
| roundToIntegralTowardNegative | Not Done | ##### | Converts float -> float |
| roundToIntegralExact | Not Done | ##### | Converts float -> float, signals if inexact |
| nextUp | Not Done | ##### | The least float greater than the input |
| nextDown | Not Done | ##### | Defined as -nextUp(-x) |
| remainder | Not Done | ##### | remainder(x, y) = x-y*n, n is an integer |
| scaleB | Not Done | ##### | x(2)<sup>y</sup>, y is an integer |
| logB | Not Done | ##### | floor(log<sub>2</sub>(x)) |

## 5.4 formatOf General-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| addition | Not Done | ##### | ##### |
| subtraction | Not Done | ##### | ##### |
| multiplication | Not Done | ##### | ##### |
| division | Not Done | ##### | ##### |
| squareRoot | Not Done | ##### | ##### |
| fusedMultiplyAdd | Not Done | ##### | fMA(x, y, z) = x*y + z, rounded only at end |
| convertFromInt | Done | **pdxvar_to_float** | modified to convertFromPdx, converts from pdxvar instead of integer |
| convertToIntegerTiesToEven | Done | **float_to_pdxvar** | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTiesToAway | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardZero | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardPositive | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerTowardNegative | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer |
| convertToIntegerExactTiesToEven | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTiesToAway | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardZero | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardPositive | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToIntegerExactTowardNegative | Not Done | ##### | modified to convertToPdx, converts to pdxvar instead of integer, signals if inexact |
| convertToDecimalCharacter | Done | **Various localization scripts** | 5 styles given: full accuracy, truncated at decimal, truncated at thousandth, rounded, and scientific notation |

## 5.5 Quiet-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| copy | Done | **set_temp_variable** / **set_variable** | Already implemented by pdxscript |
| negate | Not Done | ##### |  |
| abs | Not Done | ##### |  |
| copySign | Not Done | ##### |  |

## 5.6 Signaling-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| compareQuietEqual | Done | **compareEqual** |  |
| compareQuietGreater | Done | **compareGreater** |  |
| compareQuietGreaterEqual | Done | **compareGreaterEqual** |  |
| compareQuietLess | Done | **compareLess** |  |
| compareQuietLessEqual | Done | **compareLessEqual** |  |
| compareQuietNotEqual | Done | **compareNotEqual** |  |
| compareQuietNotGreater | Done | **compareNotGreater** |  |
| compareQuietNotGreaterEqual | Done | **compareNotGreaterEqual** |  |
| compareQuietNotLess | Done | **compareNotLess** |  |
| compareQuietNotLessEqual | Done | **compareNotLessEqual** |  |
| compareQuietOrdered | Done | **compareOrdered** | No signaling counterpart because they would raise an error upon receiving a NaN argument |
| compareQuietNotOrdered | Done | **compareNotOrdered** | No signaling counterpart because they would raise an error upon receiving a NaN argument |
| compareSignalingEqual | Done | **compareSignalingEqual** |  |
| compareSignalingGreater | Done | **compareSignalingGreater** |  |
| compareSignalingGreaterEqual | Done | **compareSignalingGreaterEqual** |  |
| compareSignalingLess | Done | **compareSignalingLess** |  |
| compareSignalingLessEqual | Done | **compareSignalingLessEqual** |  |
| compareSignalingNotEqual | Done | **compareSignalingNotEqual** |  |
| compareSignalingNotGreater | Done | **compareSignalingNotGreater** |  |
| compareSignalingNotGreaterEqual | Done | **compareSignalingNotGreaterEqual** |  |
| compareSignalingNotLess | Done | **compareSignalingNotLess** |  |
| compareSignalingNotLessEqual | Done | **compareSignalingNotLessEqual** |  |

## 5.7 Non-computational Operations
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| is754version1985 | Not Done | ##### | Always false |
| is754version2008 | Not Done | ##### | Always false |
| is754version2019 | Not Done | ##### | Always true |
| class | Not Done | ##### | 10 classes: signaling NaN, quiet NaN, negative infinity, negative normal, negative subnormal, negative zero, positive zero, positive subnormal, positive normal, and positive infinity |
| isSignMinus | Not Done | ##### |  |
| isZero | Not Done | ##### |  |
| isNormal | Not Done | ##### |  |
| isSubnormal | Not Done | ##### |  |
| isFinite | Not Done | ##### |  |
| isInfinite | Not Done | ##### |  |
| isNaN | Not Done | ##### |  |
| isSignaling | Not Done | ##### | Always false, see ../README.md as to why signaling NaNs are not implemented |
| isCanonical | Not Done | ##### |  |
| radix | Not Done | ##### | Always 2, no decimal formats implemented |
| totalOrder | Done | **totalOrder** | Consult clause 5.10 in IEEE 754 |
| totalOrderMag | Not Done | ##### | totalOrder(abs(x), abs(y)) |

### 5.7.4 Non-computational Operations, Flags
| Operation | Progress | Implemented By | Notes |
| :--- | :--- | :--- | :--- |
| lowerFlags | Not Done | ##### |  |
| raiseFlags | Not Done | ##### |  |
| testFlags | Not Done | ##### |  |
| testSavedFlags | Not Done | ##### |  |
| restoreFlags | Not Done | ##### |  |
| saveAllFlags | Not Done | ##### |  |

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