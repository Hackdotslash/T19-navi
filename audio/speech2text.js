var SpeechRecognition = window.webkitSpeechRecognition;
var recognition = new SpeechRecognition();
var Content = '';

recognition.continuous = true;

recognition.onresult = function(event) {

  var current = event.resultIndex;

  var transcript = event.results[current][0].transcript;
 
    Content += transcript;
    console.log(Content);
  
};


recognition.onstart = function() { 
  console.log('Voice recognition is ON.');
}

recognition.onspeechend = function() {
  console.log('No activity.');
}

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    console.log('Try again.');  
  }
}


  recognition.start();

