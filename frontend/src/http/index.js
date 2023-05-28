import axios from 'axios'

const $host = axios.create({
    baseURL: process.env.PYTHON_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
    }
})

const $authHost = axios.create({
    baseURL: process.env.PYTHON_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
    }
})

const authInterceptor = config => {
    config.headers.authorization = `Bearer ${localStorage.getItem('token')}`
    return config
}

$authHost.interceptors.request.use(authInterceptor)

export {
    $host,
    $authHost
}
