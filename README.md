# PolySOS

**PolySOS** is a research-oriented Python toolbox for solving polynomial optimization problems using **Sum-of-Squares (SOS) relaxations**.

The library provides tools to construct polynomial representations, moment matrices, and solve SOS relaxations using SDP, SOCP, and chordal decomposition techniques.

---

## 🚀 Features

- Polynomial algebra (monomial and multivariate polynomial representation)
- Moment and localizing matrix construction
- SOS relaxations:
  - Semidefinite Programming (SDP)
  - Second-Order Cone Programming (SOCP)
  - Chordal decomposition for large-scale problems
- Sparse SOS via chordal graphs

---

## 📁 Project Structure


src/polysos/
algebra/ # monomial and polynomial classes
moments/ # moment and localizing matrices
chordal_graph/ # sparsity + graph tools
sos_relaxation/ # SOS formulation
sos_relaxation_solvers/ # SDP / SOCP solvers


---

## ⚙️ Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/PolySOS.git
cd PolySOS
pip install -e .
▶️ Quick Example
from polysos.algebra.polynomial.polynomial import Polynomial
from polysos.sos_relaxation.sos_relaxation import SOSRelaxation

# Define a simple polynomial
# Example: f(x) = x^4 - x^2 + 1

# (Pseudo-style depending on your API)
p = Polynomial(...)

# Build SOS relaxation
sos = SOSRelaxation(p)

# Solve using SDP
result = sos.solve(method="sdp")

print("Optimal value:", result)

👉 See examples/ for full working scripts.

🧠 Methodology

PolySOS implements classical SOS-based polynomial optimization:

A polynomial optimization problem is lifted into a moment space
Positivity constraints are enforced via semidefinite conditions
Relaxations can be solved using:
Full SDP
SOCP approximations
Chordal decomposition for scalability
📊 MATLAB Reference Implementation

A MATLAB implementation is also provided in the matlab/ folder for:

Validation
Comparison
Educational purposes
🧪 Tests

Run tests:

pytest tests/
📌 Status

⚠️ Research prototype
This library is under active development and primarily intended for research and experimentation.

👤 Author

Roozbeh Abolpour
Ph.D. in Control and Optimization
Research areas:

Polynomial Optimization
QCQP and Nonconvex Optimization
Data-Driven Control (MPC)
Energy Systems
📜 License

MIT License (or choose your preferred license)


---

# 🔥 Why This README Works (Important)

This version:

✔ Looks like a **serious research library**  
✔ Shows your **mathematical depth**  
✔ Is understandable for:
- researchers
- collaborators
- employers  

---

# ⚡ Next Step

Now we go to:

👉 `.gitignore`  
👉 then `pyproject.toml`  
👉 then `example script` (very important)

Just say:
**next**