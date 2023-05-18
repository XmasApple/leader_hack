import {makeAutoObservable} from "mobx";

export class PlatformCapacityStore {
    constructor() {
        this._capacity = [
            {id: 1, name: '1-20'},
            {id: 2, name: '21-40'},
            {id: 3, name: '41-60'},
            {id: 4, name: '61-80'},
            {id: 5, name: '81 и более'},
        ]
        makeAutoObservable(this)
    }

    setCapacity(capacity) {
        this._capacity = capacity
    }

    get capacity() {
        return this._capacity
    }


}