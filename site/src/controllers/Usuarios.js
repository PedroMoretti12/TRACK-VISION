import { Usuario } from "../models/Usuarios.js"

class UsuarioController {
    static async cadastrarUsuario(req, res) {
        const ispb = req.body.ispbController
        const nome = req.body.nomeController
        const email = req.body.emailController
        const senha = req.body.senhaController
    
    try {
        if (ispb != "" || nome != "" || email != "" || senha != "") {
            res.status(200).send("Cadastro realizado")
            return await Usuario.cadastrarUsuario(ispb, nome, email, senha)
        } else {
            res.status(501).send("Algum dado indefinido.")
        }
    }
    catch (erro) {

        console.log(erro)
    
    }
        
    }

    static async entrar(req, res) {

        const email = req.body.emailController
        const senha = req.body.senhaController

        try {
            
            const usuario = await Usuario.entrar(email, senha)

            if (usuario.length != 1) {

                console.log("Não encontrou usuário ou está indefinido.")
                res.status(400).send("Falha no login.")

            } else {

                res.status(200).send(usuario)

            }

        } catch (error) {
            
            console.log(error)

        }

    }


}

export { UsuarioController };
