import { palavrasFutebol, palavrasMundialPalmeiras, palavrasRegras, palavrasTimeGosta, mostProbablyQuestion } from './can-i-answer.js'
// O que ele vai poder responder?
// - O que é futebol?
// - Quais as regras do futebol?
// - Que time ele mais gosta?
// - Palmeiras tem mundial?
// - Como lidar com perguntas que não são sobre o tema... (LIÇÃO DE CASA)


let pergunta = "O palmeiras palmeira palmeira tem mundial?" // Inicialmente isso é uma string
console.log(pergunta)
pergunta = pergunta.split(' ')
console.log(pergunta)

const bancoDeAssuntos = [palavrasFutebol, palavrasMundialPalmeiras, palavrasRegras, palavrasTimeGosta,]
console.log(bancoDeAssuntos)

pergunta.forEach(palavra => {
    // é uma pergunta de o que é futebol?
    for (let i = 0; i < bancoDeAssuntos.length; i++) {
        if(bancoDeAssuntos[i].probablyWords.indexOf(palavra) !== -1) {// Achou ou não (indice ou -1)
            bancoDeAssuntos[i].matched++
        } else {
            // Tratar isso depois
        }
    }
})

console.log("------------------------------")
console.log(bancoDeAssuntos)


// console.log(palavrasFutebol)
// perguntaArray.array.forEach(palavra => {
//     // Procure nas arrays
//         // Se achou em alguma, tensione
//         // Achei na array do palmeirasMundial
//         // palmeirasMundial.matched++

//         // Se não achou
// })

// // TENSIONAR ALGUM DOS PONTOS
// palavrasFutebol.matched = 2
// palavrasMundialPalmeiras.matched = 5



// // Verfica quem foi mais tensionado
// console.log(mostProbablyQuestion())