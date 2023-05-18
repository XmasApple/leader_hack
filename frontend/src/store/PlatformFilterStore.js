import {makeAutoObservable} from "mobx";

export class PlatformFilterStore {
    constructor() {
        this._filters = [
            {id: 1, name: 'по возрастанию цены'},
            {id: 2, name: 'по убыванию цены'},
            {id: 3, name: 'по рейтингу'},
        ]
        makeAutoObservable(this)
    }

    setFilters(filter) {
        this._filters = filter
    }

    get filters() {
        return this._filters
    }


}