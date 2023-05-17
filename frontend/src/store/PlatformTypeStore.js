import {makeAutoObservable} from "mobx";
import {ABOUT_US_ROUTE, CONTACTS_ROUTE, PLATFORMS_ROUTE} from "../consts";

export class PlatformTypeStore {
    constructor() {
        this._types = [
            {id: 1, name: 'Выставочные залы'},
            {id: 2, name: 'Художественные выставки / галереи'},
            {id: 3, name: 'Залы конференций '},
            {id: 4, name: 'Залы для репетиций'},
            {id: 5, name: 'Фотостудии'},
            {id: 6, name: 'Корпоративные мероприятия'},
            {id: 7, name: 'Места для проведения совещаний'},
            {id: 8, name: 'Секонд Хенды '},
            {id: 9, name: 'Студии звукозаписи '},
            {id: 10, name: 'На открытом воздухе'},
            {id: 11, name: 'Танцевальные студии'},
            {id: 12, name: 'Студии для креативного производства '},
            {id: 13, name: 'Складские помещения'},
        ]
        makeAutoObservable(this)
    }

    setPlatformsTypes(types) {
        this._types = types
    }

    get types() {
        return this._types
    }


}