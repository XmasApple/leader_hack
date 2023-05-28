import React, {useState} from 'react';
import s from './Business.module.css'
import CreatePlatformSection from "../../componnets/CreatePlatform/CreatePlatformSection/CreatePlatformSection";
import UserCapabilities from "../../componnets/UserCapabilities/UserCapabilities";
import blob from "../../statics/business_bg_img.png"

const Business = () => {

    const [section, setSection] = useState('')
    const [wrapper, setWrapper] = useState(<CreatePlatformSection/>)

    return (
        <main className={s.business}>
            <div className={s.blob}>
                <img src={blob} alt="blob"/>
            </div>
            <div className={s.content}>
                <UserCapabilities wrapper={wrapper} setWrapper={setWrapper}/>
                {wrapper}
            </div>
        </main>
    );
};

export default Business;