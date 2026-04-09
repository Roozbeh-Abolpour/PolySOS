# PolySOS

**PolySOS** is a hybrid **MATLAB–Python** research toolbox for polynomial optimization via **Sum-of-Squares (SOS)** and **moment relaxations**.

It provides separate implementations of:
- **SOS-SDP**
- **SOS-SOCP**
- **Chordal-decomposed SOS-SDP**

along with the algebraic and numerical tools required to construct these relaxations.

---

## Features

- Monomial and polynomial representations
- Multi-index generation
- Moment matrix construction
- Localizing matrix construction
- SOS relaxations for constrained polynomial optimization
- Multiple solver backends:
  - **SDP**
  - **SOCP**
  - **Chordal SDP**
- Independent implementations in both **Python** and **MATLAB**

---

## Repository Structure

```text
PolySOS/
├── docs/
│   ├── overview.pdf
│   ├── methodology.pdf
│   ├── architecture.pdf
│   └── Lasserre-theorems-proofs.pdf
├── examples/
│   ├── python/
│   │   └── basic_sos_example.py
│   └── matlab/
│       └── basic_sos_example.m
├── matlab/
│   ├── localizing_matrix.m
│   ├── moment_matrix.m
│   ├── multiindex.m
│   ├── sos_relaxation.m
│   ├── sos_sdp.m
│   ├── sos_socp.m
│   ├── sos_chordal_sdp.m
│   └── chordal_decomposition/
├── src/
│   └── polysos/
│       ├── algebra/
│       ├── chordal_graph/
│       ├── moments/
│       ├── sos_relaxation/
│       └── sos_relaxation_solvers/
├── tests/
├── pyproject.toml
└── README.md
```

---

## Installation

```bash
git clone https://github.com/Roozbeh-Abolpour/PolySOS.git
cd PolySOS
pip install -e .
```

```bash
pip install -e .[dev]
```

---

## Documentation

- docs/overview.pdf  
- docs/methodology.pdf  
- docs/architecture.pdf  
- docs/Lasserre-theorems-proofs.pdf  

---

## Implemented Methods

### SOS-SDP
Full moment + localizing PSD constraints

### SOS-SOCP
SOC constraints via 2×2 minors

### Chordal SOS-SDP
PSD decomposition into smaller blocks

---

## Quick Start

### Python

```python
from polysos.algebra.polynomial.polynomial import Polynomial
from polysos.sos_relaxation.sos_relaxation import SOSRelaxation
```

See: examples/python/basic_sos_example.py

### MATLAB

See: examples/matlab/basic_sos_example.m

---

## Running Tests

```bash
pytest tests/
```

---

## Design Philosophy

Polynomial → Moment lifting → Matrix construction → Solver backend

---

## Author

Roozbeh Abolpour

---

## License

MIT License
