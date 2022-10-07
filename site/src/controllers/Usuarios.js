import { Usuario } from "../models/Usuarios.js"

class UsuarioController {
    static async cadastrarUsuario(req, res) {

        const ispb = req.body.ispbController
        const nome = req.body.nomeController
        const email = req.body.emailController
        const senha = req.body.senhaController

    try {

        return await Usuario.cadastrarUsuario(ispb, nome, email, senha)
    
    }
    catch (erro) {

        console.log(erro)
    
    }
        
    }

    static async entrar(req, res) {

        const email = req.body.emailController
        const senha = req.body.senhaController

        console.log(req.body.emailController)
        console.log(req.body.senhaController)

        try {
            
            const usuario = await Usuario.entrar(email, senha)

            if (usuario.length != 1) {

                console.log("Não encontrou usuário ou está indefinido.")
                res.status(400).send("Falha no login.")

            } else {

                res.status(200).send("Login encontrado.")

            }

        } catch (error) {
            
            console.log(error)

        }

    }


}

export { UsuarioController };
