# TBF Anti-Forensics v1.0 ULTIMATE

> *"Privacy is not secrecy. Privacy is the power to selectively reveal oneself to the world."* – **Eric Hughes**

> *"The only way to ensure data is truly gone is to ensure the medium no longer recognizes it as data."* – **TBF Core**

---

## 🛡️ Про проєкт
**TBF Anti-Forensics** — це професійна консольна утиліта (CLI) для системного знищення даних. Інструмент розроблений для тих, хто розуміє, що звичайне "видалення" файлу — це лише ілюзія безпеки. 

Цей скрипт забезпечує:
* **Безповоротне знищення даних:** Перезапис байтів за військовими стандартами.
* **Anti-Forensics:** Затирання метаданих та рандомізація імен файлів перед їх видаленням.
* **RAM Purge:** Примусове очищення оперативної пам'яті для запобігання витокам у "залишковій" пам'яті.
* **Hardened Security:** Захист доступу через унікальний ключ авторизації.

---

## 🚀 Встановлення

```bash
# Оновлення системи
pkg update && pkg upgrade -y

# Встановлення залежностей
pkg install python git -y

# Клонування репозиторію
git clone [https://github.com/cocofembo-glitch/TBF-AntiForensics](https://github.com/cocofembo-glitch/TBF-AntiForensics)
cd TBF-AntiForensics

# Встановлення Python-бібліотек
pip install -r requirements.txt

# Запуск
python tbf_shredder.py
