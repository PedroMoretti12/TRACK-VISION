import express from "express";
import routes from "./site/src/routes/indexRoute.js"
import cors from "cors";
import bodyParser from 'body-parser'

const app = express();
app.use(bodyParser.json())

routes(app)
app.use(express.static('site/public'));
app.use(express.static('site/public/dashboard'))
app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: false }));

export default app;