import React from "react";
import { Link } from 'react-router-dom'

// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";

// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Button from "components/CustomButtons/Button.jsx"
import PitchCard from "components/PitchCard/PitchCard.jsx"

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";


function Pitches(props) {
  const { classes } = props;
  return (
    <div>
    <GridContainer>
      <GridItem xs={12} sm={6} md={3}>
        <PitchCard/>
      </GridItem>
      <GridItem xs={12} sm={6} md={3}>
        <Card>
          <CardHeader color="success" stats icon>
            <CardIcon color="success">
              <Icon>create</Icon>
            </CardIcon>
            <p className={classes.cardCategory}>New Pitch</p>
            <h4 className={classes.cardTitle}>
              Create A Pitch
            </h4>
          </CardHeader>
          <CardFooter stats>
            <div className={classes.stats}>
              <Button>Create Pitch</Button>
            </div>
          </CardFooter>
        </Card>
      </GridItem>

    </GridContainer>
  </div>
);
}

export default withStyles(dashboardStyle)(Pitches);
