import java.util.Scanner;
class MinhaBrincadeira {

    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        System.out.println("");

        System.out.println("Qual é o seu nome?");
        String nome = teclado.nextLine();
        System.out.println("");

        System.out.println("Qual é a sua idade?");
        String idade = teclado.nextLine();
        System.out.println("");

        System.out.println("Olá " + nome + ", e você tem " + idade + " anos, correto? (s/n)");
        String confirmacao = teclado.nextLine();
        System.out.println("");

        if (Integer.parseInt(idade) < 18) {
            System.out.println("Voce nao pode prosseguir, pois é menor de idade.\n");   
            return;
 
        } else if (confirmacao.equalsIgnoreCase("s")) {
            System.out.println("Ótimo podemos proseguir :)\n");
            
        } else if (confirmacao.equalsIgnoreCase("n")) {
            System.out.println("Re-faca o cadastro, se algo estiver errado.\n");
            
        } else {
            System.out.println("Resposta invalida. Por favor, responda com s ou n.\n");
        }    
        
    }
     
}