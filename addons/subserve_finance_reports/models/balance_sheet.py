from odoo import models, fields, api

class BalanceSheetReport(models.TransientModel):
    _name = 'subserve.balance.sheet.wizard'
    _description = 'Balance Sheet Wizard'

    date_to = fields.Date(required=True)

    def get_report_data(self):
        aml = self.env['account.move.line']

        domain = [
            ('date', '<=', self.date_to),
            ('move_id.state', '=', 'posted'),
            ('display_type', 'not in', ('line_section', 'line_note')),
        ]

        lines = aml.read_group(
            domain=domain,
            fields=['debit', 'credit', 'account_id', 'account_id.account_type'],
            groupby=['account_id', 'account_id.account_type'],
        )

        data = {
            'assets': {'current': [], 'non_current': [], 'total': 0},
            'liabilities': {'current': [], 'non_current': [], 'total': 0},
            'equity': {'lines': [], 'total': 0},
        }

        for l in lines:
            account_name = l.get('account_id') and l['account_id'][1] or ''
            account_type = l.get('account_id_account_type') or ''

            if account_type.startswith(('liability', 'equity')):
                balance = l['credit'] - l['debit']
            else:
                balance = l['debit'] - l['credit']

            entry = {
                'account': account_name,
                'balance': balance,
            }

            if account_type in ('asset_cash', 'asset_receivable', 'asset_current'):
                data['assets']['current'].append(entry)
                data['assets']['total'] += balance

            elif account_type in ('asset_fixed', 'asset_non_current', 'asset_prepayments'):
                data['assets']['non_current'].append(entry)
                data['assets']['total'] += balance

            elif account_type in ('liability_current', 'liability_payable', 'liability_credit_card'):
                data['liabilities']['current'].append(entry)
                data['liabilities']['total'] += balance

            elif account_type == 'liability_non_current':
                data['liabilities']['non_current'].append(entry)
                data['liabilities']['total'] += balance

            elif account_type in ('equity', 'equity_unaffected'):
                data['equity']['lines'].append(entry)
                data['equity']['total'] += balance

        return data


    
    def action_print(self):
        return self.env.ref(
            'subserve_finance_reports.balance_sheet_pdf'
        ).report_action(self)

