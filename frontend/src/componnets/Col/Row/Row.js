import React from 'react';
import s from './Row.module.css'

const Row = ({children}) => {
    return (
        <div className={s.row}>
            {children}
        </div>
    );
};

export default Row;