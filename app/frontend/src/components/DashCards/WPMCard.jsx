import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class WPMCard extends Component {
  render() {
    const { classes } = this.props;

    return (
    <Card>
      <CardHeader color="success" stats icon>
        <CardIcon color="success">
          <Icon>watch_later</Icon>
        </CardIcon>
        <p className={classes.cardCategory}>Words per minute</p>
        <h3 className={classes.cardTitle}>
          {this.props.wpm}
        </h3>
      </CardHeader>
      <CardFooter stats>
        <div className={classes.stats}>
        </div>
      </CardFooter>
    </Card>
  )
  }
}
