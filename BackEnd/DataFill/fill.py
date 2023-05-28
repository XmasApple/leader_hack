import base64
import json
import random
import re
from pathlib import Path

import requests

host = 'http://localhost:8000'

unauthorized_session = requests.Session()
unauthorized_session.headers.update({'Content-Type': 'application/json'})
unauthorized_session.headers.update({'Accept': 'application/json'})

user_auth_url = host + '/users/auth/'
admin_auth_data = {
    "email": 'admin',
    "password": 'admin',
    "life_time": 0
}
admin_auth_response = unauthorized_session.post(user_auth_url, data=json.dumps(admin_auth_data)).json()
admin_token = admin_auth_response['token']

admin_session = requests.Session()
admin_session.headers.update({'Content-Type': 'application/json'})
admin_session.headers.update({'Accept': 'application/json'})
admin_session.headers.update({'Authorization': 'Bearer ' + admin_token})

platform_types_url = host + '/platforms/types/'
platform_types_response = unauthorized_session.get(platform_types_url).json()


def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_random_number(length):
    import random
    import string
    return ''.join(random.choice(string.digits) for _ in range(length))


def company(company_directory):
    company_name = company_directory.name

    user_create_url = host + '/users/create/'

    company_director_create_data = {
        "email": generate_random_string(random.randint(5, 10)) + '@mail.ru',
        "password": "qwerty",
        "life_time": 0,
        "first_name": ["Иван", "Алексей", "Петр"][random.randint(0, 2)],
        "last_name": ["Иванов", "Алексеев", "Петров"][random.randint(0, 2)],
        "middle_name": ["Иванович", "Алексеевич", "Петрович"][random.randint(0, 2)],
        "phone_number": "79" + generate_random_number(9),
    }

    company_director_create_response = unauthorized_session.post(user_create_url,
                                                                 data=json.dumps(company_director_create_data)).json()
    company_director_token = company_director_create_response['token']

    company_director_session = requests.Session()
    company_director_session.headers.update({'Content-Type': 'application/json'})
    company_director_session.headers.update({'Accept': 'application/json'})
    company_director_session.headers.update({'Authorization': 'Bearer ' + company_director_token})

    company_logo = None
    for file in company_directory.iterdir():
        if re.match(r'logo\..*', file.name):
            with open(file, 'rb') as f:
                company_logo = base64.b64encode(f.read()).decode('utf-8')
                break

    description = open(company_directory / 'description.txt', 'r', encoding='utf-8').read()

    company_create_data = {
        "TIN": generate_random_number(12),
        "name": company_name,
        "legal_name": f"ООО {company_name}",
        "phone_number": "79" + generate_random_number(9),
        "description": description,
        "job_title": ["Директор", "Генеральный директор", "Руководитель"][random.randint(0, 2)],
        "logo": company_logo,
    }

    company_create_url = host + '/companies/create/'
    company_create_response = company_director_session.post(company_create_url,
                                                            data=json.dumps(company_create_data)).json()

    verify_company_id_url = host + '/admin/verify_company/' + str(company_create_response['company_id'])
    verify_company_id_response = admin_session.post(verify_company_id_url).json()
    print(f'{verify_company_id_response=}')

    for platform_dir in company_directory.iterdir():
        if not platform_dir.is_dir():
            continue
        platform(company_director_session, platform_dir)


def platform(company_director_session, platform_dir):
    logo = None
    for file in platform_dir.iterdir():
        if re.match(r'main\..*', file.name):
            with open(file, 'rb') as f:
                logo = base64.b64encode(f.read()).decode('utf-8')
                break
    if logo is None:
        return
    description = None
    with open(platform_dir / 'description.txt', 'r', encoding="utf8") as f:
        print(f.name)
        description = f.read()
        print(description)
    if description is None:
        return
    images = []
    for file in platform_dir.iterdir():
        if re.match(r'img_\d+\..*', file.name):
            with open(file, 'rb') as f:
                images.append(base64.b64encode(f.read()).decode('utf-8'))
    if len(images) == 0:
        return

    platform_create_data = {
        "name": platform_dir.name,
        "platform_type_id": random.choice(platform_types_response)['platform_type_id'],
        "square": random.random() * 100 + 10,
        "ceiling_height": random.random() * 10,
        "closest_station": ["Курская", "Чкаловская", "Красные ворота"][random.randint(0, 2)],
        "people_capacity": random.randint(1, 1000),
        "rent_type": 1,
        "price_per_time": random.randint(500, 1000),
        "geo_tag": ["55.755814,37.617635", "55.755814,37.617635", "55.755814,37.617635"][random.randint(0, 2)],
        "description": description,
        "main_image": logo,
        "images": images,
    }

    platform_create_url = host + '/platforms/create/'
    platform_create_response = company_director_session.post(platform_create_url,
                                                             data=json.dumps(platform_create_data)).json()
    print(f'{platform_create_response=}')

    verify_platform_id_url = host + '/admin/verify_platform/' + str(platform_create_response['platform_id'])
    verify_platform_id_response = admin_session.post(verify_platform_id_url).json()
    print(f'{verify_platform_id_response=}')


def main():
    path = Path('Компании')
    for directory in path.iterdir():
        if not directory.is_dir():
            continue
        company(directory)


if __name__ == '__main__':
    main()
