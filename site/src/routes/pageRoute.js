import Router from "express";
import express from "express";
import path from "path";

const router = Router()

router.get("/", (req, res) => {
    res.sendFile(path.resolve("site/public/view/index.html"))
})

router.get('/login', (req, res) => {
    res.sendFile(path.resolve("site/public/view/login.html"))
})

router.get("/cadastroUsuario", (req,res) => {
    res.sendFile(path.resolve("site/public/view/register.html"))
})

router.get("/dashboardTecnico", (req, res) => {
    res.sendFile(path.resolve("site/public/view/dashboard.html"))
})

router.get("/dashboardSeguranca", (req, res) => {
    res.sendFile(path.resolve("site/public/view/dashboard_julia.html"))
})

router.get("/dashboardVidaUtil", (req, res) => {
    res.sendFile(path.resolve("site/public/view/dashboard_gabriel.html"))
})

router.get("/dashboardTemp", (req, res) => {
    res.sendFile(path.resolve("site/public/view/dashboard_Michelly.html"))
})

router.get("/dashboardTemperatura", (req, res) => {
    res.sendFile(path.resolve("site/public/view/dashboard_aaa.html"))
})

export default router;