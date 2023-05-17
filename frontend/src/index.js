import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import {createContext} from "react";
import {UserStore} from "./store/UserStore";
import {PlatformStore} from "./store/PlatformStore";
import {NavStore} from "./store/NavStore";
import {PlatformTypeStore} from "./store/PlatformTypeStore";

export const Context = createContext(null)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Context.Provider value={{
        nav: new NavStore(),
        user: new UserStore(),
        platform: new PlatformStore(),
        platformType: new PlatformTypeStore(),
    }}>
        <App />
    </Context.Provider>
);