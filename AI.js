// create a function to return random text while given an input 
// of a string of possible characters
function randomText(input) {
    var output = "";
    // for (var i = 0; i < input.length; i++) {
    //     output += input.charAt(Math.floor(Math.random() * input.length));
    // }
    // create an array and insert this strings into it
    // hello 
    // how are you 
    //  whats your name
    // are you okey
    // what is your favourite colour
    // what is your favourite animal
    // what is your favourite food

    var array = ["hello", "how are you", "whats your name", "are you okey", "what is your favourite colour", "what is your favourite animal", "what is your favourite food"];

    // loop through the array and if the input is hello then return hey
    // if the input is how are you then return I'm fine
    // if the input is whats your name then return I'm Waldoo
    // if the input is are you okey then return yes
    // if the input is what is your favourite colour then return blue
    // if the input is what is your favourite animal then return dog
    // if the input is what is your favourite food then return pizza
    let isHas = false;
    if (input.includes("?") || input.includes("!") || input.includes(",") || input.includes(".") || input.includes(":") || input.includes(";")) {
        isHas = true;

    }
    array.forEach(function() {
        // create an array of random answers to question hello
        var randomAnswers = ["hey", "I'm fine", "What about you", "whats up", "I'm okey", "sarchaw gyan", "Welcome what do you want"];
        // create an array of ?,!,,.,:,;
        var punctuation = ["?", "!", ",", ".", ":", ";"];
        // check if the input has on of this puntuation
        if ((input === "hello" && isHas === true) || (input === "hello" || isHas === true)) {
            // give random answers of the array randomAnswers
            output = randomAnswers[Math.floor(Math.random() * randomAnswers.length)];
        } else if (input === "how are you") {
            output = "I'm fine";
        } else if (input === "whats your name") {
            output = "I'm Waldoo";
        } else if (input === "are you okey") {
            output = "yes";
        } else if (input === "what is your favourite colour") {
            output = "blue";
        } else if (input === "what is your favourite animal") {
            output = "dog";
        } else if (input === "what is your favourite food") {
            output = "pizza";
        }
    });

    return output;



}


// get the text from the input with the id of text input
// send the text to the randomText function
// return the answer
function insertText() {
    var text = document.getElementById("text").value;
    if (text === 'bye') {
        // console.log("hahahah")
        // hide the input with an id of text
        document.getElementById("text").style.display = "none";
        // hide the button with an id of sendBtn
        document.getElementById("sendBtn").style.display = "none";


    }
    var answer = randomText(text);
    // console.log(answer);
    document.getElementById("answer").innerHTML = answer;
}

// when the button with the id of sendBtn is clicked call the insertText function
document.getElementById("sendBtn").addEventListener("click", insertText);