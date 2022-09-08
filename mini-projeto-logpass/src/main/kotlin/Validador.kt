class Validador {

    lateinit var email: String
    lateinit var senha: String

    fun logado(): Boolean {
        return (email == "fernando@sptech.com" && senha == "123")
    }
}

// Track Vision - Team 10