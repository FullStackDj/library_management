import json
from odoo import http
from odoo.http import request, Response

class LibraryController(http.Controller):
    @http.route("/library/books", type="http", auth="public", methods=["GET"], csrf=False)
    def books(self, **kwargs):
        records = request.env["library.book"].sudo().search([])
        data = []
        for r in records:
            data.append({
                "id": r.id,
                "name": r.name,
                "author": r.author or "",
                "published_date": str(r.published_date) if r.published_date else "",
                "is_available": bool(r.is_available),
            })
        return Response(
            json.dumps({"books": data}),
            content_type="application/json;charset=utf-8",
            status=200,
        )
