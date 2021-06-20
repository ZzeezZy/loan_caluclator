# loan_caluclator

## To caluclate the different payment every month we use this formula
### Dm = P / n + i ∗ (P − P ∗ (m − 1) / n) 

Where:
- Dm = mth differentiated payment
- m = current repayment month.
- P = the loan principal
- i = nominal interest rate. This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.
- n = number of payments. This is usually the number of months in which repayments will be made.

### To use this calculator user should use bash or cmd or shell and type
**For type of diff:** <br />
> python filename.py --type=diff --principal=(loan-principal) --interest=(interest-rate) --periods=(in-months)

**For type of annuity:**<br />
When we dont't know how much time it takes to pay the loan
> python filename.py --type=annuity --principal=(loan-principal) --interest=(interest-rate) --payment=(monthly-payment)

**or**<br />

When we don't know how much to pay in the given time period
> python filename.py --type=annuity --principal=(loan-principal) --interest=(interest-rate) --period=(in-months)

**or**<br />

When we don't know how much loan we taked
> python filename.py --type=annuity --interest=(interest-rate) --payment=(monthly-payment) --periods=(in-month)

**example**
> python filename.py --type=diff --principal=1000000 --interest=10 --periods=10
```
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834
Overpayment = 45837
```
