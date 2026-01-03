# Design Notes

- Expressions represent matrix and vector operations (e.g. addition, multiplication).
- Each expression node carries shape information to allow early detection of dimension errors.
- Optimisation ideas include reordering chains of matrix multiplications to reduce computational cost.
