import {makeAutoObservable} from "mobx";
import img from "../statics/platform_img.png";

export class PlatformStore {
    constructor() {
        this._platforms = [
            {id: 1, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '2.3'},
            {id: 2, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 3, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '3.9'},
            {id: 4, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 5, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.0'},
            {id: 6, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 7, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '3.0'},
            {id: 8, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '4.9'},
            {id: 9, image: img, name: 'Cube.Moscow', address: 'Москва, Таганская (7 мин)', footage: '70', capacity: '35', tel: '+7 (999) 888-77-66', price: '599', rating: '5.0'},
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