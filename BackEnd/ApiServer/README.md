Документация API: https://127.0.0.1/docs
(Временная ссылка) 89.223.64.134:8000/docs
# Пользователи
- Создание пользователя: POST /users/create
- Проверка авторизации: POST /users/auth
- Получение пользователя по id: GET /users/{id}
- Проверка типа пользователя (обычный пользователь, администратор или работник): GET /users/me
- Смена пароля: POST /users/change-password
# Платформы
- Добавление платформы: POST /platforms/create
- Получение платформы по id: GET /platforms/{id}
- Получение платформы по названию: GET /platforms/name/{platform_name}
- Получение списка типов платформ: GET /platforms/types
- Сокрытие платформы: POST /platforms/hide-platform/{platform_id}
- Удаление сокрытия платформы: POST /platforms/unhide-platform/{platform_id}
# Бронь
- Добавление брони: POST /booking/create
- Получение брони пользователя по токену: GET /booking
- Получение брони по id: GET /booking/{id}
- Генерация PDF файла брони: GET /booking/generate_pdf/{platform_id}
# Компании
- Добавление компании: POST /companies/create
- Добавление сотрудника: POST /companies/add_employee
- Получение списка всех компаний: GET /companies
- Получение компании по id: GET /companies/{company_id}
- Получение списка сотрудников: GET /companies/employees
- Получение списка платформ: GET /companies/platforms
- Получение платформы компании по id: GET /companies/platforms/{platform_id}
# Администраторы
- Добавление администратора: POST /admin/add
- Удаление администратора: DELETE /admin/delete/{admin_id}
- Сокрытие платформы: POST /admin/hide-platform/{platform_id}
- Удаление сокрытия платформы: POST /admin/unhide-platform/{platform_id}
- Подтверждение платформы: POST /admin/verify_platform/{platform_id}
- Подтверждение компании: POST /admin/verify_company/{company_id}
- Получение списка неподтвержденных платформ: GET /admin/get_unverified_platforms/