import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class StopWordsCard extends Component {
  render() {
    const { classes } = this.props;

    return (
      <Card>
        <CardHeader color="danger" stats icon>
          <CardIcon color="danger">
            <Icon>warning</Icon>
          </CardIcon>
          <p className={classes.cardCategory}>Number of Expletives</p>
          <h3 className={classes.cardTitle}>
            {this.props.explitives} <small>curses</small>
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
