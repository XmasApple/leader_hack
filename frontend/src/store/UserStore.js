import {makeAutoObservable} from "mobx";

export class UserStore {
    constructor() {
        this._isAuth = false
        this._isBusiness = false
        this._user = {}
        makeAutoObservable(this)
    }

    setIsAuth(bool) {
        this._isAuth = bool
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
    get user() {
        return this._user
    }


}