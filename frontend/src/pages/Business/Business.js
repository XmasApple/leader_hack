import React, {useState} from 'react';
import s from './Business.module.css'
import Container from "../../componnets/Col/Container/Container";
import Row from "../../componnets/Col/Row/Row";
import Col from "../../componnets/Col/Col/Col";
import CreatePlatformSection from "../../componnets/CreatePlatform/CreatePlatformSection/CreatePlatformSection";

const Business = () => {

    const [state, setState] = useState('')

    return (
        <main className={s.business}>
          <CreatePlatformSection/>
        </main>
    );
};

export default Business;