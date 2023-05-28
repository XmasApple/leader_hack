import base64
import datetime
import random

import requests
import json

host = 'http://localhost:8000'


def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_random_number(length):
    import random
    import string
    return ''.join(random.choice(string.digits) for _ in range(length))


def main():
    unauthorized_session = requests.Session()
    unauthorized_session.headers.update({'Content-Type': 'application/json'})
    unauthorized_session.headers.update({'Accept': 'application/json'})

    # ====================
    # User tests
    # ====================

    # test users/create
    user_create_url = host + '/users/create/'
    user1_create_data = {
        "email": generate_random_string(10) + '@' + generate_random_string(5) + '.com',
        "password": generate_random_string(10),
        "life_time": 0,
        "first_name": "string",
        "last_name": "string",
        "middle_name": "string",
        "phone_number": generate_random_number(11)
    }
    user2_create_data = {
        "email": generate_random_string(10) + '@' + generate_random_string(5) + '.com',
        "password": generate_random_string(10),
        "first_name": "string",
        "last_name": "string",
        "middle_name": "string",
        "phone_number": generate_random_number(11)
    }

    user1_create_response = unauthorized_session.post(user_create_url, data=json.dumps(user1_create_data)).json()
    user2_create_response = unauthorized_session.post(user_create_url, data=json.dumps(user2_create_data)).json()

    print(f'{user1_create_response=}')
    print(f'{user2_create_response=}')

    # test users/auth
    user_auth_url = host + '/users/auth/'
    user1_auth_data = {
        "email": user1_create_data['email'],
        "password": user1_create_data['password'],
        "life_time": 0
    }
    admin_auth_data = {
        "email": 'admin',
        "password": 'admin',
        "life_time": 0
    }
    user1_auth_response = unauthorized_session.post(user_auth_url, data=json.dumps(user1_auth_data)).json()
    admin_auth_response = unauthorized_session.post(user_auth_url, data=json.dumps(admin_auth_data)).json()
    token1 = user1_auth_response['token']
    token2 = user2_create_response['token']
    admin_token = admin_auth_response['token']

    user1_session = requests.Session()
    user1_session.headers.update({'Content-Type': 'application/json'})
    user1_session.headers.update({'Accept': 'application/json'})
    user1_session.headers.update({'Authorization': 'Bearer ' + token1})

    user2_session = requests.Session()
    user2_session.headers.update({'Content-Type': 'application/json'})
    user2_session.headers.update({'Accept': 'application/json'})
    user2_session.headers.update({'Authorization': 'Bearer ' + token2})

    admin_session = requests.Session()
    admin_session.headers.update({'Content-Type': 'application/json'})
    admin_session.headers.update({'Accept': 'application/json'})
    admin_session.headers.update({'Authorization': 'Bearer ' + admin_token})

    # test users/me
    user_me_url = host + '/users/me/'
    user1_me_response = user1_session.get(user_me_url).json()
    user2_me_response = user2_session.get(user_me_url).json()
    admin_me_response = admin_session.get(user_me_url).json()

    print(f'{user1_me_response=}')
    print(f'{user2_me_response=}')
    print(f'{admin_me_response=}')

    # test users/
    user_url = host + '/users/'
    user1_response = unauthorized_session.get(user_url).json()
    print(f'{user1_response=}')

    # test users/{user_id}
    user_id_url = host + '/users/' + str(user1_me_response['user_id'])
    user1_id_response = unauthorized_session.get(user_id_url).json()
    print(f'{user1_id_response=}')

    # test users/change_password
    user_change_password_url = host + '/users/change-password/'
    user_change_password_data = {
        "email": user1_create_data['email'],
        "password": generate_random_string(10),
    }
    unauthorized_user_change_password_response = unauthorized_session.post(user_change_password_url,
                                                                           data=json.dumps(
                                                                               user_change_password_data)).json()
    user_change_password_response = user1_session.post(user_change_password_url,
                                                       data=json.dumps(user_change_password_data)).json()
    print(f'{unauthorized_user_change_password_response=}')
    print(f'{user_change_password_response=}')

    token1 = user_change_password_response['token']
    user1_session.headers.update({'Authorization': 'Bearer ' + token1})

    # ====================
    # Company tests
    # ====================

    # test companies/create
    company_create_url = host + '/companies/create/'
    company_create_data = {
        "TIN": generate_random_number(12),
        "name": generate_random_string(10),
        "legal_name": generate_random_string(10),
        "phone_number": generate_random_number(11),
        "description": "string",
        "job_title": "string",
        "logo": generate_random_string(10),
    }
    company_create_response = user1_session.post(company_create_url, data=json.dumps(company_create_data)).json()

    # companies/add_employee
    company_add_employee_url = host + '/companies/add_employee/'
    company_add_employee_data = {
        "user_id": user2_me_response['user_id'],
        "job_title": "string"
    }
    company_add_employee_response = user1_session.post(company_add_employee_url,
                                                       data=json.dumps(company_add_employee_data)).json()

    print(f'{company_create_response=}')
    print(f'{company_add_employee_response=}')

    # test companies/
    company_url = host + '/companies/'
    company_response = unauthorized_session.get(company_url).json()
    print(f'{company_response=}')

    # test companies/{company_id}
    company_id_url = host + '/companies/' + str(company_create_response['company_id'])
    unverified_company_id_response = unauthorized_session.get(company_id_url).json()
    print(f'{unverified_company_id_response=}')

    # test /admin/verify_company/{platform_id}

    verify_company_id_url = host + '/admin/verify_company/' + str(company_create_response['company_id'])
    verify_company_id_response = admin_session.post(verify_company_id_url).json()
    print(f'{verify_company_id_response=}')

    # test companies/employees
    company_employees_url = host + '/companies/employees/'
    company_employees_response = user1_session.get(company_employees_url).json()
    print(f'{company_employees_response=}')

    # ====================
    # Platform tests
    # ====================

    # test platforms/types
    platform_types_url = host + '/platforms/types/'
    platform_types_response = unauthorized_session.get(platform_types_url).json()
    print(f'{platform_types_response=}')

    # test platforms/create
    platform_create_url = host + '/platforms/create/'
    # load image logo.png as base64
    logo = None
    with open('test_logo.png', 'rb') as f:
        logo = base64.b64encode(f.read()).decode('utf-8')

    platform_create_data = {
        "name": generate_random_string(10),
        "platform_type_id": random.choice(platform_types_response)['platform_type_id'],
        "square": random.random() * 100,
        "ceiling_height": random.random() * 10,
        "closest_station": generate_random_string(10),
        "people_capacity": 10,
        "rent_type": 1,
        "price_per_time": random.randint(0, 1000),
        "description": generate_random_string(10),
        "geotag": generate_random_string(10),
        "main_image": logo,
        "images": [generate_random_string(10) for _ in range(random.randint(1, 10))]
    }
    platform_create_response = user1_session.post(platform_create_url, data=json.dumps(platform_create_data)).json()
    print(f'{platform_create_response=}')

    # test platforms/
    platform_url = host + '/platforms/'
    platform_response = unauthorized_session.get(platform_url).json()
    print(f'{platform_response=}')

    # test admin/verify_platform/{platform_id}
    verify_platform_id_url = host + '/admin/verify_platform/' + str(platform_create_response['platform_id'])
    verify_platform_id_response = admin_session.post(verify_platform_id_url).json()
    print(f'{verify_platform_id_response=}')

    # test platforms/{platform_id}
    platform_id_url = host + '/platforms/' + str(platform_create_response['platform_id'])
    platform_id_response = unauthorized_session.get(platform_id_url).json()
    print(f'{platform_id_response=}')

    # ====================
    # Booking tests
    # ====================

    # test booking/generate_pdf/{platform_id} (returns pdf as bytes)

    generate_pdf_url = host + '/booking/generate_pdf/' + str(platform_create_response['platform_id'])
    generate_pdf_response = user1_session.get(generate_pdf_url).content
    print(f'{generate_pdf_response=}')

    with open(f'platform_{platform_create_response["platform_id"]}.pdf', 'wb') as f:
        f.write(generate_pdf_response)

    # test booking/create

    now = datetime.datetime.now()

    booking_create_url = host + '/booking/create/'
    booking_create_data = {
        "user_id": user2_me_response['user_id'],
        "platform_id": platform_create_response['platform_id'],
        "number_of_persons": random.randint(1, 10),
        "start_date": (now + datetime.timedelta(hours=1)).isoformat(),
        "end_date": (now + datetime.timedelta(days=1)).isoformat(),
        "rent_type": platform_create_response['rent_type'],
        "comment": "string"
    }
    booking_invalid_create_data = {
        "user_id": user2_me_response['user_id'],
        "platform_id": platform_create_response['platform_id'],
        "number_of_persons": random.randint(1, 10),
        "start_date": (now + datetime.timedelta(hours=12)).isoformat(),
        "end_date": (now + datetime.timedelta(hours=36)).isoformat(),
        "rent_type": platform_create_response['rent_type'],
        "comment": "string"
    }
    booking_create_response = user2_session.post(booking_create_url, data=json.dumps(booking_create_data)).json()
    booking_invalid_create_response = user2_session.post(booking_create_url,
                                                         data=json.dumps(booking_invalid_create_data)).json()

    print(f'{booking_create_response=}')
    print(f'{booking_invalid_create_response=}')

    # test booking/
    booking_url = host + '/booking/'
    booking_response = user2_session.get(booking_url).json()
    print(f'{booking_response=}')

    # test booking/{booking_id}
    booking_id_url = host + '/booking/' + str(booking_create_response['booking_id'])
    booking_id_response = user2_session.get(booking_id_url).json()
    print(f'{booking_id_response=}')

    # ====================
    # Admin tests
    # ====================

    # test admin/add

    admin_add_url = host + '/admin/add/'
    admin_add_data = {
        "user_id": user2_me_response['user_id']
    }

    unauthorized_admin_add_response = unauthorized_session.post(admin_add_url, data=json.dumps(admin_add_data)).json()
    user1_admin_add_response = user1_session.post(admin_add_url, data=json.dumps(admin_add_data)).json()
    admin_add_response = admin_session.post(admin_add_url, data=json.dumps(admin_add_data)).json()

    print(f'{unauthorized_admin_add_response=}')
    print(f'{user1_admin_add_response=}')
    print(f'{admin_add_response=}')

    # test admin/delete/{admin_id}

    admin_delete_url = host + '/admin/delete/' + str(admin_add_response['admin_id'])

    unauthorized_admin_delete_response = unauthorized_session.delete(admin_delete_url).json()
    admin_delete_response = admin_session.delete(admin_delete_url).json()

    print(f'{unauthorized_admin_delete_response=}')
    print(f'{admin_delete_response=}')

    # test admin/hide_platform/{platform_id}

    admin_hide_platform_url = host + '/admin/hide_platform/' + str(platform_create_response['platform_id'])

    unauthorized_admin_hide_platform_response = unauthorized_session.post(admin_hide_platform_url).json()
    admin_hide_platform_response = admin_session.post(admin_hide_platform_url).json()

    print(f'{unauthorized_admin_hide_platform_response=}')
    print(f'{admin_hide_platform_response=}')

    # test admin/unhide_platform/{platform_id}

    admin_unhide_platform_url = host + '/admin/unhide_platform/' + str(platform_create_response['platform_id'])

    unauthorized_admin_unhide_platform_response = unauthorized_session.post(admin_unhide_platform_url).json()
    admin_unhide_platform_response = admin_session.post(admin_unhide_platform_url).json()

    print(f'{unauthorized_admin_unhide_platform_response=}')
    print(f'{admin_unhide_platform_response=}')


if __name__ == '__main__':
    main()
