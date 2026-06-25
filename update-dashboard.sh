#!/bin/bash

echo "# 📊 Дашборд системного аналитика" > dashboard.md
echo "" >> dashboard.md
echo "## 📈 Прогресс по кейсам" >> dashboard.md
echo "| Кейс | Артефактов | Статус |" >> dashboard.md
echo "|------|------------|--------|" >> dashboard.md

for case in 01-library-case 02-vet-clinic-case 03-data-analysis 04-coworking-case 05-yandex-maps-voice 06-tools-environment; do
  if [ -d "$case" ]; then
    count=$(ls -1 "$case"/*.md 2>/dev/null | wc -l)
    echo "| $case | $count | ✅ Готово |" >> dashboard.md
  fi
done

echo "" >> dashboard.md
echo "## 📂 Проекты" >> dashboard.md
echo "- [sistemny-analitik-portfolio](https://github.com/k0sm0xyz/sistemny-analitik-portfolio) — портфолио" >> dashboard.md
echo "- [zapret-socks](https://github.com/k0sm0xyz/zapret-socks) — DPI-обход" >> dashboard.md
echo "" >> dashboard.md
echo "## 📊 Активность" >> dashboard.md
echo "- [GitHub Activity](https://github.com/k0sm0xyz)" >> dashboard.md
echo "- [Telegram](https://t.me/k0sm0xyz)" >> dashboard.md
echo "" >> dashboard.md
echo "## 🏷️ Статус проектов" >> dashboard.md
echo "| Проект | Статус |" >> dashboard.md
echo "|--------|--------|" >> dashboard.md
echo "| Портфолио | 🟢 Активно |" >> dashboard.md
echo "| zapret-socks | 🟢 Активно |" >> dashboard.md
echo "| android-tests | 🟡 В процессе |" >> dashboard.md

echo "✅ Дашборд обновлён!"
