import { Database } from "../database/config.js"

class dataModel {
    static obterdados(idCaixa) {
        try {
            return Database.executarQuery(`select * from Leitura where fkCaixa = ${idCaixa};`)
        } catch (error) {
            console.log(error)
        }
    }

    static atualizardados(idCaixa) {
        try {
            return Database.executarQuery(`select * from Caixa where id = ${idCaixa};`)
        } catch (error) {
            console.log(error)
        }
    }
}

export { dataModel }