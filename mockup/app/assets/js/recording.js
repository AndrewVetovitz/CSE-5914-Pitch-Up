$(document).ready(function(){
    console.log("fug")
    var isRecording = false;
    var timeStart;
    var timeElapsed = 0;
    $("#recordingButton").click(() => {
        isRecording = !isRecording;
        
        if(isRecording){
            $("#recordingButton").text("Stop Recording")
            timeStart = Date.now();
            setInterval(function() {
                $("#recordingTimer").text(((Date.now() - timeStart)/1000).toFixed(2))
            }, 17)
            var visual = new p5(micSketch);
        }
        if(!isRecording){
            window.location.href = "http://localhost:8080/analyzing"
        }
    })
})

var micSketch = function(sketch){
    var mic, fft;
  
    sketch.setup = function() {
        var cnv = sketch.createCanvas(710,400);
        cnv.parent('recordingVisual')
        sketch.noFill();
     
        mic = new p5.AudioIn();
        mic.start();
        fft = new p5.FFT();
        fft.setInput(mic);
    };  

    sketch.draw = function() {
        sketch.background(255);

        var spectrum = fft.analyze();
     
        sketch.beginShape();
        for (i = 0; i<spectrum.length; i++) {
         sketch.vertex(i, sketch.map(spectrum[i], 0, 255, sketch.height, 0) - 100 );
        }
        sketch.endShape();             
    };
}


