import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import Quote from "components/Typography/Quote.jsx";
import Muted from "components/Typography/Muted.jsx";
import Primary from "components/Typography/Primary.jsx";
import Info from "components/Typography/Info.jsx";
import Success from "components/Typography/Success.jsx";
import Warning from "components/Typography/Warning.jsx";
import Danger from "components/Typography/Danger.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";
import Button from "components/CustomButtons/Button.jsx"

const style = {
  typo: {
    paddingLeft: "25%",
    marginBottom: "40px",
    position: "relative"
  },
  note: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    bottom: "10px",
    color: "#c0c1c2",
    display: "block",
    fontWeight: "400",
    fontSize: "13px",
    lineHeight: "13px",
    left: "0",
    marginLeft: "20px",
    position: "absolute",
    width: "260px"
  },
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  }
};
class RecordingStudio extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      finalTranscript: [],
      interimResult: '',
      recording: false,
      currentPitch: "Kitten Mittenz",
    }
    const BrowserSpeechRecognition =
      typeof window !== 'undefined' &&
      (window.SpeechRecognition ||
        window.webkitSpeechRecognition ||
        window.mozSpeechRecognition ||
        window.msSpeechRecognition ||
        window.oSpeechRecognition)
    
    this.recognition = new BrowserSpeechRecognition();
    this.recognition.continuous = true
    this.recognition.interimResults = true
    this.recognition.onresult = (event) => {
      var {finalTranscript} = this.state;
      var interimResult = ''
      console.log(event)
      for(var i = event.resultIndex; i < event.results.length; i++){
        if(event.results[i].isFinal){
          finalTranscript.push(event.results[i][0].transcript)
        } else {
          interimResult += event.results[i][0].transcript
        }
      }
      console.log(interimResult)
      this.setState({
        finalTranscript: finalTranscript,
        interimResult: interimResult
      })
    }
  }

  toggleRecording() {
    this.setState({
      recording: !this.state.recording
    }, () => {
      if(this.state.recording){
        this.recognition.start()
      } else {
        this.recognition.stop()
      }
    })
  }


  render() {
    const { classes } = this.props;
    return (
      <Card>
        <CardHeader color="primary">
          <h4 className={classes.cardTitleWhite}>Welcome to the Recording Studio!</h4>
          <p className={classes.cardCategoryWhite}>
            Currently recording pitch for <b>{this.state.currentPitch}</b>
          </p>
        </CardHeader>
        <CardBody style={{height: '600px', display: 'flex', flexDirection: 'column'}}>
          <h3> Ready to start Recording? </h3>
          <div style={{alignSelf: 'center'}}>
            <Button onClick={this.toggleRecording.bind(this)}> {!this.state.recording ? "Start Recording": "Stop Recording"} </Button>
            <div style={{color: 'grey', height: '80px'}}> {this.state.interimResult}</div>
            <div>
              {this.state.finalTranscript.map((line, index) => (
                <div key={index}> {line} </div>
              )
              )}
            </div>
          </div>
        </CardBody>
      </Card>
    );
  
  }
}

export default withStyles(style)(RecordingStudio);
