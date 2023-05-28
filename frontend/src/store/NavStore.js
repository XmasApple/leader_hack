import {makeAutoObservable} from "mobx";
import {ABOUT_US_ROUTE, CONTACTS_ROUTE, PLATFORMS_ROUTE} from "../consts";

export class NavStore {
    constructor() {
        this._nav = [
            {to: PLATFORMS_ROUTE, name: 'Креативные площадки'},
            {to: ABOUT_US_ROUTE, name: 'О нас'},
            {to: CONTACTS_ROUTE, name: 'Контакты'},
        ]
        this._business = [
            {id: 1, name: '1. Основная информация'},
            {id: 2, name: '2. Параметры площадки'},
            {id: 3, name: '3. Андрес пространства'},
            {id: 4, name: '4. О владельце'},
        ]
        this._info = [
            {id: 1, name: '1. Основная информация'},
            {id: 2, name: '2. О владельце'},
        ]
        makeAutoObservable(this)
    }

    get nav() {
        return this._nav
    }

    get business() {
        return this._business
    }

    get info() {
        return this._info
    }


}