import { palavrasFutebol, palavrasMundialPalmeiras, palavrasRegras, palavrasTimeGosta, mostProbablyQuestion } from './can-i-answer.js'
// O que ele vai poder responder?
// - O que é futebol?
// - Quais as regras do futebol?
// - Que time ele mais gosta?
// - Palmeiras tem mundial?

console.log(palavrasFutebol)

// TENSIONAR ALGUM DOS PONTOS
palavrasFutebol.matched = 4

// Verfica quem foi mais tensionado
console.log(mostProbablyQuestion())