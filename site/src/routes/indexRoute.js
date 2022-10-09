import index from './pageRoute.js'
import user from './userRoute.js'
import data from './dataRoute.js'

const routes = (app) => {
    app.use('/usuarios', user)
    app.use('/data', data)
    app.use(index)
}

export default routes