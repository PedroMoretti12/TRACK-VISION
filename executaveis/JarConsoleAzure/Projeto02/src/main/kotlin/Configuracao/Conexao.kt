package configuracao
import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.JdbcTemplate
class Conexao {

    val driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    val url = "jdbc:sqlserver://trackvisiondb.database.windows.net;databaseName=trackvisiondb;"
    val username = "CloudSA49c766d4"
    val password = "Urubu1004"

    fun getJdbcTemplate(): JdbcTemplate {
        val dataSource = BasicDataSource();
        dataSource.driverClassName = driver
        dataSource.url = url
        dataSource.username = username
        dataSource.password = password
        return JdbcTemplate(dataSource)
    }

    fun inserir(cpu:Double,disco:Double,ram:Double,servicosAtuais:Int,processosAtuais:Int,processosPerigosos:Int,servicosPerigosos:Int,tempCpu:Double){
        val conexao = getJdbcTemplate()
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosPerigosos,servicosPerigosos,tempCpu,momento) values(1,1,1,?,?,?,?,?,?,?,?,@Date)", cpu,ram,disco,servicosAtuais,processosAtuais,processosPerigosos,servicosPerigosos,tempCpu)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosPerigosos,servicosPerigosos,tempCpu,momento) values(1,1,31,?,?,?,?,?,?,?,?,@Date)", cpu*1.02,ram*1.00,disco*1.05,servicosAtuais ,processosAtuais ,processosPerigosos*2,servicosPerigosos+1,tempCpu+4)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosPerigosos,servicosPerigosos,tempCpu,momento) values(1,1,41,?,?,?,?,?,?,?,?,@Date)", cpu*1.04,ram*1.05,disco*1.20,servicosAtuais,processosAtuais,processosPerigosos+1,servicosPerigosos+2,tempCpu*2)
    }

    fun inserirProcesso(pid:Int,nomeProcesso:String,uso_cpu:Double,uso_memoria:Double){
        val conexao = getJdbcTemplate()
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Projeto_Julia(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso,momento) values(1,1,1,?,?,?,?,@Date)",pid,nomeProcesso,uso_cpu,uso_memoria)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Projeto_Julia(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso,momento) values(1,1,31,?,?,?,?,@Date)",pid,nomeProcesso,uso_cpu,uso_memoria*1.25)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Projeto_Julia(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso,momento) values(1,1,41,?,?,?,?,@Date)",pid,nomeProcesso,uso_cpu*1.05,uso_memoria*1.05)
    }


}