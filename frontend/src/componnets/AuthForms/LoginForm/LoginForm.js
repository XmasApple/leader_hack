import {useContext, useState} from 'react';
import sber from '../../../statics/sber.png';
import mosru from '../../../statics/mos.png';
import gosuslugi from '../../../statics/gosuslugi.png';
import vk from '../../../statics/vk.png';
import InputWithTitle from '../../../componnets/UI/InputWithTitle/InputWithTitle';
import UniversalButton from '../../../componnets/UI/UniversalButton/UniversalButton';
import TextInput from '../../../componnets/UI/TextInput/TextInput';
import s from './LoginForm.module.css';
import {userLogin} from "../../../http/userAPI";
import {Context} from "../../../index";
import {BUSINESS_ROUTE} from "../../../consts";
import {useNavigate} from "react-router-dom";

const LoginForm = () => {

    const {user} = useContext(Context)
    const navigate = useNavigate()

    const [login, setLogin] = useState({ email: '', password: '', life_time: 0});
    const handleChange = (name, value) => {
        setLogin({
            ...login,
            [name]: value,
        });
    };
    
    const onSubmit = () => {
        try {
            navigate(BUSINESS_ROUTE)
        } catch (e) {
            
        }
    }

    return (
        <form onSubmit={onSubmit}>
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
                <UniversalButton  onClick={onSubmit} type={'button'} className={'fill_red'}>
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
        </form>
    );
};

export default LoginForm;
