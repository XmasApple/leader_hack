import React from 'react';
import s from './RangeInput.module.css'

const RangeInput = ({title, min, max}) => {
    return (
        <div className={s.block}>
            <h4>{title}</h4>
            <div>
                <input type="range" className={s.block_input}/>
                <span>{min}</span>
                <span>{max}</span>
            </div>
        </div>
    );
};

export default RangeInput;