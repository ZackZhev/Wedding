# Wedding Invite — Flask (из Canvas)

Мобильный шаблон + админка. Ваша фотография уже подключена как hero (/static/images/hero.jpg).

## Запуск
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Откройте: http://127.0.0.1:5000  
Админка: http://127.0.0.1:5000/admin

## Редактирование
- Меняйте `config.json` вручную или в админке `/admin` (после «Сохранить» нажмите «Обновить превью»).
- CLI:
```bash
python update_images.py set-hero ./my_photos/hero.jpg
python update_images.py add-gallery ./my_photos/1.jpg ./my_photos/2.jpg
```