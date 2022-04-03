## Часть №1
Задание:

    Создать веб-приложение , с API интерфейсом и админ-панелью.
    Создать базу данных используя миграции Django

Требования:
1. Информация о каждом сотруднике должна храниться в базе данных и содержать
следующие данные:

    • ФИО;

    • Должность;

    • Дата приема на работу;

    • Размер заработной платы;

    • Информация о выплаченной зарплате;

2. У каждого сотрудника есть 1 начальник;

3. База данных должна содержать 5 уровней иерархий;
Под иерархией понимается древовидная структура на подобие структурной схемы
предприятия. Например:
a) У генерального директора нет руководителей, но есть подчинённые. Его уровень
иерархии будет равен 0;
b) У менеджера среднего звена уровень иерархии 2. Все его подчинённые менеджеры
будут иметь уровень иерархии 3, а у его руководителя – уровень 1.
Важно отметить, что уровень иерархии определяется не названием должности, а
отношением к остальным сотрудникам.
4. На странице сотрудников в админ-панели должны выводиться:

    • ФИО.

    • Должность.

    • Ссылка на объект начальника.

    • Заработная плата.

    • Всего выплачено.

5. На странице сотрудников в админ-панели должны быть фильтры:

    • Должность.

    • Уровень.

6. На странице сотрудников в админ-панели должен быть action который удаляет всю
информацию о выплаченной заработной плате всех выбранных сотрудников.
7. Используя DRF, создать набор представлений:

    • Все данные о сотрудниках.

    • Все данные о сотрудниках одного уровня.

8. Сотрудники с определенной группой прав должны иметь доступ к API;

## Часть №2 (опциональная)

Задание:

    Заполнить базу данных.
    Автоматизировать процессы в приложении при помощи Celery.
    Настроить отдельный доступ к API.
    Настройте автоматическое развертывание проекта.
Требования:

1. Заполните базу данных при помощи:

    • DB seeder для Django ORM

    • При помощи скрипта.


2. Напишите несколько celery задач, что бы упростить работу с приложением в админ-
панели:

    • Задача должна запускаться автоматически каждые 2 часа и начислять сотруднику
заработную плату.

    • Если action применяется более чем к 20 сотрудникам, стирание данных должно
производиться асинхронно.


3. Пользователи могут получать доступ к API при помощи специального ключа.

    • Пользователь может получить информацию только о себе.


4. Проект должен разворачиваться при помощи файла docker-compose.
