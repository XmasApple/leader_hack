import React, {useContext, useEffect, useState} from 'react';
import s from './UserCapabilities.module.css'
import {observer} from "mobx-react-lite";
import {Context} from "../../index";
import CapabilityItem from "../CapabilityItem/CapabilityItem";
import Container from "../Col/Container/Container";
import Row from "../Col/Row/Row";
import Col from "../Col/Col/Col";
import UniversalButton from "../UI/UniversalButton/UniversalButton";
import DownArrowSVG from "../svg/DownArrowSVG";
import CreatePlatformSection from "../CreatePlatform/CreatePlatformSection/CreatePlatformSection";
import BusinessPlatformList from "../BusinessPlatformList/BusinessPlatformList";
import AddingEmployee from "../AddingEmployee/AddingEmployee";
import EditBusinessInfo from "../EditBusinessInfo/EditBusinessInfo";

const UserCapabilities = observer(({wrapper, setWrapper}) => {

    const {user} = useContext(Context)

    const [visible, setVisible] = useState(true)

    useEffect(() => {
        console.log(wrapper)
    }, [])

    return (
        <section className={s.section}>
            <Container>
                <h2 onClick={() => visible ? setVisible(false) : setVisible(true)}
                    className={!visible ? [s.title, s.active].join(' ') : s.title}
                >Ваши возможности
                    <DownArrowSVG/>
                </h2>
                {visible &&
                    <div className={s.menu}>
                        <Row>
                            <Col colWidth={'col_4'}>
                                <CapabilityItem title={'О компании'}>
                                    <div className={s.capability_content}>
                                        <h4>«{user.user.company}»</h4>
                                        <span>(юридическое название)<br/>{user.user.LLC}</span>
                                        <UniversalButton
                                            onClick={() => setWrapper(<EditBusinessInfo/>)}
                                            className={wrapper.type.name === 'EditBusinessInfo' ? 'fill_red' : 'border_gray'}
                                            type={'button'}
                                        >Изменить информацию
                                        </UniversalButton>
                                    </div>
                                </CapabilityItem>
                            </Col>
                            <Col colWidth={'col_4'}>
                                <CapabilityItem title={'Креативные площадки'}>
                                    <div className={s.capability_content}>
                                        <UniversalButton
                                            className={wrapper.type.name === 'BusinessPlatformList' ? 'fill_red' : 'border_gray'}
                                            type={'button'}
                                            onClick={() => setWrapper(<BusinessPlatformList/>)}
                                        >ПОСМОТРЕТЬ ВСЕ ПЛОЩАДКИ
                                        </UniversalButton>
                                        <UniversalButton
                                            className={wrapper.type.name === 'CreatePlatformSection' ? 'fill_red' : 'border_gray'}
                                            type={'button'}
                                            onClick={() => setWrapper(<CreatePlatformSection/>)}
                                        >ДОБАВИТЬ НОВУЮ ПЛОЩАДКУ
                                        </UniversalButton>
                                        <UniversalButton
                                            className={'border_gray'}
                                            type={'button'}
                                        >ЗАПРОСЫ НА ПОДТВЕРЖДЕНИЕ
                                        </UniversalButton>
                                    </div>
                                </CapabilityItem>
                            </Col>
                            <Col colWidth={'col_4'}>
                                <CapabilityItem title={'Креативные площадки'}>
                                    <div className={s.capability_content}>
                                        <UniversalButton
                                            className={'border_gray'}
                                            type={'button'}
                                        >ПОСМОТРЕТЬ ВСЕХ СОТРУДНИКОВ
                                        </UniversalButton>
                                        <UniversalButton
                                            className={wrapper.type.name === 'AddingEmployee' ? 'fill_red' : 'border_gray'}
                                            type={'button'}
                                            onClick={() => setWrapper(<AddingEmployee/>)}
                                        >ДОБАВИТЬ НОВОГО СОТРУДНИКА
                                        </UniversalButton>
                                    </div>
                                </CapabilityItem>
                            </Col>
                        </Row>
                    </div>
                }
            </Container>
        </section>
    );
});

export default UserCapabilities;