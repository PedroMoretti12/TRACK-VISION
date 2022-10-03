import express from "express";
import routes from "./site/src/routes/indexRoute.js"
import cors from "cors";

const app = express();

routes(app)
app.use(express.static('site/public'));
app.use(express.static('site/public/dashboard'))
app.use(cors())

export default app;