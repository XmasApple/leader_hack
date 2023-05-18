import React, {useState} from 'react';
import s from './OvalButton.module.css'

const OvalButton = ({children, id, activeId, setActiveId}) => {

    return (
        <button
            onClick={() => setActiveId(id)}
            className={activeId === id  ? [s.blue_border, s.active].join(' ') : s.blue_border}>
            {children}
        </button>
    );
};

export default OvalButton;