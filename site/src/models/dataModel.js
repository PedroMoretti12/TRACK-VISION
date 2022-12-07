import { Database } from "../database/config.js"

class dataModel {
    static obterdados(idCaixa) {
        try {
            return Database.executarQuery(`select * from Leitura where fkCaixa = ${idCaixa} order by momento desc;`)
        } catch (error) {
            console.log(error)
        }
    }

    static atualizardados(idCaixa) {
        try {
            return Database.executarQuery(`select top 1 * from Leitura where fkCaixa = ${idCaixa} ORDER BY momento desc;`)
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

    static obterdadosGabriel(idCaixa) {
        try {
        return Database.executarQuery(`SELECT TOP(1) vidaUtil FROM Caixa ORDER BY id DESC;`)
        } 
        catch (error) {
            console.log(error)
        }
    }


    static atualizarCards2(idCaixa){
        try {
            return Database.executarQuery(`select top 1 servicosPerigosos as ServiceP,processosPerigosos as ProcessP from Leitura where fkCaixa = ${idCaixa} order by momento desc;`)
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

    static obterMediaMichelly(idCaixa) {
        try {
        return Database.executarQuery(`SELECT cpuPorcentagem from Proj_Michelly where fkcaixa = 1;`)
        }
        catch (error) {
            console.log(error)
        } 
    }

    static obterdadosMichelly(idCaixa) {
        try {
        return Database.executarQuery(`declare @Existingdate datetime
        Set @Existingdate=GETDATE()
        Select TOP 15 CONVERT(varchar, dateadd(hour, -3, @Existingdate), 24) as formatada, * FROM Proj_Michelly WHERE fkCaixa = ${idCaixa} order by hora desc;`)
        }
        catch (error) {
            console.log(error)
        } 
    }

    static atualizardadosMichelly(idCaixa) {
        try {
            return Database.executarQuery(`declare @Existingdate datetime
            Set @Existingdate=GETDATE() SELECT TOP 1 CONVERT(varchar, dateadd(hour, -3, @Existingdate), 24) as formatada, * FROM Proj_Michelly WHERE fkCaixa = 1 order by hora desc;`)
        } catch (error) {
            console.log(error)
        }
    }



}

export { dataModel }