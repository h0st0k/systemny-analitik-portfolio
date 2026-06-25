import json
import subprocess
import time

methods = ['fake', 'split', 'disorder', 'fakedsplit']
positions = [1, 5, 10]

for method in methods:
    for pos in positions:
        print(f"Тестируем: {method} + позиция {pos}")
        # Здесь нужно менять конфиг и проверять доступ
        # Это заглушка — реальный код будет делать запросы к YouTube
        time.sleep(1)
