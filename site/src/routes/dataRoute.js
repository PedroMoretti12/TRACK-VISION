import Router from "express";
import { dataController } from "../controllers/dataController.js";

const router = Router()

router.get('/obterdados/:idCaixa', function (req, res) {
    dataController.obterdados(req, res)
})

router.get('/obterdadosJulia/:idCaixa', function (req, res) {
    dataController.obterdadosJulia(req, res)
})

router.get('/obterdadosMichelly/:idCaixa', function (req, res) {
    dataController.obterdadosMichelly(req, res)
})

router.get('/obterdadosMichelly1/:idCaixa', function (req, res) {
    dataController.obterdadosMichelly1(req, res)
})

router.get('/atualizardados/:idCaixa', function(req, res) {
    dataController.atualizardados(req, res)
})

router.get('/atualizardadosJulia/:idCaixa', function(req, res) {
    dataController.atualizardadosJulia(req, res)
})

router.get('/obterdadosGabriel/:idCaixa', function (req, res){
    dataController.obterdadosGabriel(req, res)
})

router.get('/atualizardadosMichelly/:idCaixa', function(req, res) {
    dataController.atualizardadosMichelly(req, res)
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

router.get('/atualizarCards2/:idCaixa', function(req, res) {
    dataController.atualizarCards2(req, res)
})

export default router