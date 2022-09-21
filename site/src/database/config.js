import mysql2 from 'mysql2';

const connection = await mysql2.createConnection({
    host: 'localhost',
    user: 'pedro',
    database: 'Trackvision',
    password: '12830615tT-'
});

class Database {

    static executarQuery(instrucao) {
        return new Promise((resolve, reject) => {
            connection.query(instrucao,
                function(err, results) {
                    try {
                        console.log(results)
                    }
                    catch {
                        console.log(err)
                    }
        })
        })
    }

}

export {Database};