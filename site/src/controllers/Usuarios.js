import { Usuario } from "../models/Usuarios"

class UsuarioController {
    static async cadastrarUsuario() {
        ispb = req.body.isbpController
        nome = req.body.nomeController
        email = req.body.emailController
        senha = req.body.senhaController

        Usuario.cadastrarUsuario(ispb, nome, email, senha)
        .then(function(resultado) {
            res.json(resultado)
            console.log(resultado)
        })
        .catch(function(erro) {
            console.log(erro)
        })
    }
};

export default { UsuarioController };