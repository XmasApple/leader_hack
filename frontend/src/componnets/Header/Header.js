import React, {useContext} from 'react';
import s from './Header.module.css'
import Nav from "../Nav/Nav";
import Container from "../Col/Container/Container";

const Header = () => {
    return (
        <header className={s.content}>
            <Container>
                <Nav/>
            </Container>
        </header>
    );
};

export default Header;