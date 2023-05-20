import React from 'react';
import s from './Textarea.module.css'

const Textarea = ({name, value, placeholder, onChange}) => {
    return (
        <textarea
            className={s.textarea}
            name={name}
            id={name}
            value={value}
            onChange={(e) => onChange(name, e.target.value) }
            placeholder={placeholder}
        />
    );
};

export default Textarea;