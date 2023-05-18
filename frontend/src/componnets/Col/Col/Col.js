import React from "react";
import cn from "classnames";
import s from "./Col.module.css";

const Col = ({children, colWidth}) => {

    return (
        <div className={cn({ [s[`${colWidth}`]]: colWidth })}>
            {children}
        </div>
    );
}

export default Col;