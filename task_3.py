# TODO Найдите количество книг, которое можно разместить на дискете

# Исходные данные
disk_size_mb = 1.44  # объем дискеты в Мб
pages_per_book = 100  # количество страниц в книге
lines_per_page = 50  # число строк на странице
chars_per_line = 25  # количество символов в строке
bytes_per_char = 4  # байт на символ

# Константы перевода единиц
bytes_per_kb = 1024  # 1 Кб = 1024 байта
kb_per_mb = 1024  # 1 Мб = 1024 Кб

# 1. Находим объем одной книги в байтах
# Количество символов в книге:
total_chars_per_book = pages_per_book * lines_per_page * chars_per_line
# Объем книги в байтах:
book_size_bytes = total_chars_per_book * bytes_per_char

# 2. Переводим объем дискеты в байты
disk_size_bytes = disk_size_mb * kb_per_mb * bytes_per_kb

# 3. Рассчитываем, сколько книг поместится на дискете
# Используем целочисленное деление, так как часть книги поместить нельзя
books_on_disk = int(disk_size_bytes // book_size_bytes)

# 4. Выводим результат
print("Количество книг, помещающихся на дискету:", books_on_disk)