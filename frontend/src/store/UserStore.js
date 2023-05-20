import {makeAutoObservable} from "mobx";

export class UserStore {
    constructor() {
        this._isAuth = false
        this._isBusiness = true
        this._isAdmin = false
        this._user = {}
        makeAutoObservable(this)
    }

    setIsAuth(bool) {
        this._isAuth = bool
    }
    setIsBusiness(bool) {
        this._isBusiness = bool
    }
    setIsAdmin(bool) {
        this._isAdmin = bool
    }
    setUser(user) {
        this._user = user
    }

    get isAuth() {
        return this._isAuth
    }
    get isBusiness() {
        return this._isBusiness
    }
    get isAdmin() {
        return this._isAdmin
    }
    get user() {
        return this._user
    }


}