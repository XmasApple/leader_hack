import React, {useContext, useState} from 'react';
import s from './Select.module.css'
import DownArrowSVG from "../../svg/DownArrowSVG";
import {Context} from "../../../index";

const Select = ({children, value, setSelect, list}) => {

    const [visible, setVisible] = useState(false)

    return (
        <div className={s.select}>
            <div className={s.select_button}>
                <button
                    onFocus={() => setVisible(true)}
                    onBlur={() => setTimeout(() => setVisible(false))}
                    type="button"
                >
                    {children}
                    <DownArrowSVG/>
                </button>
            </div>
            <ul className={visible ? [s.select_options, s.active].join(' ') : s.select_options}>
                {list.map(item =>
                    <li
                        key={item.id}
                    >
                        {item.name}
                    </li>
                )}
            </ul>
        </div>
    );
};

export default Select;