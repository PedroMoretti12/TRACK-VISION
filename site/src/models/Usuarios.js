import { Database } from "../database/config"

class Usuario {
    static async cadastrarUsuario(ispb, nome, email, senha) {
        
        fkBanco = Database.executarQuery(`SELECT id FROM BANCO WHERE ISPB = ${ispb}`)
        console.log(fkBanco)
        try {
            Database.executarQuery(`INSERT INTO USUARIO VALUES (${1}, ${1}, '${nome}', '${email}', '${senha}')`)
            console.log('Inserindo novo usuário na azure.')
        } catch (error) {
            console.log(error)
        }
    }
}

export { Usuario };