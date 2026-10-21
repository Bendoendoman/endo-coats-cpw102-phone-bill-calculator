# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**

**Evidence (paste your terminal run):**

how much data did you use?
10
how much does your plan cost?
40
You are within your data limit
Your total bill is: 40.0

**Pass / Fail and why:**
pass - expected value
## Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**

**Evidence (paste your terminal run):**

how much data did you use?
15
how much does your plan cost?
40
You are over your data limit
Moderate extra usage
Your total bill is: 50.0

**Pass / Fail and why:**
pass - expected value
## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**

**Evidence (paste your terminal run):**

how much data did you use?
15.5
how much does your plan cost?
50
You are over your data limit
High extra usage
Your total bill is: 61.0

**Pass / Fail and why:**
pass - expected value
If a case fails, fix the program and add evidence of the rerun below that case.
