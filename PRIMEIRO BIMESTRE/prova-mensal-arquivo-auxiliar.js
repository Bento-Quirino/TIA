const threshold = 0.9;

const labels = [
    "identity_attack",
    "insult",
    "obscene",
    "severe_toxicity",
    "sexual_explicit",
    "threat",
]

toxicity.load(threshold).then((model) => {
  const sentences = ["you are dumb"];

  model.classify(sentences).then((predictions) => {
    console.log(predictions);
  });
});
