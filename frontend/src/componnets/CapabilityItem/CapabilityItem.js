import React from 'react';
import s from './CapabilityItem.module.css'

const CapabilityItem = ({children, title}) => {
    return (
        <div className={s.block}>
            <h4>{title}</h4>
            {children}
        </div>
    );
};

export default CapabilityItem;