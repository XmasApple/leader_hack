import React, {useContext, useEffect} from 'react';
import {BrowserRouter} from "react-router-dom";
import {Context} from "./index";
import {observer} from "mobx-react-lite";
import Header from "./componnets/Header/Header";
import AppRouter from "./componnets/AppRoute";
import Footer from "./componnets/Footer/Footer";
import './globalCSS/fonts.css'
import './globalCSS/root.css'
import './globalCSS/reset.css'

const App = () => {

    return (
        <BrowserRouter>
            <Header/>
            <AppRouter/>
            <Footer/>
        </BrowserRouter>
    );
};

export default App;