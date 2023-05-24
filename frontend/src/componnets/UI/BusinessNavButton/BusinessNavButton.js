import React from 'react';
import s from './BusinessNavButton.module.css'

const BusinessNavButton = ({activeId, id, onClick, children}) => {
    return (
        <button
            className={activeId === id ? [s.link, s.active].join(' ') : s.link}
            onClick={onClick}
        >
            {children}
        </button>
    );
};

export default BusinessNavButton;