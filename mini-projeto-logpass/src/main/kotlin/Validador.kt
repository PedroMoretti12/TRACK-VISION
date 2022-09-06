class Validador {

    lateinit var email: String
    lateinit var senha: String
    val cadbanco = mutableListOf<String>()

    fun logado(): Boolean {
        return (email == "fernando@sptech.com" && senha == "123")
    }
}

// Rafaela Dias (SIS) for Track Vision - Team 10