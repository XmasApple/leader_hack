import React from 'react';
import s from './UniversalButton.module.css';
import cn from "classnames";

const UniversalButton = ({ onClick, type, children, className }) => {
    return (
        <button type={type} onClick={onClick} className={cn({ [s[`${className}`]]: className })}>
            {children}
        </button>
    );
};

export default UniversalButton;
