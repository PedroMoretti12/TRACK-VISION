import Router from "express";
import { UsuarioController } from "../controllers/Usuarios.js";

const router = Router()

router.post('/cadastrarusuario', function (req, res) {
    UsuarioController.cadastrarUsuario(req, res)
})

export default router