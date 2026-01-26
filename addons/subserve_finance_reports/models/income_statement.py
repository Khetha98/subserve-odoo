from odoo import models, fields, api

class IncomeStatementReport(models.TransientModel):
    _name = 'subserve.income.statement.wizard'
    _description = 'Income Statement Wizard'

    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)

    def get_lines(self):
        lines = self.env['account.move.line'].read_group(
            domain=[
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to),
                ('account_id.account_type', 'in', ['income', 'expense']),
                ('move_id.state', '=', 'posted'),
            ],
            fields=['debit', 'credit', 'account_id'],
            groupby=['account_id'],
        )
        result = []
        for l in lines:
            # For Income/Expense, balance is usually Credit - Debit for Income 
            # or Debit - Credit for Expense. Standardized here as Debit - Credit.
            balance = l['debit'] - l['credit']
            if not self.env.company.currency_id.is_zero(balance):
                result.append({
                    'account': l['account_id'][1], # Get the name from the m2o tuple
                    'balance': balance,
                })
        return result
    
    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.income_statement_pdf'
        ).report_action(self)

