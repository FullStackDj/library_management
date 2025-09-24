from odoo import fields, models
from odoo.exceptions import UserError


class LibraryRentWizard(models.TransientModel):
    _name = "library.rent.wizard"
    _description = "Library Rent Wizard"

    partner_id = fields.Many2one("res.partner", required=True, string="Користувач", ondelete="restrict")

    def action_confirm(self):
        self.ensure_one()
        active_id = self.env.context.get("active_id")
        if not active_id:
            raise UserError("Книгу не знайдено.")
        book = self.env["library.book"].browse(active_id)
        if not book:
            raise UserError("Книгу не знайдено.")
        self.env["library.rent"].create({"partner_id": self.partner_id.id, "book_id": book.id})
        return {"type": "ir.actions.act_window_close"}
