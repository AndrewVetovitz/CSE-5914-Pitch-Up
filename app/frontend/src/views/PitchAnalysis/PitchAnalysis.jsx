import React from "react";
import PropTypes from "prop-types";
// react plugin for creating charts
import ChartistGraph from "react-chartist";
// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Store from "@material-ui/icons/Store";
import Warning from "@material-ui/icons/Warning";
import DateRange from "@material-ui/icons/DateRange";
import LocalOffer from "@material-ui/icons/LocalOffer";
import Update from "@material-ui/icons/Update";
import ArrowUpward from "@material-ui/icons/ArrowUpward";
import AccessTime from "@material-ui/icons/AccessTime";
import Accessibility from "@material-ui/icons/Accessibility";
import BugReport from "@material-ui/icons/BugReport";
import Code from "@material-ui/icons/Code";
import Cloud from "@material-ui/icons/Cloud";
import Mic from "@material-ui/icons/Mic";
// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Table from "components/Table/Table.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Button from "components/CustomButtons/Button.jsx"

import { bugs, website, server } from "variables/general";

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "variables/charts";

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

class PitchAnalysis extends React.Component {
    state = {
        pitch_try: {
            transcript: '',
            duration: 0,
            analysis_concepts: {},
            analysis_words: {
                explitives: '',
                stop_words: ''
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
                    stop_words: null
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

                console.log(this.state);
        })
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
    
    const duration = pitch_try.duration;
    const words_per_minute = pitch_try.words_per_minute;
    const stop_words = pitch_try.analysis_words.stop_words;
    const explitives = pitch_try.analysis_words.explitives;
    const transcription = pitch_try.transcription;

    return (
      <div>
        <GridContainer>

          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="warning" stats icon>
                <CardIcon color="warning">
                  <Icon>content_copy</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Total Stop Words</p>
                <h3 className={classes.cardTitle}>
                  {stop_words}
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                </div>
              </CardFooter>
            </Card>
          </GridItem>

          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="danger" stats icon>
                <CardIcon color="danger">
                  <Icon>warning</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Number of Expletives</p>
                <h3 className={classes.cardTitle}>
                    {explitives} <small>curses</small>
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                </div>
              </CardFooter>
            </Card>
          </GridItem>

          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="success" stats icon>
                <CardIcon color="success">
                  <Icon>watch_later</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Pitch Duration</p>
                <h3 className={classes.cardTitle}>
                  {duration} <small>sec</small>
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                </div>
              </CardFooter>
            </Card>
          </GridItem>

        <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="success" stats icon>
                <CardIcon color="success">
                  <Icon>watch_later</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Words per minute</p>
                <h3 className={classes.cardTitle}>
                  {words_per_minute}
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                </div>
              </CardFooter>
            </Card>
          </GridItem>

        </GridContainer>
        <GridContainer>
          <GridItem xs={12} sm={12} md={6}>
            <Card>
              <CardHeader color="warning">
                <h4 className={classes.cardTitleWhite}>Pitch Transcription</h4>
                <p className={classes.cardCategoryWhite}>
                  Complete Transcription of Your Pitch
                </p>
              </CardHeader>
              <CardBody>
                <p>
                {transcription}
                </p>
              </CardBody>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={12} md={6}>
            <Card>
              <CardHeader color="warning">
                <h4 className={classes.cardTitleWhite}>Raw JSON</h4>
                <p className={classes.cardCategoryWhite}>
                  Raw analysis from our model
               </p>
              </CardHeader>
              <CardBody>
                <p> 
                  {JSON.stringify(pitch_try, null, 4)}
                </p>
              </CardBody>
            </Card>
          </GridItem>
        </GridContainer>
      </div>
    );
  }
}

PitchAnalysis.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(dashboardStyle)(PitchAnalysis);
