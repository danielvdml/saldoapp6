# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .number_to_letter import to_word 

class ResPartner(models.Model):
    _inherit = ['res.partner']
    agente_de_retencion = fields.Boolean("Agente de Retención")    

class AccountInvoice(models.Model):
    _inherit = ['account.invoice']

    amount_total_word = fields.Char("Monto Total en Palabras",store=True, readonly=True,compute="_compute_amount")
    amount_iva_retenido = fields.Monetary("IVA Retenido",store=True, readonly=True,default=0,compute="_compute_amount", currency_field='currency_id')
    afecto_a_retencion = fields.Boolean("Afecto a Retención")

    
    @api.model
    def default_get(self, fields):
        res = super(AccountInvoice, self).default_get(fields)
        res.update({
            "afecto_a_retencion":self.partner_id.agente_de_retencion
        })
        return res

    
    @api.onchange('partner_id')
    def _onchange_field(self):
        self.afecto_a_retencion = self.partner_id.agente_de_retencion
    
    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type')
    def _compute_amount(self):
        round_curr = self.currency_id.round
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)
        if self.afecto_a_retencion and self.amount_untaxed >= 100:
            self.amount_iva_retenido = self.amount_untaxed*.01
        else:
            self.amount_iva_retenido = 0

        self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids)
        self.amount_total = self.amount_untaxed + self.amount_tax - self.amount_iva_retenido
        amount_total_company_signed = self.amount_total
        amount_untaxed_signed = self.amount_untaxed
        if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
            currency_id = self.currency_id
            amount_total_company_signed = currency_id._convert(self.amount_total, self.company_id.currency_id, self.company_id, self.date_invoice or fields.Date.today())
            amount_untaxed_signed = currency_id._convert(self.amount_untaxed, self.company_id.currency_id, self.company_id, self.date_invoice or fields.Date.today())
        sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
        self.amount_total_company_signed = amount_total_company_signed * sign
        self.amount_total_signed = self.amount_total * sign
        self.amount_untaxed_signed = amount_untaxed_signed * sign

        
        self.amount_total_word = to_word(self.amount_total,self.currency_id.name)