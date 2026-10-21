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
```

**Домовленості для всіх модулів:**

- У кожному модулі є `agenda.md` з планом лекції; слайди, якщо вони є, додані як PDF.
- Сторінки `.html` самодостатні: відкривайте їх просто з диска в браузері, без сервера та встановлення.
- Кожен результат на HTML-сторінці отримано реальним запуском прикладу на CPython 3.14.3.
- Кожен скрипт запускається окремо: `python module01/strings/basics.py`. Скрипти в `module02/if_statements/` і `module02/while_loop/` просять ввести дані.

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
