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

    fun inserir(cpu:Double,disco:Double,ram:Double,servicosAtuais:Int,processosAtuais:Int,processosPerigosos:Int,servicosPerigosos:Int){
        val conexao = getJdbcTemplate()
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosIncoerentes,servicosIncoerentes,processosPerigosos,momento) values(1,1,1,?,?,?,?,?,?,?,@Date)", cpu,ram,disco,servicosAtuais,processosAtuais,processosPerigosos,servicosPerigosos)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosIncoerentes,servicosIncoerentes,momento) values(1,1,2,?,?,?,?,?,?,?,@Date)", cpu*1.05,ram*1.00,disco*1.05,servicosAtuais * 2,processosAtuais * 2,processosPerigosos*2,servicosPerigosos*2)
        conexao.update("DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into Leitura(fkBanco,fkAgencia,fkCaixa,cpuPorcentagem,ramPorcentagem,hdPorcentagem,processosAtivos,servicosAtivos,processosIncoerentes,servicosIncoerentes,momento) values(1,1,3,?,?,?,?,?,?,?,@Date)", cpu*1.20,ram*1.05,disco*1.20,servicosAtuais,processosAtuais,processosPerigosos,servicosPerigosos)
    }

    fun inserirProcesso(pid:Int,nomeProcesso:String,uso_cpu:Double,uso_memoria:Double){
        val conexao = getJdbcTemplate()
        conexao.update("insert into Leitura(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso) values(1,1,1,?,?,?)",pid,nomeProcesso,uso_cpu,uso_memoria)
        conexao.update("insert into Leitura(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso) values(1,1,2,?,?,?)",pid,nomeProcesso,uso_cpu*1.25,uso_memoria*1.25)
        conexao.update("insert into Leitura(fkBanco,fkAgencia,fkCaixa,pid, nomeProcesso, usoCpuProcesso,UsoMemoriaProcesso) values(1,1,3,?,?,?)",pid,nomeProcesso,uso_cpu*1.05,uso_memoria*1.05)
    }


}