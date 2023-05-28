import {$host, $authHost} from "./index";
import jwt_decode from 'jwt-decode'

export const userLogin = async (json) => {
    const {data} = await $host.post('/users/auth', json)
    localStorage.setItem('token', data)
    return jwt_decode(data)
}

export const exit = async () => {
    localStorage.removeItem('token')
    return true
}