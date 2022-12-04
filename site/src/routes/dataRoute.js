import Router from "express";
import { dataController } from "../controllers/dataController.js";

const router = Router()

router.get('/obterdados/:idCaixa', function (req, res) {
    dataController.obterdados(req, res)
})

router.get('/obterdadosJulia/:idCaixa', function (req, res) {
    dataController.obterdadosJulia(req, res)
})

router.get('/atualizardados/:idCaixa', function(req, res) {
    dataController.atualizardados(req, res)
})

router.get('/atualizardadosJulia/:idCaixa', function(req, res) {
    dataController.atualizardadosJulia(req, res)
})

router.get('/obtermedia/:idAgencia', function(req, res){
    dataController.obterMedia(req, res)
})

router.get('/obterRegressao/:idAgencia', function(req, res) {
    dataController.obterRegressao(req, res)
})

router.get('/atualizarCards/:idCaixa', function(req, res) {
    dataController.atualizarCards(req, res)
})


export default router