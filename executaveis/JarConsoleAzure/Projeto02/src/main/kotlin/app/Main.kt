package app

import com.github.britooo.looca.api.core.Looca
import configuracao.Conexao

fun main() {
    val repositorio = Looca()
    val conexao = Conexao().getJdbcTemplate()


    val processJ = repositorio.grupoDeProcessos.processos
    val processosPadrao = mutableListOf<String>()
    val servicosPadrao = mutableListOf<String>()

    var c = 0
    while (c < processJ.size - 1) {
        processosPadrao.add(repositorio.grupoDeProcessos.processos[c].nome)
        c++
    }
    var b = 0
    while (b < repositorio.grupoDeServicos.servicos.size - 1) {
        servicosPadrao.add(repositorio.grupoDeServicos.servicos[c].nome)
        b++
    }

    while (true) {

        val uso_cpu = (repositorio.processador.uso).toDouble()
        var uso_ram = (repositorio.memoria.emUso / 1024 / 1024 / 1024).toDouble()
        var uso_disco = (repositorio.grupoDeDiscos.volumes[0].disponivel / 1024 / 1024 / 1024).toDouble()
        var servicosAtuais = (repositorio.grupoDeServicos.servicos.size)
        var processAtuais = (repositorio.grupoDeProcessos.processos.size)
        var processosPerigosos = (processAtuais - processosPadrao.size)
        var servicosPerigosos = (servicosAtuais - servicosPadrao.size)
        var tempCpu = (repositorio.temperatura.temperatura).toDouble()

        Conexao().inserir(
            uso_cpu,
            uso_ram,
            uso_disco,
            servicosAtuais,
            processAtuais,
            processosPerigosos,
            servicosPerigosos,
            tempCpu
        )

        println("foi")
        var r = 0
        while (r < repositorio.grupoDeProcessos.processos.size - 1) {
            if (processJ[r].usoCpu > 0.5) {
                val pid = (processJ[r].pid).toInt()
                val nomeProcesso = (processJ[r].nome).toString()
                val uso_cpu = (processJ[r].usoCpu).toDouble()
                val uso_memoria = (processJ[r].usoMemoria).toDouble()
                r++
                Conexao().inserirProcesso(pid, nomeProcesso, uso_cpu, uso_memoria)
                println("foi2")
            } else {
                r++
            }


        }


    }
}

