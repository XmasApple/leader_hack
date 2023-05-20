import React, {useContext, useEffect, useState} from 'react';
import s from './CreatePlatformSection.module.css'
import Container from "../../Col/Container/Container";
import Row from "../../Col/Row/Row";
import Col from "../../Col/Col/Col";
import {Context} from "../../../index";
import BusinessNavButton from "../../UI/BusinessNavButton/BusinessNavButton";
import CreatePlatformInfo from "../CreatePlatformInfo/CreatePlatformInfo";
import TextInput from "../../UI/TextInput/TextInput";
import InputWithTitle from "../../UI/InputWithTitle/InputWithTitle";
import ImageInput from "../../UI/ImageInput/ImageImput";
import Textarea from "../../UI/Textarea/Textarea";
import UniversalButton from "../../UI/UniversalButton/UniversalButton";
import DeletedInput from "../../UI/DeletedInput/DeletedInput";
import deletedInput from "../../UI/DeletedInput/DeletedInput";
import PlusSVG from "../../svg/PlusSVG";
import Select from "../../UI/Select/Select";

const CreatePlatformSection = () => {

    const {nav} = useContext(Context)
    const {eventType} = useContext(Context)

    const [activeId, setActiveId] = useState(1)
    const [platform, setPlatform] = useState({
        name: '',
        cost: '',
        image: null,
        description: '',
        height: '',
        square: '',
        capacity: '',
        prohibitions: [],
    })

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

    const [eventTypes, setEventTypes] = useState([])
    const addType = () => {
        setEventTypes([... eventTypes, {id: null, number: Date.now()}])
    }
    const removeType = (number) => {
        setEventTypes(eventTypes.filter(i => i.number !== number))
    }

    const handleChange = (name, value) => {
        setPlatform({
            ...platform,
            [name]: value,
        });
    };

    return (
        <section className={s.padding}>
            <div className={s.block}>
                <Container>
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
                                                name={'name'}
                                                placeholder={'Название площадки'}
                                                onChange={handleChange}
                                                value={platform.name}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Стоимость аренды (от)*'} name={'cost'}>
                                            <TextInput
                                                name={'cost'}
                                                placeholder={'Стоимость аренды'}
                                                onChange={handleChange}
                                                value={platform.cost}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Прикрепить фотографии площадки*'} name={'images'}>
                                            <ImageInput
                                                name={'images'}
                                                placeholder={'Выбрать изображения'}
                                                onChange={handleChange}
                                                value={platform.image}
                                            />
                                        </InputWithTitle>
                                    </div>
                                    <div>
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
                                                list={eventType.types} /*setSelect={} value={}*/
                                            >
                                                Тип мероприятия
                                            </Select>
                                        </InputWithTitle>
                                        <InputWithTitle title={'Высота потолков (м.)'} name={'height'}>
                                            <TextInput
                                                name={'height'}
                                                placeholder={'Высота потолков'}
                                                onChange={handleChange}
                                                value={platform.height}
                                            />
                                        </InputWithTitle>
                                        <InputWithTitle title={'Площадь помещения'} name={'square'}>
                                            <TextInput
                                                name={'square'}
                                                placeholder={'Площадь помещения'}
                                                onChange={handleChange}
                                                value={platform.square}
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
                        </Col>
                    </Row>
                    <div className={s.nav_buttons}>
                        <UniversalButton
                            className={'prev'}
                            onClick={() => setActiveId(activeId - 1)}
                        >
                            Назад
                        </UniversalButton>
                        <UniversalButton
                            className={'next'}
                            onClick={() => setActiveId(activeId + 1)}
                        >
                            Далее
                        </UniversalButton>
                    </div>
                </Container>
            </div>

        </section>
    );
};

export default CreatePlatformSection;