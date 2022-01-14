const randomAnswer = (input) => {
    var output = "";

    var randomAnswersHello = ["hey", "I'm fine", "Hi", "whats up", "I'm okey", "sarchaw gyan", "Welcome what do you want"];

    // random answers for whats your name   
    var randomAnswersWhatsYourName = ["I'm Waldoo", "I'm Ahmed", "I'm Mohammed", "I'm Aziz", "I'm Jabar", "I'm Jack", "I'm Jackob", "I'm Jason"];

    if (input === "hello" || input === "hey" || input === "how are you") {
        output = randomAnswersHello[Math.floor(Math.random() * randomAnswersHello.length)];
    } else if (input.toLowerCase().replaceAll(/\s/g, '').replaceAll(/[^a-zA-Z ]/g, '') === "whatsyourname" || (input.toLowerCase().replaceAll(/\s/g, '').slice(-1) === '?' && input.toLowerCase().replaceAll(/\s/g, '') === "what'syourname?")) {
        output = randomAnswersWhatsYourName[Math.floor(Math.random() * randomAnswersWhatsYourName.length)];
    }

    return output;



}





const rightMessage = () => {
    let text = document.getElementById("text").value;
    if (text === "bye") {
        document.getElementById("text").style.display = "none";
        document.getElementById("sendBtn").style.display = "none";
        document.getElementById("response").innerHTML = "<b>Goodbye</b>";
    } else {
        let answer = randomAnswer(text)
        console.log(answer);
        document.getElementById("response").innerHTML = answer;
    }
}


document.getElementById("sendBtn").addEventListener("click", rightMessage);