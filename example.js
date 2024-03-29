// Pergunta a ser feita (Mude o valor da variável para testar o código)
const pergunta = "Qual seu time favorito?"

// Separar palavra por palavra da frase
const palavras = pergunta.split(" ") // Divide a string em arrays (Ex: "ela_é" se torna ["ela", "é"]

// Supõe o que é a pergunta
const suposicao = () => {
  let supostaPergunta = "" // Criada com let pois vamos mudar a cada iteração do for

  for(let i = palavras.length-1; i > palavras.length-4; i--) { // Vejo quais são as ultimas 3 palavras
    supostaPergunta = palavras[i] + " " + supostaPergunta // Insira a palavra que está na pergunta e o que já tem na variável
  }

  return supostaPergunta
}
// Muda termo
const mudaTermo = (supostaResposta) => { // Muda os sujeitos da frase para uma resposta em primeira pessoa
  if(supostaResposta.includes("seu")) { // Se tiver a palavra "seu"
    supostaResposta = supostaResposta.replace("seu", "meu") // Substitui "seu" por "meu"
  }
  if(supostaResposta.includes("você")) { // Se tiver a palavra "você"
    supostaResposta = supostaResposta.replace("você", "eu") // Substitui "você" por "eu"
  }

  return supostaResposta
}
// Trata a resposta
const trataResposta = (resposta) => {
  // Sorteia uma introdução aleatória para nossa resposta na nossa array de strings
  const introducoes = ["Bem...", "Hum...", "Ah...", "Quer mesmo só falar sobre", "Você quer saber sobre"] // Uma lista de introduções que nosso "MODELO" tem
  const introducao = introducoes[Math.floor(Math.random() * introducoes.length)] // Sorteia um número, e pega uma palavra nessa posição na array
  
  return `${introducao} ${resposta}` // Interpola a introdução com a resposta que já temos
}

// Monta a resposta
const montaResposta = () => {
  let resposta = suposicao()
  console.log("O que foi perguntado:")
  console.log(resposta)
  console.log("---------------------")
  console.log("Mudar para primeira pessoa:")
  resposta = mudaTermo(resposta)
  console.log(resposta)
  console.log("---------------------")
  console.log("Embeleza a resposta:")
  resposta = trataResposta(resposta)
  console.log(resposta)
  console.log("---------------------")
  console.log("Jorge: " + pergunta)
  console.log("Chatbot: " + resposta)
}

// Inicia o código
montaResposta()
