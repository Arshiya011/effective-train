"""Simple Interest utilities and a tiny CLI.

Formula:
    SI = P * (R/100) * T

Where:
    P = principal (float)
    R = annual rate in percent (float)
    T = time in years (float)
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass

def simple_interest(principal: float, rate_percent: float, time_years: float) -> float:
    if principal < 0:
        raise ValueError("principal must be non-negative")
    if time_years < 0:
        raise ValueError("time must be non-negative")
    return principal * (rate_percent / 100.0) * time_years

def total_amount(principal: float, rate_percent: float, time_years: float) -> float:
    return principal + simple_interest(principal, rate_percent, time_years)

@dataclass
class Result:
    principal: float
    rate_percent: float
    time_years: float
    interest: float
    total: float

def _parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Compute simple interest (SI = P * R/100 * T)."    )
    parser.add_argument("--principal", "-p", type=float, required=True, help="Principal amount (>= 0)")
    parser.add_argument("--rate", "-r", type=float, required=True, help="Annual interest rate in percent (e.g., 12 for 12%)")
    parser.add_argument("--time", "-t", type=float, required=True, help="Time in years (>= 0)")
    return parser.parse_args(argv)

def _main(argv=None):
    args = _parse_args(argv)
    interest = simple_interest(args.principal, args.rate, args.time)
    total = total_amount(args.principal, args.rate, args.time)
    res = Result(args.principal, args.rate, args.time, interest, total)
    print(f"Principal: {res.principal}")
    print(f"Rate (%):  {res.rate_percent}")
    print(f"Time (y):  {res.time_years}")
    print(f"Interest:  {res.interest}")
    print(f"Total:     {res.total}")
    return 0

if __name__ == "__main__":
    raise SystemExit(_main())
