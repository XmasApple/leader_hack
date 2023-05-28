import { useState } from 'react';
import InputWithTitle from '../../UI/InputWithTitle/InputWithTitle';
import TextArea from '../../UI/Textarea/Textarea';
import UniversalButton from '../../UI/UniversalButton/UniversalButton';
import TextInput from '../../UI/TextInput/TextInput';
import s from './RegisterCompanyForm.module.css';

const RegisterCompanyForm = () => {
    const [login, setLogin] = useState({
        phys_name: '',
        legal_name: '',
        description: '',
        tin: '',
        job: '',
        phone: '',
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
                <InputWithTitle title={'Название компании'} name={'phys_name'}>
                    <TextInput
                        name={'phys_name'}
                        placeholder={'Введите название компании'}
                        onChange={handleChange}
                        type={'text'}
                    />
                </InputWithTitle>
                <InputWithTitle
                    title={'Юридическое название компании'}
                    name={'legal_name'}
                >
                    <TextInput
                        name={'legal_name'}
                        placeholder={'Введите юридическое название компании'}
                        onChange={handleChange}
                        type={'text'}
                    />
                </InputWithTitle>
                <InputWithTitle
                    title={'Описание компании'}
                    name={'description'}
                >
                    <TextArea
                        name={'description'}
                        onChange={handleChange}
                        placeholder={'Напишите описание компании'}
                    />
                </InputWithTitle>
                <InputWithTitle title={'ИНН организации'} name={'tin'}>
                    <TextInput
                        name={'tin'}
                        placeholder={'Введите ИНН организации'}
                        onChange={handleChange}
                        type={'text'}
                    />
                </InputWithTitle>
                <InputWithTitle title={'Должность'} name={'job'}>
                    <TextInput
                        name={'job'}
                        placeholder={'Введите Вашу должность в компании'}
                        onChange={handleChange}
                        type={'text'}
                    />
                </InputWithTitle>
                <InputWithTitle title={'Номер телефона'} name={'phone'}>
                    <TextInput
                        name={'phone'}
                        placeholder={'Введите номер телефона для связи'}
                        onChange={handleChange}
                        type={'text'}
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

export default RegisterCompanyForm;
