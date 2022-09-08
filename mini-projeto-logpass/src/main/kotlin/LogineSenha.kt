import javax.swing.JOptionPane

fun main() {

    val verifica = Validador()

    var cont = 0
    while (cont < 3) {

        verifica.email = JOptionPane.showInputDialog("E-mail: ")
        verifica.senha = JOptionPane.showInputDialog("Senha: ")

        if (verifica.logado()) {
            JOptionPane.showMessageDialog(null, "Bem-vindo à Track Vision!")
            break
        }
        JOptionPane.showMessageDialog(null, "Tente novamente!")
        cont++
    }
    if (cont == 3) {
        JOptionPane.showMessageDialog(null, "Número de tentativas excedidas!")
    }
}
// Track Vision - Team 10