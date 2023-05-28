import { useState } from 'react';
import sber from '../../../statics/sber.png';
import mosru from '../../../statics/mos.png';
import gosuslugi from '../../../statics/gosuslugi.png';
import vk from '../../../statics/vk.png';
import InputWithTitle from '../../../componnets/UI/InputWithTitle/InputWithTitle';
import UniversalButton from '../../../componnets/UI/UniversalButton/UniversalButton';
import TextInput from '../../../componnets/UI/TextInput/TextInput';
import s from './LoginForm.module.css';

const LoginForm = () => {
    const [login, setLogin] = useState({ login: '', password: '' });
    const handleChange = (name, value) => {
        setLogin({
            ...login,
            [name]: value,
        });
    };

    return (
        <>
            <div className={s.form_fields}>
                <InputWithTitle title={'Почта'} name={'email'}>
                    <TextInput
                        name={'email'}
                        placeholder={'Введите электронную почту'}
                        onChange={handleChange}
                        type={'email'}
                    />
                </InputWithTitle>
                <InputWithTitle title={'Пароль'} name={'password'}>
                    <TextInput
                        name={'password'}
                        placeholder={'Введите пароль'}
                        onChange={handleChange}
                        type={'password'}
                    />
                </InputWithTitle>
            </div>
            <div className={s.form_button}>
                <UniversalButton type={'button'} className={'fill_red'}>
                    Войти
                </UniversalButton>
            </div>
            <div className={s.form_social}>
                <p>Вход через</p>
                <div className={s.form_social_icons}>
                    <a href="" className={s.form_social_icon}>
                        <img src={mosru} alt="mosru" />
                    </a>
                    <a href="" className={s.form_social_icon}>
                        <img src={gosuslugi} alt="gosuslugi" />
                    </a>
                    <a href="" className={s.form_social_icon}>
                        <img src={vk} alt="vk" />
                    </a>
                    <a href="" className={s.form_social_icon}>
                        <img src={sber} alt="sber" />
                    </a>
                </div>
            </div>
        </>
    );
};

export default LoginForm;
