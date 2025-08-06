# 🎯 Complex Plane Transformation Visualizer

This Python script **generates and visualizes complex transformations** of points sampled from one of three types of complex sets:
- The **unit disk**
- A **ring**
- The **unit circle**

It then applies **rotation and translation transformations** to the points and plots both the original and transformed sets.

## 🧮 Mathematical Operations

Given a set of complex numbers `z = r·e^{iθ}`:
- **Rotation**: by angle `arg(a1 + i·a2)`
- **Scaling**: by modulus `|a| = √(a1² + a2²)`
- **Translation**: by complex number `b1 + i·b2`


## 📌 Input Meaning

- `a1`, `a2`: Components of the complex multiplier (rotation + scaling)
- `b1`, `b2`: Components of the complex number added (translation)
- `|z|`: Selects the base shape:
  - `1`: Unit disk
  - `2`: Ring (outside unit disk)
  - `3`: Unit circle

## 📊 Output

- Red dots: original complex set
- Blue dots: transformed complex set

## 🧠 Requirements

```bash
pip install numpy matplotlib
```

This tool is great for visualizing Möbius transformations or exploring geometric behavior in the complex plane.

