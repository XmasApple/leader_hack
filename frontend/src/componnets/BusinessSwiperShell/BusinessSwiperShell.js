import React from 'react';
import s from "./BusinessSwiperShell.module.css";
import Container from "../Col/Container/Container";

const BusinessSwiperShell = ({children, title}) => {
    return (
        <section className={s.section}>
            <Container>
                <h3>{title}</h3>
            </Container>
            <div className={s.section_bg}>
                <Container>
                    {children}
                </Container>
            </div>
        </section>
    );
};

export default BusinessSwiperShell;