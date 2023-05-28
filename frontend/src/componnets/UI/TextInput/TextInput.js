import React from 'react';
import s from './TextInput.module.css'

const TextInput = ({name, placeholder, value, type, onChange}) => {
    return (
        <input
            name={name}
            id={name}
            className={s.input}
            value={value}
            onChange={(e) => onChange(name, e.target.value) }
            type={type}
            placeholder={placeholder}
        />
    );
};

export default TextInput;