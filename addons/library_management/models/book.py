from odoo import fields, models


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char(required=True, string="Назва")
    author = fields.Char(string="Автор")
    published_date = fields.Date(string="Дата публікації")
    is_available = fields.Boolean(default=True, string="Доступна")

    def action_open_rent_wizard(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Видача книги",
            "res_model": "library.rent.wizard",
            "view_mode": "form",
            "view_id": self.env.ref("library_management.library_rent_wizard_form").id,
            "target": "new",
            "context": {"active_id": self.id, "active_model": self._name},
        }
