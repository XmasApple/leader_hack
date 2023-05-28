import React from 'react';
import s from './EditBusinessInfo.module.css'
import BusinessSwiperShell from "../BusinessSwiperShell/BusinessSwiperShell";
import Row from "../Col/Row/Row";
import Col from "../Col/Col/Col";
import BusinessNavButton from "../UI/BusinessNavButton/BusinessNavButton";
import {useContext, useState} from "react";
import {Context} from "../../index";
import CreatePlatformInfo from "../CreatePlatform/CreatePlatformInfo/CreatePlatformInfo";
import InputWithTitle from "../UI/InputWithTitle/InputWithTitle";
import TextInput from "../UI/TextInput/TextInput";
import ImageInput from "../UI/ImageInput/ImageImput";
import Textarea from "../UI/Textarea/Textarea";
import UniversalButton from "../UI/UniversalButton/UniversalButton";

const EditBusinessInfo = () => {

    const {nav} = useContext(Context)
    const [activeId, setActiveId] = useState(1)

    const [baseInfo, setBaseInfo] = useState({
        company_name: '',
        legal_company_name: '',
        LLC: '',
        company_description: ''
    })
    const baseInfoHandleChange = (name, value) => {
        setBaseInfo({
            ...baseInfo,
            [name]: value,
        });
    };
    const baseInfoSubmit = () => {
        try {

        } catch (e) {

        }
    }

    const [aboutOwner, setAboutOwner] = useState({
        position: '',
        tel: '',
        owner_name: '',
        site: ''
    })
    const aboutOwnerHandleChange = (name, value) => {
        setAboutOwner({
            ...aboutOwner,
            [name]: value,
        });
    };
    const aboutOwnerSubmit = () => {
        try {

        } catch (e) {

        }
    }

    return (
        <BusinessSwiperShell title={'Изменение информации о компании'}>
            <div className={s.block}>
                <h4>Карточка компании</h4>
                <Row style={{justifyContent: 'space-between'}}>
                    <Col colWidth={'col_3'}>
                        <nav className={s.business_nav}>
                            {nav.info.map((item) =>
                                <BusinessNavButton
                                    key={item.id}
                                    id={item.id}
                                    activeId={activeId}
                                    onClick={() => setActiveId(item.id)}
                                >
                                    {item.name}
                                </BusinessNavButton>
                            )}
                        </nav>
                        <p className={s.important}>* - обязательные поля для заполнения </p>
                    </Col>
                    <Col colWidth={'col_8'}>
                        {
                            activeId === 1 &&
                            <form onSubmit={baseInfoSubmit}>
                                <CreatePlatformInfo>
                                    <div>
                                        <InputWithTitle title={'Название компании'} name={'company_name'}>
                                            <TextInput
                                                type={'text'}
                                                name={'company_name'}
                                                placeholder={'Введите название компании'}
                                                 onChange={baseInfoHandleChange}
                                                 value={baseInfo.company_name}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Юридическое название компании'} name={'legal_company_name'}>
                                            <TextInput
                                                type={'text'}
                                                name={'legal_company_name'}
                                                placeholder={'Введите юридическое название компании'}
                                                       onChange={baseInfoHandleChange}
                                                       value={baseInfo.legal_company_name}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'ИНН организации'} name={'LLC'}>
                                            <TextInput
                                                type={'text'}
                                                name={'LLC'}
                                                placeholder={'Введите ИНН организации'}
                                                 onChange={baseInfoHandleChange}
                                                 value={baseInfo.LLC}
                                            />
                                        </InputWithTitle>
                                    </div>
                                    <div className={s.textarea}>
                                        <InputWithTitle title={'Описание компании'} name={'company_description'}>
                                            <Textarea
                                                 onChange={baseInfoHandleChange}
                                                name={'company_description'}
                                                  value={baseInfo.company_description}
                                                placeholder={'Напишите описание компании'}/>
                                        </InputWithTitle>
                                    </div>
                                </CreatePlatformInfo>
                                <div className={s.submit_button}>
                                    <div>
                                        <UniversalButton
                                            onClick={baseInfoSubmit}
                                            type={'submit'}
                                            className={'fill_red'}
                                        >
                                            Изменить
                                        </UniversalButton>
                                    </div>
                                </div>
                            </form>
                        }
                        {
                            activeId === 2 &&
                            <form onSubmit={aboutOwnerSubmit}>
                                <CreatePlatformInfo>
                                    <div>
                                        <InputWithTitle title={'Должность'} name={'position'}>
                                            <TextInput
                                                type={'text'}
                                                name={'position'}
                                                placeholder={'Введите Вашу должность в компании'}
                                                onChange={baseInfoHandleChange}
                                                value={aboutOwner.position}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Номер телефона'} name={'tel'}>
                                            <TextInput
                                                type={'text'}
                                                name={'tel'}
                                                placeholder={'Введите номер телефона для связи'}
                                                onChange={baseInfoHandleChange}
                                                value={aboutOwner.tel}
                                            />
                                        </InputWithTitle>
                                    </div>
                                    <div className={s.textarea}>
                                        <InputWithTitle title={'Имя владельца площадки * '} name={'owner_name'}>
                                            <TextInput
                                                type={'text'}
                                                name={'owner_name'}
                                                placeholder={'Имя владельца '}
                                                onChange={baseInfoHandleChange}
                                                value={aboutOwner.owner_name}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Ссылка на сайт *'} name={'site'}>
                                            <TextInput
                                                type={'text'}
                                                name={'site'}
                                                placeholder={'Ссылка на сайт компании'}
                                                onChange={baseInfoHandleChange}
                                                value={aboutOwner.site}
                                            />
                                        </InputWithTitle>
                                    </div>
                                </CreatePlatformInfo>
                                <div className={s.submit_button}>
                                    <div>
                                        <UniversalButton
                                            onClick={aboutOwnerSubmit}
                                            type={'submit'}
                                            className={'fill_red'}
                                        >
                                            Изменить
                                        </UniversalButton>
                                    </div>
                                </div>
                            </form>
                        }
                    </Col>
                </Row>
            </div>
        </BusinessSwiperShell>
    );
};

export default EditBusinessInfo;