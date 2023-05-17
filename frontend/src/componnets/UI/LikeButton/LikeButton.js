import React, {useState} from 'react';
import s from './LikeButton.module.css'
import LikeSVG from "../../svg/LikeSVG";
import ActiveLikeSVG from "../../svg/ActiveLikeSVG";

const LikeButton = () => {

    const [active, setActive] = useState(false)

    const changeActive = () => {
        if (active)
            setActive(false)
        else
            setActive(true)
    }

    return (
        <button
            onClick={() => changeActive()}
            className={s.button}>
            {active ? <ActiveLikeSVG/> : <LikeSVG/>}
        </button>
    );
};

export default LikeButton;