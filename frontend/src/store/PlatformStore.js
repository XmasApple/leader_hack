import {makeAutoObservable} from "mobx";
import img from "../statics/platform_img.png";

export class PlatformStore {
    constructor() {
        this._platforms = [
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
        ]
        makeAutoObservable(this)
    }

    setPlatforms(platforms) {
        this._platforms = platforms
    }

    get platforms() {
        return this._platforms
    }


}