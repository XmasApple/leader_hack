import React from 'react';
import s from './ImageInput.module.css'
import AddImgSVG from "../../svg/AddImgSVG";

const ImageInput = ({name, value, placeholder, onChange}) => {
    return (
        <label className={s.input_file}>
            <span className={s.input_file_text}>{placeholder}</span>
            <input
                name={name}
                id={name}
                value={value}
                onChange={(e) => onChange(name, e.target.value) }
                type="file"
                placeholder={placeholder}
                multiple
            />
            <span className={s.input_file_button}><AddImgSVG/></span>
        </label>
    );
};

export default ImageInput;