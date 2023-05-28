import React, {useState} from 'react';
import s from './BusinessPlatformItem.module.css'
import TrashSVG from "../svg/TrashSVG";
import DotsSVG from "../svg/DotsSVG";
import PenSVG from "../svg/PenSVG";

const BusinessPlatformItem = ({children}) => {
    const [active, setActive] = useState(false);

    return (
        <div className={s.block}>
            <div className={s.content}>
                <h4>{children}</h4>
                <div onClick={() => active ? setActive(false) : setActive(true)}
                     className={s.dot_menu}>
                    <DotsSVG/>
                </div>
            </div>
            {active &&
                <div className={s.edit_menu}>
                    <button>
                        <PenSVG/>
                        <span>Редактировать площадку</span>
                    </button>
                    <button>
                        <TrashSVG/>
                        <span>Удалить площадку</span>
                    </button>
                </div>
            }
        </div>
    );
};

export default BusinessPlatformItem;