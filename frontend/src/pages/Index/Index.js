import React from 'react';
import Container from "../../componnets/Col/Container/Container";
import DownArrowSVG from "../../componnets/svg/DownArrowSVG";
import SearchSVG from "../../componnets/svg/SearchSVG";
import WelcomeSection from "../../componnets/WelcomeSection/WelcomeSection";
import PlatformsSection from "../../componnets/PlatformsSection/PlatformsSection";


const Index = () => {

    return (
        <main>
            <WelcomeSection/>
            <PlatformsSection/>
        </main>
    );
};

export default Index;