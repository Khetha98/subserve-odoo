Subserve Module Dependency Map

(POS → Inventory → Accounting → Compliance)


┌───────────────────────────┐
│        POS (Frontend)     │
│ point_of_sale             │
│ - Cashiers                │
│ - Payments                │
│ - Receipts                │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│        Inventory          │
│ stock                     │
│ - Products                │
│ - Barcodes                │
│ - Stock moves             │
│ - Valuation               │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│        Accounting         │
│ account                   │
│ - Journals                │
│ - Cash / Card entries     │
│ - Debtors / Creditors     │
│ - Balance sheet           │
└──────────────┬────────────┘
               │
               ▼
┌───────────────────────────┐
│     Subserve Compliance   │
│ subserve_compliance       │
│ - CIPC / SARS records     │
│ - Annual returns          │
│ - Reports                 │
└───────────────────────────┘





Community Accounting Engine (what you actually use)

This is already in your codebase, but it’s split into modules and not branded as a single app.

Community accounting is provided by:

Module	            Purpose	            Community
account	            Journals, moves, GL	    ✅
account_accountant	Extra accounting UI	❌ Enterprise
account_reports	    Financial statements❌ Enterprise
account_asset	    Assets	            ❌ Enterprise
l10n_*	            Country rules	        ✅
point_of_sale	    POS accounting entries	✅

📌 In Community, you do NOT install “Accounting”
📌 You enable accounting via POS, Invoicing, Purchases, Inventory



///////////////////////////////
Odoo Core (account, stock, pos)
        ↓
Subserve Finance Extensions (reports, wizards)
        ↓
Subserve Compliance Automation


Dependency map (high level)
POS
 └── Inventory
      └── Accounting
           └── Finance Reports
                └── Compliance
                     └── Compliance Automation
                          └── Audit Trail


point_of_sale
 └── stock
      └── account
           └── subserve_finance_reports
                └── subserve_compliance
                     └── subserve_compliance_automation
                          └── subserve_audit_trail

