import { useState } from 'react';
import InputWithTitle from '../../UI/InputWithTitle/InputWithTitle';
import UniversalButton from '../../UI/UniversalButton/UniversalButton';
import TextInput from '../../UI/TextInput/TextInput';
import s from './RegisterUserForm.module.css';

const RegisterUserForm = () => {
    const [login, setLogin] = useState({
        full_name: '',
        email: '',
        password: '',
    });
    const handleChange = (name, value) => {
        setLogin({
            ...login,
            [name]: value,
        });
    };

    return (
        <>
            <div className={s.form_fields}>
                <InputWithTitle title={'ФИО'} name={'full_name'}>
                    <TextInput
                        name={'full_name'}
                        placeholder={'Введите ФИО'}
                        onChange={handleChange}
                        type={'text'}
                    />
                </InputWithTitle>
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
                    Зарегистрироваться
                </UniversalButton>
            </div>
        </>
    );
};

export default RegisterUserForm;
