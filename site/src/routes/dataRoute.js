import Router from "express";
import { dataController } from "../controllers/dataController.js";

const router = Router()

router.get('/obterdados/:idCaixa', function (req, res) {
    dataController.obterdados(req, res)
})

router.post('/atualizardados', function(req, res) {
    dataController.atualizardados(req, res)
})

export default router