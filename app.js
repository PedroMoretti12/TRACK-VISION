import express from "express";
import routes from "./site/src/routes/indexRoute.js"

const app = express();

routes(app)
app.use(express.static('site/public'));


export default app;