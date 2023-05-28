import React, {useEffect} from 'react';
import s from './Nav.module.css'
import {Link, useLocation, useNavigate} from "react-router-dom";
import {BUSINESS_ROUTE, INDEX_ROUTE, LOGIN_ROUTE, REGISTRATION_COMPANY_ROUTE, REGISTRATION_ROUTE} from "../../consts";
import LogoSVG from "../svg/LogoSVG";
import {useContext} from "react";
import {Context} from "../../index";
import AvatarSVG from "../svg/AvatarSVG";

const Nav = () => {

    const {pathname} = useLocation()

    const {nav} = useContext(Context)
    const {user} = useContext(Context)

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
                    {pathname === BUSINESS_ROUTE ?
                        <ul className={s.is_business_auth}>
                            <li>
                                <Link to={LOGIN_ROUTE}>
                                    <AvatarSVG />
                                </Link>
                            </li>
                        </ul>
                        : (
                            !(pathname === LOGIN_ROUTE || pathname === REGISTRATION_ROUTE ||
                                pathname === REGISTRATION_COMPANY_ROUTE) &&
                                <ul className={s.menu_auth}>
                                    <li className={s.auth_business}>
                                        <Link to={REGISTRATION_COMPANY_ROUTE}>Бизнес-аккаунт</Link>
                                    </li>
                                    <li className={s.auth_login}>
                                        <Link to={LOGIN_ROUTE}>Войти</Link>
                                    </li>
                                </ul>
                            )}
                </li>
            </ul>
        </nav>
    );
};

export default Nav;