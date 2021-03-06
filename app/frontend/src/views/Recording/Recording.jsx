import React from "react";
import { withRouter } from 'react-router-dom'

// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
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
    },
    selected: {
        color: 'red'
    }
};
class RecordingStudio extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            finalTranscript: [],
            interimResult: '',
            recording: false,
            currentPitch: "Kitten Mittenz",
            time: 0,
            selected: ''
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
            var { finalTranscript } = this.state;
            var interimResult = ''
            //   console.log(event);
            for (var i = event.resultIndex; i < event.results.length; i++) {
                if (event.results[i].isFinal) {
                    finalTranscript.push(event.results[i][0].transcript)
                } else {
                    interimResult += event.results[i][0].transcript
                }
            }
            //   console.log(interimResult);
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
            if (this.state.recording) {
                this.setState({
                    finalTranscript: []
                }, () => {
                    this.recognition.start()
                    this.startTimer()
                })
            } else {
                this.recognition.stop()
                this.stopTimer()
            }
        })
    }

    getPitchId() {
        let hashProps = this.props.location.hash.split('#')
        let pitchId = 13371337
        if (hashProps.length > 1) {
            pitchId = hashProps[1]
        }
        return pitchId
    }

    analyzePitch() {
        let transcript = this.state.finalTranscript.reduce((acum, curr) => acum + ' ' + curr, '');
        let duration = this.state.time;
        localStorage.setItem('pitch_transcription', transcript);
        localStorage.setItem('pitch_duration', duration);
        var pitch_id = this.getPitchId()

        fetch('http://localhost:5000/pitch/' + pitch_id + '/new_try', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ transcription: transcript, duration: duration, company: this.state.selected })
        }).then((resp) => {
            if (!resp.ok) {
                throw Error("ruh roh")
            }
            return resp.json()
        }).then((json) => {
            this.props.history.push('/pitch_analysis#' + json.pitch_try_id);
        }).catch((err) => {
            this.props.history.push('/pitch_analysis#13371337');
        })
    }

    startTimer() {
        this.startTime = Date.now()
        this.timer = setInterval(() => {
            this.setState({
                time: ((Date.now() - this.startTime) / 1000).toFixed(2)
            })
        }, 16.6)
    }

    stopTimer() {
        if (this.timer) {
            clearInterval(this.timer)
        }
    }

    select(name){
        if(this.state.selected === name){
            this.setState({
                selected: ''
            });
        } else {
            this.setState({
                selected: name
            });
        }
    }

    getCompanyStyle(name){
        return this.state.selected === name ? 'danger' : null
    }

    render() {
        const { classes } = this.props;
        const transcriptAvailable = (this.state.finalTranscript.length > 0);

        return (
            <Card>
                <CardHeader color="primary">
                    <h4 className={classes.cardTitleWhite}>Welcome to the Recording Studio!</h4>
                    <p className={classes.cardCategoryWhite}>
                        Currently recording pitch for <b>{this.state.currentPitch}</b>
                    </p>
                </CardHeader>
                <CardBody style={{ height: '600px', display: 'flex', flexDirection: 'column' }}>
                    <h3> Ready to start Recording? </h3>
                    <div style={{ alignSelf: 'center', display: 'flex' }}>
                        {
                            this.state.selected === 'Amazon' || (!transcriptAvailable && !this.state.recording && this.state.selected === '')
                                ? <Button color={this.getCompanyStyle('Amazon')} onClick={this.select.bind(this, 'Amazon')}>Amazon</Button>
                                : <Button disabled>Amazon</Button>
                        }
                        {
                            this.state.selected === 'Microsoft' || (!transcriptAvailable && !this.state.recording && this.state.selected === '')
                                ? <Button color={this.getCompanyStyle('Microsoft')} onClick={this.select.bind(this, 'Microsoft')}>Microsoft</Button>
                                : <Button disabled>Microsoft</Button>
                        }
                        {
                            this.state.selected === 'Google' || (!transcriptAvailable && !this.state.recording && this.state.selected === '')
                                ? <Button color={this.getCompanyStyle('Google')} onClick={this.select.bind(this, 'Google')}>Google</Button>
                                : <Button disabled>Google</Button>
                        }
                        {
                            this.state.selected === 'Facebook' || (!transcriptAvailable && !this.state.recording && this.state.selected === '')
                                ? <Button color={this.getCompanyStyle('Facebook')} onClick={this.select.bind(this, 'Facebook')}>Facebook</Button>
                                : <Button disabled>Facebook</Button>
                        }
                    </div>
                    <br />
                    <div style={{ alignSelf: 'center', display: 'flex', flexDirection: 'column' }}>
                        <Button style={{ alignSelf: 'center' }} onClick={this.toggleRecording.bind(this)}> {!this.state.recording ? "Start Recording" : "Stop Recording"} </Button>
                        <h2 style={{ alignSelf: 'center' }}> {this.state.time} </h2>
                        <div style={{ color: 'grey', height: '40px' }}> {this.state.interimResult}</div>
                        <div>
                            {this.state.finalTranscript.map((line, index) => (
                                <div key={index}> {line} </div>
                            )
                            )}
                        </div>
                    </div>
                    <div style={{ alignSelf: '' }}>
                        {
                            transcriptAvailable && !this.state.recording ? <Button onClick={this.analyzePitch.bind(this)}> Analyze Pitch Attempt </Button> : null
                        }
                    </div>
                </CardBody>
            </Card>
        );

    }
}

export default withRouter(withStyles(style)(RecordingStudio));
