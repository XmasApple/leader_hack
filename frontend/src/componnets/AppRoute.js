import React, {useContext, useEffect} from 'react';
import {Routes, Route, useLocation} from 'react-router-dom'
import {businessRoutes, publicRoutes} from "../routes";
import {Context} from "../index";
import {observer} from "mobx-react-lite";
import Index from "../pages/Index/Index";

const AppRouter = observer(() => {
    const {user} = useContext(Context)
    const { pathname, hash, key } = useLocation();

    useEffect(() => {
        if (hash === '') {
            window.scrollTo(0, 0);
        }
        else {
            setTimeout(() => {
                const id = hash.replace('#', '');
                const element = document.getElementById(id);
                if (element) {
                    element.scrollIntoView();
                }
            }, 500)
            window.history.pushState('', document.title, window.location.pathname);
        }

    }, [pathname, hash, key]);

    return (
        <Routes>
            {user.isBusiness && businessRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}
            {publicRoutes.map(({path, Component}) =>
                <Route key={path} path={path} element={<Component/>} exact/>
            )}
            <Route path="*" element={<Index/>} exact/>
        </Routes>
    );
});

export default AppRouter;