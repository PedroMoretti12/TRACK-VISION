import index from './pageRoute.js'
import user from './userRoute.js'

const routes = (app) => {
    app.use('/usuarios', user)
    app.use(index)
}

export default routes