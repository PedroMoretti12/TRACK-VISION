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

    static atualizardadosJulia(idCaixa) {
        try {
            return Database.executarQuery(`select t2.* from (select nomeProcesso, max(momento) as momento from Projeto_Julia where fkCaixa = ${idCaixa} group by nomeProcesso) t1 join [dbo].[Projeto_Julia] t2 on t1.momento = t2.momento`)
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

    static obterdadosJulia(idCaixa) {
        try {
        return Database.executarQuery(`SELECT * FROM Projeto_Julia WHERE fkCaixa = ${idCaixa};`)
        }
        catch (error) {
            console.log(error)
        } 
    }

    static regressao(idAgencia) {
        try {
            return Database.executarQuery(`SELECT * FROM Leitura WHERE fkAgencia = ${idAgencia}`)
        } catch (error) {
            console.log(error)
        }
    }

}

export { dataModel }