import {makeAutoObservable} from "mobx";
import {ABOUT_US_ROUTE, CONTACTS_ROUTE, PLATFORMS_ROUTE} from "../consts";

export class NavStore {
    constructor() {
        this._topNav = [
            {to: PLATFORMS_ROUTE, name: 'Креативные площадки'},
            {to: ABOUT_US_ROUTE, name: 'О нас'},
            {to: CONTACTS_ROUTE, name: 'Контакты'},
        ]
        makeAutoObservable(this)
    }

    get topNav() {
        return this._topNav
    }


}