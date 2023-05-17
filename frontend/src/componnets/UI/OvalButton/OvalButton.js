import React, {useState} from 'react';
import s from './OvalButton.module.css'

const OvalButton = ({children}) => {

    const [active, setActive] = useState(false)

    const changeActive = () => {
        if (active)
            setActive(false)
        else
            setActive(true)
    }

    return (
        <button
            onClick={() => changeActive()}
            className={active ? [s.blue_border, s.active].join(' ') : s.blue_border}>
            {children}
        </button>
    );
};

export default OvalButton;