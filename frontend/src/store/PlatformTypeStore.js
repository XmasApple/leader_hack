import {makeAutoObservable} from "mobx";
import {ABOUT_US_ROUTE, CONTACTS_ROUTE, PLATFORMS_ROUTE} from "../consts";

export class PlatformTypeStore {
    constructor() {
        this._types = [
            {id: 1, name: 'Киностудии'},
            {id: 2, name: 'Галереи'},
            {id: 3, name: 'Издательства'},
            {id: 4, name: 'Книжные магазины'},
            {id: 5, name: 'Выставочные залы'},
            {id: 6, name: 'Дизайн студии'},
            {id: 7, name: 'Креативные пространства'},
            {id: 8, name: 'Кинотеатры'},
            {id: 9, name: 'Звукозаписывающие студии'},
            {id: 10, name: 'Танцевальная студия'},
            {id: 11, name: 'AR/VR студии'},
        ]
        makeAutoObservable(this)
    }

    setTypes(types) {
        this._types = types
    }

    get types() {
        return this._types
    }


}