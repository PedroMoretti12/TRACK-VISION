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
            return Database.executarQuery(`SELECT TOP 1 * FROM Projeto_Julia  WHERE fkCaixa = ${idCaixa} order by momento desc;`)
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

    static atualizarCards(idCaixa){
        try {
            return Database.executarQuery(`select top 1 servicosAtivos as Service,processosAtivos as Process from Leitura where fkCaixa = ${idCaixa} order by momento desc;`)
            }
            catch (error) {
                console.log(error)
            } 
    }

    static obterdadosJulia(idCaixa) {
        try {
        return Database.executarQuery(`SELECT TOP 5 * FROM Projeto_Julia  WHERE fkCaixa = ${idCaixa} order by momento desc;`)
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