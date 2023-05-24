import React from 'react';
import s from './UniversalButton.module.css'
import cn from "classnames";

const UniversalButton = ({children, className, onClick}) => {
    return (
        <button onClick={onClick} className={cn({ [s[`${className}`]]: className })}>
            {children}
        </button>
    );
};

export default UniversalButton;