import React, {useContext} from 'react';
import s from './Footer.module.css'
import Container from "../Col/Container/Container";
import LogoSVG from "../svg/LogoSVG";
import {Link, useLocation} from "react-router-dom";
import {Context} from "../../index";
import img from './../../statics/footer_bg_img.png'
import {LOGIN_ROUTE, REGISTRATION_COMPANY_ROUTE, REGISTRATION_ROUTE} from "../../consts";

const Footer = () => {

    const {nav} = useContext(Context)
    const {pathname} = useLocation()

    return (
        !(pathname === LOGIN_ROUTE || pathname === REGISTRATION_ROUTE || pathname === REGISTRATION_COMPANY_ROUTE) &&
        <footer
            style={{backgroundImage: `url(${img})`}}
            className={s.footer}>
            <Container>
                <div className={s.footer_block}>
                    <div className={s.footer_logo}>
                        <LogoSVG/>
                    </div>
                    <div className={s.footer_info}>
                        <div className={s.info_nav}>
                            <h4>навигация</h4>
                            <ul>
                                {nav.nav.map(({to, name}) =>
                                    <li key={to}><Link to={to}>{name}</Link></li>
                                )}
                            </ul>
                        </div>
                        <div className={s.info_documents}>
                            <h4>документы</h4>
                            <ul>
                                <li><Link>Политика конфиденциальности</Link></li>
                                <li><Link>Пользовательское соглашение</Link></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className={s.footer_c}>
                    <p>Creative Compass ⓒ 2023</p>
                    <a href="mailto:creative.compass@mail.ru">creative.compass@mail.ru</a>
                </div>
            </Container>
        </footer>
    );
};

export default Footer;