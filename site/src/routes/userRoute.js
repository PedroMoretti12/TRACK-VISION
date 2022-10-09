import Router from "express";
import { UsuarioController } from "../controllers/Usuarios.js";


const router = Router()

router.post('/cadastrarusuario', function (req, res) {
    console.log("seila")
    console.log(req.originalUrl)
    UsuarioController.cadastrarUsuario(req, res)
})

router.post('/entrar', function(req, res) { 
    UsuarioController.entrar(req, res)
})


export default router