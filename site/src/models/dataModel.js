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
            return Database.executarQuery(`select top 1 * from Leitura where fkCaixa = 1 ORDER BY momento desc;`)
        } catch (error) {
            console.log(error)
        }
    }

    static obterMedia(idAgencia) {
        try {
        return Database.executarQuery(`SELECT AVG(cpuPorcentagem) AS "Cpu", AVG(ramPorcentagem) AS "Ram", AVG(hdPorcentagem) AS "Hd" FROM Leitura WHERE fkAgencia = ${idAgencia};`)
        }
        catch (error) {
            console.log(error)
        } 
    }

}

export { dataModel }