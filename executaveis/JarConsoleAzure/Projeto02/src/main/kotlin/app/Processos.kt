package app
import com.github.britooo.looca.api.core.Looca
import configuracao.Conexao
import java.lang.Exception

fun main() {
   var repositorio = Looca()

    var all_Process = repositorio.grupoDeProcessos.processos
    var all_Services = repositorio.grupoDeServicos.servicos

    val processosPadrao = mutableListOf<String>()
    val  servicosPadrao = mutableListOf<String>()

    all_Process.forEach {
        processosPadrao.add(it.nome)
    }

    all_Services.forEach {
        servicosPadrao.add(it.nome)
    }

    while (true) {
        //Info PC
        val pc_Cpu = (repositorio.processador.uso).toDouble()
        var pc_Ram = (repositorio.memoria.emUso / 1024 / 1024 / 1024).toDouble()
        var pc_Disco = (repositorio.grupoDeDiscos.volumes[0].disponivel / 1024 / 1024 / 1024).toDouble()
        var tempCpu = (repositorio.temperatura.temperatura).toDouble()


        //Processos
        var servicos_Atuais = repositorio.grupoDeServicos.totalDeServicos
        var processos_Atuais = repositorio.grupoDeProcessos.totalProcessos
        var processos_Perigosos = processos_Atuais - processosPadrao.size
        var servicos_Perigosos = servicos_Atuais - servicosPadrao.size

        //INSERÇÃO CPU

        Conexao().inserir(pc_Cpu,pc_Disco,pc_Ram,servicos_Atuais,processos_Atuais,processos_Perigosos,servicos_Perigosos,tempCpu)
        println("inseri os dados do PC")
        println(processos_Perigosos)
        println(servicos_Perigosos)

        //Inserção PROCESSOS
        all_Process.forEach {
            if (it.usoCpu > 5) {
                Conexao().inserirProcesso(it.pid, it.nome, it.usoCpu/20, it.usoMemoria)
                println("inseri: ${it.usoCpu}")
            }
        }
    }
}