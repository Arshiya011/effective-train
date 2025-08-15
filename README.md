# Microfinance Simple Interest

A tiny, community-friendly reference project for a micro-finance startup's transition from SVN to Git.  
It demonstrates best practices for an open-source repo and includes a simple Python CLI to compute **simple interest**.

> Formula: **SI = P × R × T**, where:
> - **P** = Principal amount
> - **R** = Annual interest rate (in percent)
> - **T** = Time in years

## Why this repo?
- Clear structure and docs (README, CONTRIBUTING, Code of Conduct, License).
- Tested code with a minimal CLI and unit tests.
- Apache License 2.0 to enable broad community use.

## Quick start

### 1) Use the CLI
```bash
python si.py --principal 10000 --rate 12 --time 1.5
```
Output shows the simple interest and total amount.

### 2) Use as a library
```python
from si import simple_interest, total_amount
interest = simple_interest(10000, 12, 1.5)  # -> 1800.0
total = total_amount(10000, 12, 1.5)        # -> 11800.0
```

### 3) Run tests
```bash
python -m unittest
```

## Project structure
```
.
├── si.py                 # Library + CLI
├── tests/
│   └── test_si.py        # Unit tests
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE               # Apache License 2.0
└── .gitignore
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License
This project is licensed under the [Apache License 2.0](LICENSE).
