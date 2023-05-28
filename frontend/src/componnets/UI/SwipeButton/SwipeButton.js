import React from 'react';
import s from './SwipeButton.module.css'
import cn from "classnames";

const SwipeButton = ({children, className, onClick}) => {
    return (
        <button onClick={onClick} className={cn({ [s[`${className}`]]: className })}>
            {children}
        </button>
    );
};

export default SwipeButton;