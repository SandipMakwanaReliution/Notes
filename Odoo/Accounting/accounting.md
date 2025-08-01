## ✅ 1. Set Up Fiscal Localization and Fiscal Year

### 📘 What is it?

- **Fiscal Localization**: Country-specific accounting rules and tax structures (e.g., GST for India).
- **Fiscal Year**: Defines the accounting start and end dates.
  Example: **April to March** (India), **January to December** (US/Europe).
  
---

## ✅ 2. Set Up Chart of Accounts, Journals, and Taxes

---

### 📘 What is a Chart of Account (CoA)?

- A list of all accounts used to record financial transactions in your company.
- Examples:
  - **Receivable Account** (for customers)
  - **Payable Account** (for vendors)
  - **Sales Income**
  - **Purchase Expense**
  - **Bank/Cash Accounts**

---

### 📘 What Are Taxes in Odoo?

- Taxes calculate **GST/VAT** automatically on invoices and bills.
- Odoo uses tax records to apply the correct tax percentage and post to the correct tax accounts.

---

## ✅ 3. Set Up Bank Accounts (Optional)

If your company uses banks for transactions, you should add your bank accounts in Odoo.

---

Journal
-------
Type:
	- Sales
	- Purchase
	- Cash
	- Bank
	- Miscellaneous
	
Invoice/Bill
------------

- when create a invoice odoo find "Account Payable" and "Account Reciable" from Customer or Vendor Contect form.

=================           
ACCOUNT TYPES:
=================   
Balance Sheet:
    Assests:
        Receivable
        Bank and Cash
        Current Assests
        Non-current Assets
        Prepayments
        Fixed Assests
    Liabilites:
        Payable
        Credit Card
        Current Liabilites
        Non-current Liabilites
    Equity:
        Equity
        Current Year Earnings [Mandatory]

Profit and Loss:
    Other:
        Off-Balance Sheet
    Expenses:
        Cost of Revenue
        Depreciation
        Expenses    
    Income:
        Income
        Other Income

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

