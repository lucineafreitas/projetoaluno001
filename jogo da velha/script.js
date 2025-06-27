var jogador = "x";

function jogar(celula){
    
    //compara se a célula está vazia para assim escrever
    if(celula.innerHTML == ""){

        //escreva a letra na célula
        celula.innerHTML = jogador;

        //alterna a variável jogador para a próxima jogada
        if(jogador == "x"){
            jogador = "o";
            celula.style.backgroundColor = "gold";
            
         }else{
            jogador = "x";
            celula.style.backgroundColor = "silver";
        }
    }
}

function reiniciar(){
    window.location.reload();
}