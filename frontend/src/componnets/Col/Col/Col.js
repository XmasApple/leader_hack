import React from "react";
import cn from "classnames";
import s from "./Col.module.css";

const Col = ({children, colWidth}) => {

    return (
        <dib className={cn({ [s[`${colWidth}`]]: colWidth })}>
            {children}
        </dib>
    );
}

export default Col;