import {makeAutoObservable} from "mobx";

export class EventTypeStore {
    constructor() {
        this._types = [
            {id: 1, name: 'выставка'},
            {id: 2, name: 'ярмарка'},
            {id: 3, name: 'праздник'},
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