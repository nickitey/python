def app(environ, start_response):
    data = b"Who are you?\nI didn't call you!\nGo fuck yourself!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
    
    
# Для запуска в терминале пиши 
# gunicorn -w 4 example:app
# А затем по адресу, который в stdout терминала 
# (Вероятнее всего это http://127.0.0.1:8000/)
# Ищи то, что возвращает эта программа:
# Who are you?
# I didn't call you!
# Go fuck yourself!
# NB: Это не работает с кириллицей