import sql from "mssql";

const sqlServerConfig = {
    user: "CloudSA49c766d4",
    password: "Urubu1004",
    database: "trackvisiondb",
    server: "trackvisiondb.database.windows.net",
    pool: {
        max: 10,
        min: 0,
        idleTimeoutMillis: 30000
    },
    options: {
        encrypt: true, // for azure
    }
}

class Database {
        static executarQuery(instrucao) {
            return new Promise(function (resolve, reject) {
                sql.connect(sqlServerConfig).then(function () {
                    return sql.query(instrucao);
                }).then(function (resultados) {
                    console.log(resultados);
                    resolve(resultados.recordset);
                }).catch(function (erro) {
                    reject(erro);
                    console.log('ERRO: ', erro);
                });
                sql.on('error', function (erro) {
                    return ("ERRO NO SQL SERVER (Azure): ", erro);
                });
        }); 

    }
}

export {Database};