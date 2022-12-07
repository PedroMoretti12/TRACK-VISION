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

    static obterdadosMichelly(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.obterdadosMichelly(idCaixa)
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

    static obterdadosGabriel(req, res) {
        var idCaixa = req.params.idCaixa;
        dataModel.obterdadosGabriel(idCaixa)
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

    static obterdadosJulia(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.obterdadosJulia(idCaixa)
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

    static atualizarCards(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.atualizarCards(idCaixa)
        .then(response => {
            res.status(200).json(response)
        }).catch(e => {
       
            console.log(e)
            res.status(500).send()
        })
    }

    static atualizarCards2(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.atualizarCards2(idCaixa)
        .then(response => {
            res.status(200).json(response)
        }).catch(e => {
       
            console.log(e)
            res.status(500).send()
        })
    }

    static atualizardadosJulia(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.atualizardadosJulia(idCaixa)
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

    static atualizardadosMichelly(req, res) {
        var idCaixa = req.params.idCaixa;

        dataModel.atualizardadosMichelly(idCaixa)
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

    static obterRegressao(req, res) {

        var idAgencia = req.params.idAgencia;
        
        dataModel.regressao(idAgencia)
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