import React from 'react';
import s from './InputWithTitle.module.css'
import TextInput from "../TextInput/TextInput";

const InputWithTitle = ({name, title, children}) => {
    return (
        <div className={s.block}>
            <label className={s.block_label} htmlFor={name}>{title}</label>
            {children}
        </div>
    );
};

export default InputWithTitle;