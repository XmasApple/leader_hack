import React from 'react';
import s from './Nav.module.css'
import {Link} from "react-router-dom";
import {INDEX_ROUTE, LOGIN_ROUTE} from "../../consts";
import LogoSVG from "../svg/LogoSVG";
import {useContext} from "react";
import {Context} from "../../index";

const Nav = () => {

    const {nav} = useContext(Context)

    return (
        <nav className={s.nav}>
            <ul className={s.nav_menu}>
                <li className={s.menu_left}><Link to={INDEX_ROUTE}><LogoSVG/></Link></li>
                <li className={s.menu_right}>
                    <ul className={s.menu_link}>
                        {nav.nav.map(({to, name}) =>
                            <li key={to}><Link to={to}>{name}</Link></li>
                        )}
                    </ul>
                    <ul className={s.menu_auth}>
                        <li className={s.auth_business}><Link to={LOGIN_ROUTE}>Бизнес-аккаунт</Link></li>
                        <li className={s.auth_login}><Link to={LOGIN_ROUTE}>Войти</Link></li>
                    </ul>
                </li>
            </ul>
        </nav>
    );
};

export default Nav;