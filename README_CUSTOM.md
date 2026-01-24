🧩 End-to-end architecture (Community)
Supplier
   ↓ Purchase Order
   ↓ Stock Receipt
   ↓ Inventory
   ↓ POS
   ↓ Accounting
   ↓ Bank / Cash

1️⃣ Buying goods from suppliers

Modules:

Purchase

Inventory

Accounting

Flow:

Create Supplier

Purchase Order

Receive goods → Stock increases

Vendor Bill → Creditors Journal

Payment → Bank / Cash Journal

✔️ Updates:

Balance Sheet

Income Statement

CPJ / CRJ

Creditors ledger

2️⃣ Register & scan goods

Modules:

Inventory

Barcode

POS

Setup:

Product:

Barcode

Cost price

Sale price

Image

Barcode scanner = keyboard wedge (cheap, works)

✔️ Scan in
✔️ Scan out
✔️ Images visible on POS

3️⃣ Cashiers with POS-only access

Modules:

Users

POS

How:

Create Group: POS Cashier

Access:

POS only

No Accounting

No Inventory

No Compliance

Result:
Cashier logs in → POS opens immediately

4️⃣ Price tags & shelves

Modules:

Inventory

Reporting (Community)

How:

Use product labels

Print barcoded price tags

Link barcode ↔ product ↔ price

✔️ Shelf labels printable
✔️ Prices synced with POS

5️⃣ Sale → accounting → hardware

Modules:

POS

Accounting

Inventory

When a sale happens:

Stock decreases

Revenue posted

Tax posted

Receipt printed

Cash drawer opens (ESC/POS)

Customer display updates

Manual card/cash selection

✔️ Security checks slip vs goods
✔️ Cash back supported


🧱 Upgrade-safe rules (VERY important)

To keep upgrades painless:

✅ Never modify core Odoo
✅ All custom logic in custom modules
✅ Use _inherit, never override
✅ No monkey patching
✅ One feature = one module
✅ Pin Odoo version in Git

This keeps:

Minimal git conflicts

Clean diffs

Easy Odoo 17 → 18 → 19 upgrades