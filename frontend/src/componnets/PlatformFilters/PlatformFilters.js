import React, {useState} from 'react';
import s from './PlatformFilters.module.css'
import OvalButton from "../UI/OvalButton/OvalButton";

const PlatformFilters = ({title, filters}) => {

    const [activeId, setActiveId] = useState(null)

    return (
        <div className={s.block}>
            <h3>{title}</h3>
            <div className={s.block_filters}>
                {filters.map((filter) =>
                    <OvalButton
                        id={filter.id}
                        activeId={activeId}
                        setActiveId={setActiveId}
                        key={filter.id}
                    >
                        {filter.name}
                    </OvalButton>
                )}
            </div>
        </div>
    );
};

export default PlatformFilters;