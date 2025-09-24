{
    "name": "Керування бібліотекою",
    "summary": "Облік книг та видач",
    "description": "Модуль для керування книгами та видачами в бібліотеці.",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "author": "Test Assignment",
    "website": "https://library_management.com",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/rent_views.xml",
        "views/wizard_views.xml",
        "views/menu.xml"
    ],
    "application": True,
    "installable": True
}
