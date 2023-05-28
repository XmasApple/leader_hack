import React, {useContext, useState} from 'react';
import { useNavigate } from 'react-router-dom';
import s from './PlatformsSection.module.css'
import Container from "../Col/Container/Container";
import DownArrowSVG from "../svg/DownArrowSVG";
import SearchSVG from "../svg/SearchSVG";
import {observer} from "mobx-react-lite";
import {Context} from "../../index";
import PlatformCard from "../PlatformCard/PlatformCard";
import Row from "../Col/Row/Row";
import Col from "../Col/Col/Col";
import CloseSVG from "../svg/CloseSVG";
import map from '../../statics/map.jpg'
import PlatformFilters from "../PlatformFilters/PlatformFilters";
import RangeInput from "../UI/RangeInput/RangeInput";
import img from './../../statics/platforms_bg_img.png'
import {PLATFORMS_ROUTE} from "../../consts";
import Calendar from "../Calendar/Calendar";


const PlatformsSection = observer(() => {

    const {platform} = useContext(Context)
    const {platformType} = useContext(Context)
    const {eventType} = useContext(Context)
    const {capacity} = useContext(Context)
    const {filter} = useContext(Context)

    const navigate = useNavigate()

    const [selectActive, setSelectActive] = useState(false)
    const [activeId, setActiveId] = useState(null)
    const [mapActive, setMapActive] = useState(false)

    const search = async (e) => {
        try {
            e.preventDefault()
        } catch (e) {

        }
    }

    const setFilter = async (platformTypeId) => {
        try {
            setActiveId(parseInt(platformTypeId))
            setTimeout(() => setSelectActive(false), 200)
        } catch (e) {

        }
    }

    const changeMapActive = () => {
        if (mapActive)
            setMapActive(false)
        else
            setMapActive(true)
    }

    return (
        <section className={s.platforms}>
            <Container>
                <div className={s.platforms_view_settings}>
                    <div className={s.platforms_controllers}>
                        <div
                            onClick={() => setSelectActive(true)}
                            className={s.platforms_filter}>
                            <span>Креативные</span>
                            <div className={s.filter}>
                                <h2>Площадки</h2>
                                <DownArrowSVG/>
                            </div>
                        </div>
                        <div className={s.platforms_search}>
                            <button
                                onClick={() => changeMapActive()}
                                className={s.search_map_button}
                            >
                                {mapActive ? 'Закрыть карту' : 'Открыть карту'}
                            </button>
                            <form className={s.search_form} onSubmit={search}>
                                <input placeholder="Поиск площадки или услуги...  " type="search"/>
                                <button
                                    onClick={search}
                                    type="submit"
                                >
                                    <SearchSVG/>
                                </button>
                            </form>
                        </div>
                    </div>
                    {
                        selectActive &&
                        <div className={s.platforms_select}>
                            <span
                                onClick={() => setSelectActive(false)}
                            >
                                <CloseSVG/>
                            </span>
                            <div>
                                <button
                                    onClick={() => setFilter(0)}
                                    className={!activeId ?
                                        [s.option_button, s.active].join(' ') :
                                        s.option_button}
                                >
                                    Все
                                </button>
                                {platformType.types.map((type) =>
                                    <button
                                        key={type.id}
                                        onClick={() => setFilter(type.id)}
                                        className={activeId === type.id ?
                                            [s.option_button, s.active].join(' ') :
                                            s.option_button}
                                    >
                                        {type.name}
                                    </button>
                                )}
                            </div>
                        </div>
                    }
                </div>
                <div
                    className={s.platforms_list}>
                    <Row>
                        <Col
                            colWidth={'col_9'}>
                            <div
                                style={{backgroundImage: `url(${img})`}}
                                className={s.list_bg}>
                                <Row>
                                    {
                                        mapActive &&
                                        <Col colWidth={'col_12'}>
                                            <img className={s.platforms_map} src={map} alt="Карта"/>
                                        </Col>
                                    }
                                    {platform.platforms.map((platform) =>
                                        <Col key={platform.platform_id} colWidth={'col_4'}>
                                            <PlatformCard
                                                onClick={() => navigate(PLATFORMS_ROUTE + '/' + platform.id)}
                                                platform={platform}/>
                                        </Col>
                                    )}
                                </Row>
                            </div>

                        </Col>
                        <Col colWidth={'col_3'}>
                            <Calendar/>
                            <PlatformFilters
                                title={'Сортировка'}
                                filters={filter.filters}
                            />
                            <PlatformFilters
                                title={'Тип мероприятия'}
                                filters={eventType.types}
                            />
                            <PlatformFilters
                                title={'Количество гостей'}
                                filters={capacity.capacity}
                            />
                            <RangeInput
                                title={'Цена'}
                                min={'0'}
                                max={'500 000 р.'}
                            />
                            <RangeInput
                                title={'Площадь помещения'}
                                min={'0'}
                                max={'max?'}
                            />
                            <RangeInput
                                title={'Высота потолков'}
                                min={'0'}
                                max={'max?'}
                            />
                        </Col>
                    </Row>
                </div>
            </Container>
        </section>
    );
});

export default PlatformsSection;