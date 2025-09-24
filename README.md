## 1) Запуск
1. Запустити Docker Desktop.
2. У корені проєкту:
```bash
  docker compose up -d
```

3. Відкрити http://localhost:8069 → створити базу `test_odoo`.

Master password: значення змінної `ODOO_ADMIN_PASSWD` з `.env`.
Email/Password адміністратора: будь-які.

## 2) Встановлення модуля
1. Увімкнути Developer Mode.
2. Apps → знайти **Керування бібліотекою** → Install.

## 3) REST перевірка
http://localhost:8069/library/books