from odoo import models, fields, api

class IncomeStatementReport(models.TransientModel):
    _name = 'subserve.income.statement.wizard'
    _description = 'Income Statement Wizard'

    date_from = fields.Date(required=True, default=fields.Date.context_today)
    date_to = fields.Date(required=True, default=fields.Date.context_today)

    def get_report_data(self):
            lines = self.env['account.move.line'].read_group(
                domain=[
                    ('date', '>=', self.date_from),
                    ('date', '<=', self.date_to),
                    ('account_id.account_type', 'in', ['income', 'income_other', 'expense', 'expense_direct_cost', 'expense_depreciation']),
                    ('move_id.state', '=', 'posted'),
                ],
                fields=['debit', 'credit', 'account_id'],
                groupby=['account_id'],
                lazy=False
            )

            # Correct initialization
            data = {
                'revenue': {'lines': [], 'total': 0.0},
                'cos': {'lines': [], 'total': 0.0},
                'other_income': {'lines': [], 'total': 0.0},
                'expenses': {'lines': [], 'total': 0.0},
            }

            for l in lines:
                account = self.env['account.account'].browse(l['account_id'][0])
                acc_type = account.account_type
                balance = l['credit'] - l['debit']
                
                if 'expense' in acc_type:
                    balance = l['debit'] - l['credit']

                entry = {'account': l['account_id'][1], 'balance': balance}

                if acc_type == 'income':
                    data['revenue']['lines'].append(entry)
                    data['revenue']['total'] += balance
                elif acc_type == 'expense_direct_cost':
                    data['cos']['lines'].append(entry)
                    data['cos']['total'] += balance
                elif acc_type == 'income_other':
                    data['other_income']['lines'].append(entry)
                    data['other_income']['total'] += balance
                else:
                    data['expenses']['lines'].append(entry)
                    data['expenses']['total'] += balance

            return data


    def action_print(self):
        return self.env.ref('subserve_finance_reports.income_statement_pdf').report_action(self)