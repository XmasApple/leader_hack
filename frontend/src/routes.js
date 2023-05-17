import {
    ABOUT_US_ROUTE,
    BUSINESS_ROUTE,
    CONTACTS_ROUTE,
    INDEX_ROUTE,
    LOGIN_ROUTE,
    REGISTRATION_ROUTE
} from "./consts";
import Business from "./pages/Business/Business";
import Index from "./pages/Index/Index";
import Auth from "./pages/Auth/Auth";
import Platforms from "./pages/Platforms/Platforms";
import AboutUs from "./pages/AboutUs/AboutUs";
import Contacts from "./pages/Contacts/Contacts";


export const authRoutes = []

export const businessRoutes = [
    {
        path: BUSINESS_ROUTE,
        Component: Business
    },
]

export const publicRoutes = [
    {
        path: INDEX_ROUTE,
        Component: Index
    },
    {
        path: LOGIN_ROUTE,
        Component: Auth
    },
    {
        path: REGISTRATION_ROUTE,
        Component: Auth
    },
    {
        path: Platforms + '/:id',
        Component: Platforms
    },
    {
        path: ABOUT_US_ROUTE,
        Component: AboutUs
    },
    {
        path: CONTACTS_ROUTE,
        Component: Contacts
    },
]