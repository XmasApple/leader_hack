import React from 'react';
import s from './Row.module.css'

const Row = ({children, style}) => {
    return (
        <div style={style} className={s.row}>
            {children}
        </div>
    );
};

export default Row;