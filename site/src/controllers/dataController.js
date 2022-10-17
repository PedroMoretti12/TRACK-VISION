import { dataModel } from "../models/dataModel.js"

class dataController {
    static obterdados(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.obterdados(idCaixa)
            .then(response => {
                res.status(200).json(response)
            }).catch(e => {
                console.log(e)
                res.status(500).send()
            })

        // try {

            // return await dataModel.obterdados(idCaixa)
        // } catch (erro) {
        //}   
    }

    static atualizardados(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.atualizardados(idCaixa)
            .then(response => {

                res.status(200).json(response)
            }).catch(e => {
           
                console.log(e)
                res.status(500).send()
            })

        // try {

            // return await dataModel.obterdados(idCaixa)
        // } catch (erro) {
        //}   
    }

    static obterMedia(req, res) {

        var idAgencia = req.params.idAgencia;
        console.log(idAgencia)

        dataModel.obterMedia(idAgencia)
        .then(response => {
            res.status(200).json(response)
        })
        .catch(error => {
            console.log(error)
            res.status(500).send()
        })

    }
}

export { dataController }