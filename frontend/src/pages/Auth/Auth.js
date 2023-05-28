import React from 'react';
import Container from '../../componnets/Col/Container/Container';
import LoginForm from '../../componnets/AuthForms/LoginForm/LoginForm';
import login_img from '../../statics/login_img.png';
import register_img from '../../statics/register_img.png';
import bg from '../../statics/auth_bg_img.png';
import s from './Auth.module.css';
import { useLocation } from 'react-router-dom';
import {
    LOGIN_ROUTE,
    REGISTRATION_ROUTE,
    REGISTRATION_COMPANY_ROUTE,
} from '../../consts';
import { Link } from 'react-router-dom';
import RegisterUserForm from '../../componnets/AuthForms/RegisterUserForm/RegisterUserForm';
import RegisterCompanyForm from '../../componnets/AuthForms/RegisterCompanyForm/RegisterCompanyForm';

const Auth = () => {
    const { pathname } = useLocation();
    const auth = { title: '', suggestion: '', form: '', image_src: '' };

    switch (pathname) {
        case LOGIN_ROUTE:
            auth.title = 'Авторизация';
            auth.suggestion = (
                <>
                    Нет аккаунта?{' '}
                    <Link to={REGISTRATION_ROUTE}>Зарегистрируйся</Link>
                </>
            );
            auth.form = <LoginForm />;
            auth.image_src = login_img;
            break;
        case REGISTRATION_ROUTE:
            auth.title = 'Регистрация';
            auth.suggestion = (
                <>
                    Уже есть аккаунт? <Link to={LOGIN_ROUTE}>Войти</Link>
                </>
            );
            auth.form = <RegisterUserForm />;
            auth.image_src = register_img;

            break;
        case REGISTRATION_COMPANY_ROUTE:
            auth.title = 'Регистрация компании';
            auth.suggestion = (
                <>
                    Уже есть аккаунт? <Link to={LOGIN_ROUTE}>Войти</Link>
                </>
            );
            auth.form = <RegisterCompanyForm />;
            auth.image_src = register_img;

            break;
    }

    return (
        <main style={{ backgroundImage: `url(${bg})` }} className={s.auth}>
            <Container>
                <div className={s.auth_wrapper}>
                    <div className={s.form}>
                        <div className={s.form_header}>
                            <h3>{auth.title}</h3>
                            <p>{auth.suggestion}</p>
                        </div>
                        {auth.form}
                    </div>
                    <div className={s.auth_image}>
                        <img src={auth.image_src} alt="auth image" />
                    </div>
                </div>
            </Container>
        </main>
    );
};

export default Auth;
