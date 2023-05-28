import {
    ABOUT_US_ROUTE,
    BUSINESS_ROUTE,
    CONTACTS_ROUTE,
    INDEX_ROUTE,
    LOGIN_ROUTE, PLATFORMS_ROUTE, REGISTRATION_COMPANY_ROUTE,
    REGISTRATION_ROUTE, USER_PROFILE
} from "./consts";
import Business from "./pages/Business/Business";
import Index from "./pages/Index/Index";
import Auth from "./pages/Auth/Auth";
import Platforms from "./pages/Platforms/Platforms";
import AboutUs from "./pages/AboutUs/AboutUs";
import Contacts from "./pages/Contacts/Contacts";
import UserProfile from "./pages/UserProfile/UserProfile";


export const authRoutes = []

export const businessRoutes = [
    {
        path: BUSINESS_ROUTE,
        Component: Business
    },
    {
        path: BUSINESS_ROUTE + '/:id',
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
        path: REGISTRATION_COMPANY_ROUTE,
        Component: Auth,
    },
    {
        path: USER_PROFILE,
        Component: UserProfile,
    },
    {
        path: PLATFORMS_ROUTE,
        Component: Platforms
    },
    {
        path: PLATFORMS_ROUTE + '/:id',
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