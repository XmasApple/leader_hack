import React from 'react';
import bg from "../../statics/index_bg_img.jpg";
import s from "./WelcomeSection.module.css";
import Container from "../Col/Container/Container";
import {Link} from "react-router-dom";
import {PLATFORMS_ROUTE} from "../../consts";
import ArrowSVG from "../svg/ArrowSVG";

const WelcomeSection = () => {
    return (
        <section style={{backgroundImage: `url(${bg})`}} className={s.index_top}>
            <Container>
                <div className={s.top_content_centered}>
                    <div className={s.top_content}>
                        <h1>Агрегатор площадок и услуг<br/><b>креативных индустрий</b> Москвы</h1>
                        <Link to={PLATFORMS_ROUTE}>
                            <ArrowSVG/>
                            посмотреть все пространства
                        </Link>
                    </div>
                </div>
            </Container>
        </section>
    );
};

export default WelcomeSection;