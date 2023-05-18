import React, {useContext} from 'react';
import s from './Footer.module.css'
import Container from "../Col/Container/Container";
import LogoSVG from "../svg/LogoSVG";
import {Link} from "react-router-dom";
import {Context} from "../../index";
import img from './../../statics/footer_bg_img.png'

const Footer = () => {

    const {nav} = useContext(Context)

    return (
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
                            <h3>навигация</h3>
                            <ul>
                                {nav.nav.map(({to, name}) =>
                                    <li key={to}><Link to={to}>{name}</Link></li>
                                )}
                            </ul>
                        </div>
                        <div className={s.info_documents}>
                            <h3>документы</h3>
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