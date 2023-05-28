import { useState } from 'react';
import s from './UserCard.module.css';
import Container from '../Col/Container/Container';
import Row from '../Col/Row/Row';
import Col from '../Col/Col/Col';
import InputWithTitle from '../UI/InputWithTitle/InputWithTitle';
import UserCalendarCard from '../../componnets/UserCalendarCard/UserCalendarCard';
import UniversalButton from '../../componnets/UI/UniversalButton/UniversalButton';
import ReferenceSVG from '../../componnets/svg/ReferenceSVG';
import TextInput from '../UI/TextInput/TextInput';

const calendarCardsData = [
    {
        id: 0,
        date: '18.05.2023',
        title: 'Московский международный Дом музыки',
    },
    {
        id: 1,
        date: '18.05.2023',
        title: 'Cube.Moscow',
    },
    {
        id: 2,
        date: '18.05.2023',
        title: 'тут может быть размещен длинный текст, позволяющий вместить в себя около 100 символов',
    },
    {
        id: 3,
        date: '18.05.2023',
        title: 'Cube.Moscow',
    },
    {
        id: 4,
        date: '18.05.2023',
        title: 'Cube.Moscow',
    },
    {
        id: 5,
        date: '18.05.2023',
        title: 'Московский международный Дом музыки',
    },

    {
        id: 6,
        date: '18.05.2023',
        title: 'Cube.Moscow',
    },
    {
        id: 7,
        date: '18.05.2023',
        title: 'Cube.Moscow',
    },
];

const UserCard = () => {
    const [form, setForm] = useState({ full_name: '', email: '', phone: '' });
    const handleChange = (name, value) => {
        setForm({
            ...form,
            [name]: value,
        });
    };

    return (
        <div className={s.user_card}>
            <Container>
                <Row style={{ justifyContent: 'space-between' }}>
                    <Col colWidth={'col_3'}>
                        <div className={s.user_card_form}>
                            <h4>Карточка пользователя</h4>
                            <InputWithTitle title={'ФИО *'} name={'full_name'}>
                                <TextInput
                                    name={'full_name'}
                                    placeholder={'Введите ФИО'}
                                    onChange={handleChange}
                                    type={'text'}
                                />
                            </InputWithTitle>
                            <InputWithTitle title={'Почта *'} name={'email'}>
                                <TextInput
                                    name={'email'}
                                    placeholder={'Введите электронную почту'}
                                    onChange={handleChange}
                                    type={'email'}
                                />
                            </InputWithTitle>
                            <InputWithTitle
                                title={'Номер телефона *'}
                                name={'phone'}
                            >
                                <TextInput
                                    name={'phone'}
                                    placeholder={'Введите номер телефона'}
                                    onChange={handleChange}
                                    type={'text'}
                                />
                            </InputWithTitle>
                            <p className={s.user_card_form_caption}>
                                * - обязательные поля для заполнения{' '}
                            </p>
                            <UniversalButton className={'fill_red'}>
                                Изменить данные
                            </UniversalButton>
                        </div>
                    </Col>
                    <Col colWidth={'col_8'}>
                        <div className={s.user_calendar}>
                            <div className={s.user_calendar_header}>
                                <h4>Календарь бронированных площадок</h4>
                                <p>
                                    Рейтинг пользователя 4.7 <ReferenceSVG />
                                    <span>
                                        На основании оценок арендодателей
                                    </span>
                                </p>
                            </div>
                            <div className={s.user_calendar_cards}>
                                {calendarCardsData.map((card) => (
                                    <div
                                        key={card.id}
                                        className={s.user_calendar_card}
                                    >
                                        <UserCalendarCard
                                            date={card.date}
                                            title={card.title}
                                        />
                                    </div>
                                ))}
                            </div>
                        </div>
                    </Col>
                </Row>
            </Container>
        </div>
    );
};

export default UserCard;
