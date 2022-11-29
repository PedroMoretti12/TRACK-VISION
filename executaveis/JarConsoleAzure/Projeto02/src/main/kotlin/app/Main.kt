package app
import com.github.britooo.looca.api.core.Looca
import com.github.britooo.looca.api.group.processos.ProcessosGroup
import javax.swing.JOptionPane
import configuracao.Conexao
   fun main (){
            val repositorio = Looca()
            val conexao = Conexao().getJdbcTemplate()

       

            var processJ = repositorio.grupoDeProcessos.processos
            var servicosJ = repositorio.grupoDeServicos.servicos
            var processosPadrao = mutableListOf<String>()
            var servicosPadrao = mutableListOf<String>()

            var c = 0
            while(c < processJ.size) {
                processosPadrao.add(repositorio.grupoDeProcessos.processos[c].nome)
                c++
            }

            while(c < servicosJ.size) {
                servicosPadrao.add(repositorio.grupoDeServicos.servicos[c].nome)
                c++
            }

            while(true) {
                val uso_cpu = (repositorio.processador.uso).toDouble()
                var uso_ram = (repositorio.memoria.emUso / 1024 / 1024 / 1024).toDouble()
                var uso_disco = (repositorio.grupoDeDiscos.volumes[0].disponivel / 1024 / 1024 / 1024).toDouble()
                var servicosAtuais = (repositorio.grupoDeServicos.servicos.size).toInt()
                var processAtuais = (repositorio.grupoDeProcessos.processos.size).toInt()
                var processosPerigosos = (processAtuais - processosPadrao.size).toInt()
                var servicosPerigosos = (servicosAtuais - servicosPadrao.size).toInt()

                Conexao().inserir(uso_cpu, uso_ram, uso_disco, servicosAtuais, processAtuais, processosPerigosos, servicosPerigosos)


                while (c < repositorio.grupoDeProcessos.processos.size) {
                    if(processJ[c].usoCpu > 0.5){
                        val pid = (processJ[c].pid).toInt()
                        val nomeProcesso =  (processJ[c].nome).toString()
                        val uso_cpu=  (processJ[c].usoCpu).toDouble()
                        val uso_memoria = (processJ[c].usoMemoria).toDouble()

                        c++
                        Conexao().inserirProcesso(pid,nomeProcesso,uso_cpu, uso_memoria)

                    }
                    else {
                        c++
                    }


                }

            }
        }

