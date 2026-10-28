# Python Core

[English](README.md) · **Українська**

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)

Матеріали лекцій курсу Python Core. Кожен модуль — це одна лекція: слайди, план лекції, інтерактивні
сторінки та скрипти, які роблять **одну ідею** відчутною: запустіть, змініть, прочитайте, чому змінився
результат.

Модулі додаються в міру проведення лекцій; повна попередня ітерація курсу — [PythonCoreI3](https://github.com/OlegAndrus12/PythonCoreI3).

<img src="yoda.jpg" alt="May the Force be with you" width="280">

```
├── module01/   Типи даних: вбудовані типи, змінність, типізація, пріоритет операторів, колекції, перетворення
├── module02/   Керуючі конструкції: if / elif / else, тернарний оператор, цикли for і while, винятки, перші функції
├── module03/   Дата, час і випадковість: datetime, timedelta, часові пояси, UTC, time, calendar, random
├── module04/   Рядки: f-рядки та специфікація формату, старі способи форматування, методи рядків, спецсимволи, regex
├── module05/   Файли: open() і його режими, читання й запис, текстовий і двійковий режими, кодування, seek / tell, with
```

**Домовленості для всіх модулів:**

- У кожному модулі є `agenda.md` з планом лекції; слайди, якщо вони є, додані як PDF.
- Сторінки `.html` самодостатні: відкривайте їх просто з диска в браузері, без сервера та встановлення.
- Кожен результат на HTML-сторінці отримано реальним запуском прикладу на CPython 3.14.3.
- Кожен скрипт запускається окремо: `python module01/strings/basics.py`. Скрипти в `module02/if_statements/` і `module02/while_loop/`, а також `module04/methods/_strip.py` просять ввести дані.
- Скрипти в `module05/_open/` і `module04/ip_aggregator/straightforward.py` відкривають файли за відносним шляхом — запускайте їх з їхньої папки.

---

# Модуль 01 — Типи даних

Що таке кожен вбудований тип, що він уміє, і ідеї, які пояснюють більшість несподіванок для початківців:
імена — це посилання, одні об'єкти змінюються на місці, а інші ніколи, і Python перевіряє типи під час
виконання, але ніколи не перетворює їх мовчки.

| Файл | Що це |
| --- | --- |
| **[python-data-types.html](module01/python-data-types.html)** | Інтерактивна шпаргалка: окрема вкладка для кожного вбудованого типу плюс п'ять концептуальних вкладок (нижче) |
| **[visualizer.html](module01/visualizer.html)** | Введіть `a = [1, "hi"]`, `b = a`, `a.append(99)`, `del a` і подивіться, як імена вказують на об'єкти в купі — з лічильниками посилань, інтернуванням малих цілих, збиранням сміття та байткодом кожного рядка |
| **[collections.md](module01/collections.md)** | `list` / `tuple` / `set` / `dict` / `str` в одній таблиці, складність кожної операції і коли що використовувати |
| **[strong_dynamic.txt](module01/strong_dynamic.txt)** | Статична й динамічна типізація: переваги та недоліки кожної |
| **[Intro.pdf](module01/Intro.pdf)** | Слайди лекції |

**Приклади скриптів** — кожен відтворює реальну ситуацію (плейлист, профіль користувача, відповідь API):

| Скрипт | Що показує |
| --- | --- |
| [strings/basics.py](module01/strings/basics.py) | Три способи форматування рядка, методи регістру, пошук і перевірки, зміна, split і join, зрізи, `IndexError` |
| [lists/basics.py](module01/lists/basics.py) | Плейлист: додавання, видалення та пошук треків, сортування (зокрема `key=len`), зрізи, копіювання, `IndexError` |
| [tuples/basics.py](module01/tuples/basics.py) | Створення (і кома в кортежі з одного елемента), доступ, розпакування, незмінність, методи, кортеж проти списку, кортежі як ключі словника |
| [tuples/use_cases.py](module01/tuples/use_cases.py) | Вісім реальних застосувань: координати, повернення кількох значень, розпакування рядків CSV, складені ключі, дедуплікація записів, обмін значень, константи, ключі сортування |
| [sets/basics.py](module01/sets/basics.py) | `add` / `remove` / `discard`, дедуплікація, операції над множинами — з [діаграмою](module01/sets/Python-Set-Operatioons.png) |
| [dicts/basics.py](module01/dicts/basics.py) | Профіль користувача, товар у магазині, HTTP-відповідь, налаштування застосунку; що може і що не може бути ключем; `KeyError` |
| [dicts/list_of_dicts.py](module01/dicts/list_of_dicts.py) | Список словників — вихідні дані для вправ |
| [conversions/basics.py](module01/conversions/basics.py) | Перетворення між `int`, `float`, `bool`, `None`, `str`, `list`, `set` і `dict`, а також ланцюжки перетворень |
| [deposit.py](module01/deposit.py) | Розбір рядків конфігурації `KEY=value` у словник з пропуском коментарів |

**Шпаргалка, вкладка за вкладкою:**

| Вкладка | Що в ній |
| --- | --- |
| `int` `None` `str` `bool` `list` `dict` `tuple` `set` | Літерали, ключові властивості, кожен публічний метод з прикладом і операції, на яких часто помиляються. Для `bool` є таблиця істинності |
| **Змінність** | Карта змінних і незмінних типів; діаграми пам'яті для `b.append()` і `t += '!'`; наслідки для ключів словника, аргументів за замовчуванням і копіювання |
| **Типізація** | Статична/динамічна × сильна/слабка на одній схемі; коли ловиться помилка типу (під час компіляції, виконання чи mypy); той самий вираз у Python, JavaScript і Java |
| **Пріоритети** | Усі 18 рівнів з асоціативністю, дерево виразу, яке показує, як Python розставляє дужки в `1 + 2 * 3 ** 2 > 10 and not False`, і 17 пасток на кшталт `-2 ** 2` |
| **Колекції** | `list` / `tuple` / `set` / `dict` / `str` поруч, Big-O кожної операції, чому `in` для множини — O(1), і блок-схема «що мені потрібно?» |
| **Порівняння** | Усі вісім типів в одній таблиці |

📋 Повний перелік тем: **[module01/agenda.md](module01/agenda.md)**

---

# Модуль 02 — Керуючі конструкції

Як змусити програму вибирати й повторювати: розгалуження з `if`, цикли `for` і `while`, вбудовані функції,
які роблять цикли читабельними, і обробка винятків. Лекція завершується ідеєю функцій.

| Файл | Що це |
| --- | --- |
| **[python-control-flow.html](module02/python-control-flow.html)** | Інтерактивна шпаргалка: окрема вкладка для `if`, `while`, `for` і `try` / `except` — синтаксис, ключові правила, покроковий показ того, як це виконує інтерпретатор, ієрархія винятків, приклади та підводні камені |
| **[caesar_visualizer.html](module02/functions/caesar/caesar_visualizer.html)** | Шифр Цезаря літера за літерою: кожна літера стає числом, зсувається і повертається на початок алфавіту; з повною таблицею заміни |

**Оператор `if`** — інтерактивні, кожен скрипт просить ввести дані:

| Скрипт | Що показує |
| --- | --- |
| [if_statements/01.py](module02/if_statements/01.py) | Перевірка входу: вкладені `if` / `elif` / `else` |
| [if_statements/02.py](module02/if_statements/02.py) | Порівняння двох чисел |
| [if_statements/03.py](module02/if_statements/03.py) | Поєднання умов через `and` / `or` |
| [if_statements/04.py](module02/if_statements/04.py) | Перевірка входження через `in` / `not in` |
| [if_statements/06.py](module02/if_statements/06.py) | Високосний рік — порядок умов має значення |
| [if_statements/ternary.py](module02/if_statements/ternary.py) | Тернарний оператор: `value_if_true if condition else value_if_false` |

**Цикли `for`:**

| Скрипт | Що показує |
| --- | --- |
| [for_loop/basics.py](module02/for_loop/basics.py) | Обхід списку, рядка і `range` |
| [for_loop/break_continue.py](module02/for_loop/break_continue.py) | `break` на першому критичному рядку логу; `continue`, щоб пропустити елементи |
| [for_loop/building_collections.py](module02/for_loop/building_collections.py) | Фільтрація в новий список: файли `.py`, невдалі HTTP-відповіді |
| [for_loop/enumerate.py](module02/for_loop/enumerate.py) | `enumerate(..., start=1)` — нумерований лог комітів |
| [for_loop/zip.py](module02/for_loop/zip.py) | `zip` — паралельний обхід двох списків |
| [for_loop/nested.py](module02/for_loop/nested.py) | Вкладені цикли: розклад на тиждень, кругова система матчів |

**Цикли `while`** — інтерактивні, кожен скрипт просить ввести дані:

| Скрипт | Що показує |
| --- | --- |
| [while_loop/digit_sum.py](module02/while_loop/digit_sum.py) | Сума цифр числа через `% 10` і `//= 10` |
| [while_loop/guess.py](module02/while_loop/guess.py) | Вгадай число: цикл, поки відповідь не правильна, з підрахунком спроб |
| [while_loop/menu.py](module02/while_loop/menu.py) | Меню гри: `while True` з `break` для виходу і `continue` при неправильному введенні |
| [while_loop/menu_enum.py](module02/while_loop/menu_enum.py) | Те саме меню з `Enum` і `match` / `case` замість порівняння рядків |

**Функції:**

| Скрипт | Що показує |
| --- | --- |
| [functions/01_functions.py](module02/functions/01_functions.py) | Реєстрація пацієнта в клініці: ІМТ, аргументи за замовчуванням та іменовані аргументи, перевірка введення і ранній вихід, повернення кількох значень, поєднання маленьких функцій |
| [functions/caesar/main.py](module02/functions/caesar/main.py) | `encrypt(key, message)` — шифр Цезаря, на якому побудовано візуалізатор |

📋 Повний перелік тем: **[module02/agenda.md](module02/agenda.md)**

---

# Модуль 03 — Дата, час і випадкові числа

Робота з датою та часом — створення, форматування, розбір, арифметика і перетворення між часовими
поясами — а також модуль `random`.

| Файл | Що це |
| --- | --- |
| **[python-date-random.html](module03/python-date-random.html)** | Інтерактивна шпаргалка: вкладки для `datetime`, `date`, `time`, `timedelta`, часових поясів (`timezone` і `zoneinfo`), UTC, модуля `time`, `calendar`, `random`, усіх кодів `strftime` / `strptime` і готових рецептів |
| **[formats.md](module03/formats.md)** | Усі коди форматування `strftime` / `strptime`, кожен показаний на одній і тій самій даті |

**Скрипти про дату й час:**

| Скрипт | Що показує |
| --- | --- |
| [date/01_dt.py](module03/date/01_dt.py) | Створення `datetime`, розбиття на `date()` і `time()`, `now()` і `today()` |
| [date/02_dt.py](module03/date/02_dt.py) | Розбір рядка через `strptime`, `replace()`, різниця двох дат — це `timedelta` |
| [date/03_dt.py](module03/date/03_dt.py) | Додавання `timedelta` до поточного часу |
| [date/04_dt.py](module03/date/04_dt.py) | `strftime("%B")` / `"%A"` — назва місяця чи дня тижня |
| [date/05_dt.py](module03/date/05_dt.py) | Усі дні між двома датами через `range` і `timedelta(days=i)` |
| [date/06_dt.py](module03/date/06_dt.py) | Порядковий номер дня, timestamp, `ctime` та ISO-формат — і відновлення `datetime` з кожного |
| [date/07_dt.py](module03/date/07_dt.py) | `datetime.combine`, `timedelta.total_seconds()`, рух назад у часі |
| [date/08_dt.py](module03/date/08_dt.py) | `calendar`: `isleap`, `monthrange`, `weekday`, `monthcalendar` |
| [date/09_age_and_birthdays.py](module03/date/09_age_and_birthdays.py) | HR / CRM: точний вік і в кого з команди день народження цього тижня (з урахуванням 29 лютого) |
| [date/10_utc.py](module03/date/10_utc.py) | UTC крок за кроком: naive проти aware, перетворення з місцевого часу й назад, фіксований зсув проти `ZoneInfo` і літній час |
| [date/11_log_parsing.py](module03/date/11_log_parsing.py) | DevOps: розбір часу з лог-файлу і виведення в ISO та зручному для людини форматі |
| [date/12_meeting_across_timezones.py](module03/date/12_meeting_across_timezones.py) | Одна зустріч за часом Києва, Стокгольма й Техасу; чому не можна змішувати naive і aware |
| [date/timezones3.py](module03/date/timezones3.py) | `zoneinfo` (стандартна бібліотека): прив'язка часового поясу, перетворення через `astimezone()`, naive → aware |
| [date/timezones.py](module03/date/timezones.py), [timezones2.py](module03/date/timezones2.py) | Те саме зі сторонніми пакетами `pytz` і `dateutil` (`pip install pytz python-dateutil`) |
| [date/calend.py](module03/date/calend.py) | `calendar.calendar(year)` і `calendar.month_name` |
| [date/deal_time.py](module03/date/deal_time.py) | `time.sleep()` у циклі |

**Скрипти з `random`:**

| Скрипт | Що показує |
| --- | --- |
| [random/01_rd.py](module03/random/01_rd.py) | `randint` — підкидання монети |
| [random/02_rd.py](module03/random/02_rd.py) | Підкидати монету, поки одна сторона не випаде чотири рази поспіль |
| [random/03_rd.py](module03/random/03_rd.py) | Bogosort: `shuffle` списку, поки він випадково не стане відсортованим |
| [random/04_rd.py](module03/random/04_rd.py) | `choices` — генерація випадкового автомобільного номера |
| [random/05_rd.py](module03/random/05_rd.py) | `choice` проти `sample` проти `choices`: один елемент, унікальні елементи, елементи з повтореннями |
| [random/06_rd.py](module03/random/06_rd.py) | `random()`, `uniform()` і `seed()` для відтворюваних результатів |

📋 Повний перелік тем: **[module03/agenda.md](module03/agenda.md)**

---

# Модуль 04 — Рядки та регулярні вирази

Як вивести дані саме в потрібному вигляді, методи рядків, які знадобляться щодня, і регулярні вирази
для пошуку тексту за його формою.

| Файл | Що це |
| --- | --- |
| **[python-strings-regex.html](module04/python-strings-regex.html)** | Інтерактивна шпаргалка: вкладки для f-рядків, `%` і `str.format()`, методів `str`, модуля `re`, повної специфікації формату, спецсимволів і сирих рядків та синтаксису regex |
| **[formated_string/cheatsheet.md](module04/formated_string/cheatsheet.md)** | Специфікація формату на одній сторінці: вирівнювання й заповнення, числа, системи числення, відсотки, дати |
| **[reg/cheatsheet.md](module04/reg/cheatsheet.md)** | Regex на одній сторінці: функції `re`, класи й набори символів, якорі, квантифікатори (жадібні й ліниві), групи, альтернатива, lookahead / lookbehind, прапорці, `re.sub` з функцією |
| **[methods/moderate_visualizer.html](module04/methods/moderate_visualizer.html)** | Модератор контенту крок за кроком: як `find` у копії в нижньому регістрі знаходить заборонені слова і чому перевірка меж слова не чіпає `class` |

**Форматування рядків:**

| Скрипт | Що показує |
| --- | --- |
| [formated_string/01.py](module04/formated_string/01.py) | Вирівнювання ліворуч, праворуч і по центру у фіксованій ширині |
| [formated_string/02.py](module04/formated_string/02.py) | Таблиця чисел 0–15 у десятковій, шістнадцятковій і двійковій системах |
| [formated_string/03.py](module04/formated_string/03.py) | `:.2%` проти ручного обчислення відсотка |
| [formated_string/04.py](module04/formated_string/04.py) | `f"{x=}"` для налагодження, багаторядкові f-рядки, умова всередині `{}` |
| [formated_string/05.py](module04/formated_string/05.py) | Числа: розділювач тисяч, точність, експоненційний запис, знак, доповнення нулями, системи числення, відсотки |
| [formated_string/06.py](module04/formated_string/06.py) | Дати у f-рядках: `f"{d:%d.%m.%Y}"`, чому там не працює вирівнювання, форматування `timedelta` |
| [formated_string/08.py](module04/formated_string/08.py) | Старі способи: оператор `%` і `str.format()`, шаблони для повторного використання |
| [formated_string/09.py](module04/formated_string/09.py) | `ljust`, `rjust`, `center`, `zfill` — і зміст книги з крапками |
| [formated_string/10.py](module04/formated_string/10.py) | Практика: чек з магазину з вирівняними колонками, знижкою й підсумком |
| [formated_string/special_symbols.py](module04/formated_string/special_symbols.py) | `\n`, `\f`, `\r`, `\t`, `\v` — що кожен робить із виведенням |

**Методи рядків:**

| Скрипт | Що показує |
| --- | --- |
| [methods/_case_and_search.py](module04/methods/_case_and_search.py) | Регістр, `startswith` / `endswith`, `count`, `find` проти `index`, `rfind`, доповнення |
| [methods/_isdigit_isalpha.py](module04/methods/_isdigit_isalpha.py) | `isdigit`, `isalpha`, `isalnum`, `isspace`, `isupper` / `islower`; перевірка введення користувача |
| [methods/_split.py](module04/methods/_split.py) | `split`: найдовше слово, найдовший ланцюжок голосних |
| [methods/_join.py](module04/methods/_join.py) | `join` — відсортовані ключі словника одним рядком |
| [methods/_replace.py](module04/methods/_replace.py) | `replace` у циклі, щоб прибрати повторювані коми |
| [methods/_strip.py](module04/methods/_strip.py) | `strip` перед порівнянням введення користувача — просить ввести дані |
| [methods/validate_password.py](module04/methods/validate_password.py) | Практика: перевірка надійності пароля — які правила виконано, а які ні |
| [methods/slugify.py](module04/methods/slugify.py) | Практика: перетворити заголовок статті на URL-slug за допомогою `strip`, `lower`, `split` і `join` |
| [methods/moderate.py](module04/methods/moderate.py) | Практика: замінити заборонені слова на `*` — без урахування регістру, лише цілі слова, решта тексту без змін |

**Регулярні вирази:**

| Скрипт | Що показує |
| --- | --- |
| [reg/match_vs_search2.py](module04/reg/match_vs_search2.py) | `re.match` (лише початок рядка) проти `re.search` (будь-де) на рядках логів і URL |
| [reg/anchors.py](module04/reg/anchors.py) | `^` і `$`: починається з, закінчується на, перевірка всього рядка на формат `YYYY-MM-DD` |
| [reg/_split.py](module04/reg/_split.py) | `re.split`: послідовності пробілів, кілька роздільників одразу, `maxsplit`, збереження роздільника через групу |
| [reg/split_recipients.py](module04/reg/split_recipients.py) | Практика: поле «Кому:» листа — розбити за будь-яким роздільником, прибрати порожні рядки й дублікати, позначити некоректні адреси |
| [reg/card_mask.py](module04/reg/card_mask.py) | Маскування номерів карток через `re.sub` і зворотне посилання; `group()`, `groups()`, `finditer`, іменовані групи |
| [reg/phone_normalize.py](module04/reg/phone_normalize.py) | Телефонні номери в будь-якому форматі — до одного: `\D`, щоб прибрати все, крім цифр |
| [reg/password_validate.py](module04/reg/password_validate.py) | Знову перевірка пароля, по одному regex на правило |
| [reg/slugify.py](module04/reg/slugify.py) | Знову генератор slug — одним `re.sub` |
| [reg/moderate.py](module04/reg/moderate.py) | Знову модератор: межі слова `\b`, `re.IGNORECASE`, `re.sub` з функцією |
| [reg/emails.py](module04/reg/emails.py) | `findall` для email-адрес і група, щоб витягти лише домен |
| [reg/find_urls.py](module04/reg/find_urls.py) | `https?://` — пошук посилань у тексті |
| [reg/hashtags_mentions.py](module04/reg/hashtags_mentions.py) | `#хештеги` і `@згадки` з підпису до допису |
| [reg/price_extract.py](module04/reg/price_extract.py) | Екранування `$` і `.`, щоб витягти ціни з опису |
| [reg/parse_ips.py](module04/reg/parse_ips.py) | `re.compile` і `findall` для IPv4-адрес |
| [reg/commatose.py](module04/reg/commatose.py) | `,+` — прибрати повторювані коми одним `sub` (порівняйте з `methods/_replace.py`) |
| [reg/find_max_vowels.py](module04/reg/find_max_vowels.py) | Найдовший ланцюжок голосних одним рядком (порівняйте з `methods/_split.py`) |

**Практика: аналіз логів** — [ip_aggregator/logs.txt](module04/ip_aggregator/logs.txt) — приклад логу Django:

| Скрипт | Що показує |
| --- | --- |
| [ip_aggregator/straightforward.py](module04/ip_aggregator/straightforward.py) | Перша спроба: знайти IP у кожному рядку й порахувати запити з кожної адреси |
| [ip_aggregator/log_analyser.py](module04/ip_aggregator/log_analyser.py) | Шаблон з коментарями та іменованими групами: кількість записів кожного рівня з діаграмою і топ IP за кількістю помилок |

📋 Повний перелік тем: **[module04/agenda.md](module04/agenda.md)**

---

# Модуль 05 — Робота з файлами

Читання й запис файлів: `open()` і його режими, читання всього файлу або рядок за рядком, текстовий і
двійковий режими, кодування, переміщення у файлі за допомогою `seek` / `tell` і чому `with` закриває файл
за вас.

| Скрипт | Що показує |
| --- | --- |
| [_open/ex_01.py](module05/_open/ex_01.py) | Усі режими `open()` — `r`, `w`, `x`, `a`, `b`, `t`, `+` — в одній таблиці |
| [_open/ex_02.py](module05/_open/ex_02.py) | Дописування у файл через `"a"`, потім `close()` (спробуйте `"x"`, щоб побачити помилку на наявному файлі) |
| [_open/ex_03.py](module05/_open/ex_03.py) | Читання перших N рядків через `readline()` і перехоплення `OSError` |
| [_open/ex_04.py](module05/_open/ex_04.py) | `write` проти `writelines` всередині `with` — і помилка, коли папки не існує |
| [_open/ex_05.py](module05/_open/ex_05.py) | Той самий текст у кодуваннях UTF-8, UTF-16 і cp1251, записаний і прочитаний у двійковому режимі |
| [_open/ex_06.py](module05/_open/ex_06.py) | Відкриття зображення в режимі `"rb"` — як виглядає двійковий файл у байтах |
| [_open/ex_07.py](module05/_open/ex_07.py) | `read(n)`, `tell()` і `seek(0)` — повторне читання тієї самої частини файлу |

📋 Повний перелік тем: **[module05/agenda.md](module05/agenda.md)**
