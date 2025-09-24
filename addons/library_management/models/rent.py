from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    _name = "library.rent"
    _description = "Library Rent"
    _order = "rent_date desc"

    partner_id = fields.Many2one("res.partner", required=True, string="Користувач", ondelete="restrict")
    book_id = fields.Many2one("library.book", required=True, string="Книга", ondelete="restrict")
    rent_date = fields.Date(default=fields.Date.context_today, required=True, readonly=True, string="Дата видачі")
    return_date = fields.Date(string="Дата повернення")

    @api.constrains("book_id", "return_date")
    def _check_book_availability(self):
        for rec in self:
            if not rec.book_id:
                continue
            domain = [("book_id", "=", rec.book_id.id), ("return_date", "=", False), ("id", "!=", rec.id)]
            if self.search_count(domain):
                raise ValidationError("Цю книгу вже видано та її ще не повернули.")

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if rec.book_id and not rec.return_date:
            rec.book_id.write({"is_available": False})
        return rec

    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            if "return_date" in vals:
                if rec.return_date:
                    rec.book_id.write({"is_available": True})
                else:
                    if rec.book_id:
                        rec.book_id.write({"is_available": False})
        return res
