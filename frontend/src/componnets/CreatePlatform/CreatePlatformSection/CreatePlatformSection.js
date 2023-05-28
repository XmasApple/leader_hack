import React, {useContext, useEffect, useState} from 'react';
import s from './CreatePlatformSection.module.css'
import Row from "../../Col/Row/Row";
import Col from "../../Col/Col/Col";
import {Context} from "../../../index";
import BusinessNavButton from "../../UI/BusinessNavButton/BusinessNavButton";
import CreatePlatformInfo from "../CreatePlatformInfo/CreatePlatformInfo";
import TextInput from "../../UI/TextInput/TextInput";
import InputWithTitle from "../../UI/InputWithTitle/InputWithTitle";
import ImageInput from "../../UI/ImageInput/ImageImput";
import Textarea from "../../UI/Textarea/Textarea";
import DeletedInput from "../../UI/DeletedInput/DeletedInput";
import PlusSVG from "../../svg/PlusSVG";
import Select from "../../UI/Select/Select";
import imgMap from "../../../statics/business_map_img.jpg"
import SwipeButton from "../../UI/SwipeButton/SwipeButton";
import BusinessSwiperShell from "../../BusinessSwiperShell/BusinessSwiperShell";

const CreatePlatformSection = () => {

    const {nav} = useContext(Context)
    const {eventType} = useContext(Context)

    const [activeId, setActiveId] = useState(1)
    const [platform, setPlatform] = useState({
        name: '',
        cost: '',
        image: null,
        images: [],
        description: '',
        height: '',
        square: '',
        capacity: '',
        prohibitions: [],
        owner_name: '',
        tel: '',
        site: ''
    })
    const [select, setSelect] = useState([])

    const [prohibitions, setProhibitions] = useState([])
    const addProhibitions = () => {
        setProhibitions([... prohibitions, {name: '', number: Date.now()}])
    }
    const removeProhibitions = (number) => {
        setProhibitions(prohibitions.filter(i => i.number !== number))
    }
    const changeProhibitions = (count, value) => {
        setProhibitions(prohibitions.map(i => i.number === count ? {...i, 'name': value} : i))
    }

    const handleChange = (name, value) => {
        setPlatform({
            ...platform,
            [name]: value,
        });
    };

    return (
        <BusinessSwiperShell title={'Добавление новой площадки'}>
            <div className={s.block}>
                <h4>Карточка пространства</h4>
                <Row style={{justifyContent: 'space-between'}}>
                    <Col colWidth={'col_3'}>
                        <nav className={s.business_nav}>
                            {nav.business.map((item) =>
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
                            <CreatePlatformInfo>
                                <div>
                                    <InputWithTitle title={'Название площадки*'} name={'name'}>
                                        <TextInput
                                            type={'text'}
                                            name={'name'}
                                            placeholder={'Название площадки'}
                                            onChange={handleChange}
                                            value={platform.name}
                                        />
                                    </InputWithTitle>
                                    <InputWithTitle title={'Стоимость аренды (от)*'} name={'cost'}>
                                        <TextInput
                                            type={'text'}
                                            name={'cost'}
                                            placeholder={'Стоимость аренды'}
                                            onChange={handleChange}
                                            value={platform.cost}
                                        />
                                    </InputWithTitle>
                                    <InputWithTitle title={'Прикрепить главную фотографию площадки*'} name={'image'}>
                                        <ImageInput
                                            name={'image'}
                                            placeholder={'Выбрать изображение'}
                                            onChange={handleChange}
                                            value={platform.image}
                                        />
                                    </InputWithTitle>
                                    <InputWithTitle title={'Прикрепить фотографии площадки*'} name={'images[]'}>
                                        <ImageInput
                                            name={'images[]'}
                                            placeholder={'Выбрать изображения'}
                                            onChange={handleChange}
                                            value={platform.images}
                                        />
                                    </InputWithTitle>
                                </div>
                                <div className={s.textarea}>
                                    <InputWithTitle title={'Описание площадки*'} name={'description'}>
                                        <Textarea
                                            onChange={handleChange}
                                            name={'description'}
                                            value={platform.description}
                                            placeholder={'Описание плозадки'}/>
                                    </InputWithTitle>
                                </div>
                            </CreatePlatformInfo>
                        }
                        {
                            activeId === 2 &&
                            <CreatePlatformInfo>
                                <div>
                                    <InputWithTitle title={'Тип мероприятия*'} name={'eventType'}>
                                        <Select
                                            list={eventType.types} setSelect={setSelect} select={select}
                                        >
                                            Тип мероприятия
                                        </Select>
                                    </InputWithTitle>
                                    <InputWithTitle title={'Высота потолков (м.)'} name={'height'}>
                                        <TextInput
                                            type={'text'}
                                            name={'height'}
                                            placeholder={'Высота потолков'}
                                            onChange={handleChange}
                                            value={platform.height}
                                        />
                                    </InputWithTitle>
                                    <InputWithTitle title={'Площадь помещения'} name={'square'}>
                                        <TextInput
                                            type={'text'}
                                            name={'square'}
                                            placeholder={'Площадь помещения'}
                                            onChange={handleChange}
                                            value={platform.square}
                                        />
                                    </InputWithTitle>
                                    <InputWithTitle title={'Количество гостей (чел.)'} name={'capacity'}>
                                        <TextInput
                                            type={'text'}
                                            name={'capacity'}
                                            placeholder={'Количество гостей'}
                                            onChange={handleChange}
                                            value={platform.capacity}
                                        />
                                    </InputWithTitle>
                                </div>
                                <InputWithTitle title={'Запреты на площадке'} name={'prohibitions'}>
                                    <div className={s.prohibitions}>
                                        {prohibitions.map((prohibition) =>
                                            <DeletedInput
                                                key={prohibition.count}
                                                name={prohibition.number}
                                                placeholder={'Запрет'}
                                                value={prohibition.name}
                                                edit={changeProhibitions}
                                                remove={removeProhibitions}
                                            />
                                        )}
                                        <button
                                            className={s.prohibitions_add_button}
                                            onClick={addProhibitions}
                                        >
                                            Добавить новый запрет
                                            <PlusSVG/>
                                        </button>
                                    </div>
                                </InputWithTitle>
                            </CreatePlatformInfo>
                        }
                        {
                            activeId === 3 &&
                            <CreatePlatformInfo>
                                <div>
                                    <InputWithTitle title={'Адрес пространства*'} name={'address'}>
                                        <TextInput
                                            type={'text'}
                                            name={'address'}
                                            placeholder={'Найти площадку'}
                                            onChange={handleChange}
                                            value={platform.cost}
                                        />
                                    </InputWithTitle>
                                    <img src={imgMap} alt="map"/>
                                </div>
                            </CreatePlatformInfo>
                        }
                        {
                            activeId === 4 &&
                            <CreatePlatformInfo>
                                <Row>
                                    <Col colWidth={'col_5'}>
                                        <InputWithTitle title={'Имя владельца площадки * '} name={'owner_name'}>
                                            <TextInput
                                                type={'text'}
                                                name={'owner_name'}
                                                placeholder={'Имя владельца '}
                                                onChange={handleChange}
                                                value={platform.owner_name}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Номер телефона для связи с владельцем *'} name={'tel'}>
                                            <TextInput
                                                type={'text'}
                                                name={'tel'}
                                                placeholder={'Номер телефона '}
                                                onChange={handleChange}
                                                value={platform.tel}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Ссылка на сайт *'} name={'site'}>
                                            <TextInput
                                                type={'text'}
                                                name={'site'}
                                                placeholder={'Ссылка на сайт компании'}
                                                onChange={handleChange}
                                                value={platform.site}
                                            />
                                        </InputWithTitle>
                                    </Col>
                                </Row>
                            </CreatePlatformInfo>
                        }
                    </Col>
                </Row>
                <div className={s.nav_buttons}>
                    <SwipeButton
                        className={'prev'}
                        onClick={() => setActiveId(activeId - 1)}
                    >
                        Назад
                    </SwipeButton>
                    <SwipeButton
                        className={'next'}
                        onClick={() => activeId !== 4 && setActiveId(activeId + 1)}
                    >
                        {activeId === 4 ? 'добавить площадку' : 'Далее'}
                    </SwipeButton>
                </div>
            </div>
        </BusinessSwiperShell>
    );
};

export default CreatePlatformSection;