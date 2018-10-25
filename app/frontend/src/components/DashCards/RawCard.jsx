





import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";

export default class RawCard extends Component {
  render() {
    const { json, classes } = this.props;

    return (
        <Card>
            <CardHeader color="warning">
                <h4 className={classes.cardTitleWhite}>Raw JSON</h4>
                <p className={classes.cardCategoryWhite}>
                    Raw analysis from our model
                </p>
            </CardHeader>
            <CardBody>
                <p>
                    {JSON.stringify(json, null, 4)}
                </p>
            </CardBody>
        </Card>
    )
  }
}
