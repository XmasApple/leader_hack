import React, {useRef} from 'react';
import s from "./DeletedInput.module.css";
import TrashSVG from "../../svg/TrashSVG";
import {remove} from "mobx";

const DeletedInput = ({name, placeholder, value, edit, remove}) => {

    const ref = useRef(null);
    const handleInput = (e) => {
        if (ref.current) {
            ref.current.style.height = "auto";
            ref.current.style.height = `${e.target.scrollHeight}px`;
        }
    };

    return (
        <div className={s.block}>
            <textarea
                ref={ref}
                rows={1}
                name={name}
                id={name}
                className={s.textarea}
                value={value}
                onChange={(e) => edit(name, e.target.value) }
                onInput={handleInput}
                placeholder={placeholder}
            />
            <button onClick={() => remove(name)}><TrashSVG/></button>
        </div>
    );
};

export default DeletedInput;