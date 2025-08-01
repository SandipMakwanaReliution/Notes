# 1. Fiscal Localization and Fiscal Year

- **Fiscal Localization**: Country-specific accounting rules and tax structures (e.g., GST for India).
- **Fiscal Year**: Defines the accounting start and end dates.
  Example: **April to March** (India), **January to December** (US/Europe).
  
---

# 2. Chart of Accounts (CoA)

- The Chart of Accounts is a **list of all accounts** used to record financial transactions in your company.
- Each account belongs to a specific **account type**, which determines where it appears in reports (Balance Sheet or Profit & Loss).
- It forms the backbone of your accounting setup in Odoo.

## 🧮 Balance Sheet Accounts

### 📂 Assets
- `Receivable` 
- `Bank and Cash`
- `Current Assets`
- `Non-current Assets`
- `Prepayments`
- `Fixed Assets`

### 📂 Liabilities
- `Payable`
- `Credit Card`
- `Current Liabilities`
- `Non-current Liabilities`

### 📂 Equity
- `Equity`
- `Current Year Earnings` – **⚠️ Mandatory** – Holds current year net profit/loss

## 📉 Profit and Loss Accounts

### 📂 Income
- `Income`
- `Other Income`

### 📂 Expenses
- `Cost of Revenue`
- `Depreciation`
- `Expenses`

### 📂 Other
- `Off-Balance Sheet`

---

# 3. Taxes

- Taxes calculate **GST/VAT** automatically on invoices and bills.
- Odoo uses tax records to apply the correct tax percentage and post to the correct tax accounts.

---

# 4. Bank Accounts (Optional)

If your company uses banks for transactions, you should add your bank accounts in Odoo.

---

# 5. Journal

- `Sales`
- `Purchase`
- `Cash`
- `Bank`
- `Miscellaneous`
	
---

Invoice/Bill
------------

- when create a invoice odoo find "Account Payable" and "Account Reciable" from Customer or Vendor Contect form.



=================
JOURNAL TYPES:
=================
Sales Journal
- [Default Account] : Income 
- Receivable 

Purchase Journal
- [Default Account] : Expenses
- Payable

Cash Journal
- [Cash Account] : Bank and Cash 
- [Suspense Account] : Current Assests 
- [Profit Account] : Income 
- [Loss Account] : Expenses 

Bank Journal
- [Bank Account] : Bank and Cash 
- [Suspense Account] : Current Assests 

Miscellaneous
- [Default Account]

=================
TAX TYPES:
=================
Sales
- Current Liabilites [Tax Receive]

Purchase
- Current Assets [Tax Paid]

================
Invoices Conf:
================
1. Receivable on contact forms.

2. Accounts on the 'taxes'.

3. Default 'income' account on Sales Journal.
Optional: 'default income' account on peoduct or product category.

4. Invoice Layout.

================
Bills Conf:
================
1. Payable on contact forms.

2. Accounts on the 'taxes'.

3. Default 'expense' account on Purchase Journal.
Optional: 'default expense' account on peoduct or product category.

================
Reporting:
================
1. Legal
    - Balance Sheet
    - Profit and Loss Statement
    - Tax report
2. Management
    - General ledger
    - Trial balance
    - Partner ledger
    - Aged balances
    - Depreciaiton board
    
Assests (Things the company owns)                       =   Liabilites (What the company owes)                  +   Equity (Owner’s interest in the company)

Bank and Cash                                                                                                           Unallocated Earnings (or Retained Earnings)
•   Increases with Sales (+)                                                                                            •   Increases with Sales (+)
•   Decreases with Purchases (-)                                                                                        •   Decreases with Purchases (-)

Receivable (Accounts Receivable)                            Payable (Accounts Payable)
•   Increases when Invoice is posted (Pending Payment)          •   Increases when a Bill is posted (Pending Payment)
•   Decreases when Payment is received                          •   Decreases when Payment is made

Current Assests                                             Current Liabilities
•   Increases when Tax is Receivable                            •   Increases when Tax is Payable
•   Decreases when Tax Return                                   •   Decreases when Tax Return 

----------

Net Profit = Expenses (Purchase +) - Income (Sales +)

