import { Database } from "../database/config.js"

class Usuario {
    static async cadastrarUsuario(ispb, nome, email, senha) {
        
        const bancoQuery = await Database.executarQuery(`SELECT id FROM Banco WHERE ISPB = ${ispb}`)
        const fkBanco = bancoQuery[0].id

        try {
            
            await Database.executarQuery(`INSERT INTO USUARIO (fkBanco, nome, email, senha) VALUES (${fkBanco}, '${nome}', '${email}', '${senha}')`)
            console.log(`Usuário novo inserido na Azure.\n Banco de ID: ${fkBanco}\n Nome: ${nome}\n Email: ${email}`)


        } catch (error) {
            console.log(error)
        }
    }
}

export { Usuario }