import { Usuario } from "../models/Usuarios.js"

class UsuarioController {
    static async cadastrarUsuario(req, res) {

        const ispb = req.body.ispbController
        const nome = req.body.nomeController
        const email = req.body.emailController
        const senha = req.body.senhaController

        console.log("ISPB CADASTRADO: ", ispb)
        console.log("NOME CADASTRADO: ", nome)
        console.log("EMAIL CADASTRADO: ", email)
        console.log("SENHA CADASTRADA: ", senha)



    try {

        return await Usuario.cadastrarUsuario(ispb, nome, email, senha)
    }
    catch (erro) {

        console.log(erro)
    }
        
    }
}

export { UsuarioController };