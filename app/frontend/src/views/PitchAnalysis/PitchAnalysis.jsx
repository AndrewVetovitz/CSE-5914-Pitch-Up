import React from "react";
import PropTypes from "prop-types";
// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import StopWordsCard from "components/DashCards/StopWordsCard.jsx";
import CursesCard from "components/DashCards/CursesCard.jsx";
import PitchDurationCard from "components/DashCards/PitchDurationCard.jsx";
import WPMCard from "components/DashCards/WPMCard.jsx";
import TranscriptionCard from "components/DashCards/TranscriptionCard.jsx";
import RawCard from "components/DashCards/RawCard.jsx";

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";
import ToneCard from "../../components/DashCards/ToneCard";

class PitchAnalysis extends React.Component {
    state = {
        pitch_try: {
            transcript: '',
            duration: 0,
            analysis_concepts: {},
            analysis_words: {
                explitives: '',
                stop_words: '',
                tone: ''
            },
            transcription: null,
            words_per_minute: 0
        }
    };

  componentDidMount() {
    const pitch_attempt_id = this.props.location.hash.split('#')[1]

    if(pitch_attempt_id === undefined){
        this.setState({
            pitch_try: {
                transcription: null,
                duration: null,
                analysis_concepts: {},
                analysis_words: {
                    explitives: null,
                    stop_words: null,
                    tone: null
                },
                words_per_minute: null  
            }
        })
    } else {
        fetch('http://localhost:5000/pitch_try/' + pitch_attempt_id).then((resp) => resp.json())
            .then((res_json) => {
                this.setState({
                    pitch_try: {
                        ...res_json.pitch_try
                    }
                });
        });
    }
  }

  handleChange = (event, value) => {
    this.setState({ value });
  };

  handleChangeIndex = index => {
    this.setState({ value: index });
  };

  render() {
    const { classes } = this.props;
    
    const pitch_try = this.state.pitch_try;    
    
    const { duration, words_per_minute, transcription } = pitch_try;
    const { stop_words, explitives, tone } = pitch_try.analysis_words;

    return (
      <React.Fragment>
        <GridContainer>
          <GridItem xs={12} sm={6} md={3}>
            <StopWordsCard stopWords={stop_words} classes={classes}/>
          </GridItem>

          <GridItem xs={12} sm={6} md={3}>
            <CursesCard explitives={explitives} classes={classes}/>
          </GridItem>

          <GridItem xs={12} sm={6} md={3}>
            <PitchDurationCard duration={duration} classes={classes}/>
          </GridItem>

          <GridItem xs={12} sm={6} md={3}>
            <WPMCard wpm={words_per_minute} classes={classes}/>
          </GridItem>

        </GridContainer>
        <GridContainer>
          <GridItem xs={12} sm={12} md={6}>
            <TranscriptionCard transcription={transcription} classes={classes}></TranscriptionCard>
          </GridItem>

          <GridItem xs={12} sm={12} md={6}>
            <ToneCard tone={tone} classes={classes}/>
          </GridItem>
          
          <GridItem xs={12} sm={12} md={6}>
            <RawCard json={pitch_try} classes={classes}/>
          </GridItem>
        </GridContainer>
      </React.Fragment>
    );
  }
}

PitchAnalysis.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(PitchAnalysis);
