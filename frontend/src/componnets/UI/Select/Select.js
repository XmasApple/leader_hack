import React, {useContext, useEffect, useState} from 'react';
import s from './Select.module.css'
import DownArrowSVG from "../../svg/DownArrowSVG";
import {Context} from "../../../index";

let nextNum = 0;

const Select = ({children, select, setSelect, list}) => {

    const [visible, setVisible] = useState(false)

    const onSelect = (id) => {
        if (select.includes(id)) {
            const updatedSelect = select.filter((item) => item !== id);
            setSelect(updatedSelect);
        } else {
            const updatedSelect = [...select, id];
            setSelect(updatedSelect);
        }
    }

    const activeSelect = () => {
        if (visible)
            setVisible(false)
        else
            setVisible(true)
    }

    return (
        <div className={s.select}>
            <div className={s.select_button}>
                <button
                    onClick={() => activeSelect()}
                    type="button"
                >
                    {children} {select.length ? `(Выбрано ${select.length})` : undefined }
                    <DownArrowSVG/>
                </button>
            </div>
            <ul className={visible ? [s.select_options, s.active].join(' ') : s.select_options}>
                {list.map(item =>
                    <li
                        className={select.includes(item.id) ? s.target : undefined}
                        onClick={() => onSelect(item.id)}
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