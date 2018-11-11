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
import ToneCard from "../../components/DashCards/ToneCard";
import ContainsNameCard from "../../components/DashCards/ContainsNameCard";

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

class PitchAnalysis extends React.Component {
    state = {
        transcript: '',
        duration: 0,
        analysis_concepts: {},
        analysis_words: {
            explitives: '',
            stop_words: '',
            tone: '',
            contains_name: ''
        },
        transcription: null,
        words_per_minute: 0
    };

  componentDidMount() {
    const pitch_attempt_id = this.props.location.hash.split('#')[1]

    if(pitch_attempt_id === undefined){
        this.setState({
            transcription: null,
            duration: null,
            analysis_concepts: {},
            analysis_words: {
                explitives: null,
                stop_words: null,
                tone: null,
                contains_name: null
            },
            words_per_minute: null  
        })
    } else {
        fetch('http://localhost:5000/pitch_try/' + pitch_attempt_id).then((resp) => resp.json())
            .then((res_json) => {
                this.setState({
                    ...res_json
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
    
    const { duration, words_per_minute, transcription } = this.state;
    const { stop_words, explitives, tone, contains_name } = this.state.analysis_words;

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
          <GridItem xs={12} sm={6} md={3}>
            <ContainsNameCard truth={contains_name} classes={classes}></ContainsNameCard>
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
            <RawCard json={this.state} classes={classes}/>
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
