import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";

export default class TranscriptionCard extends Component {
  render() {
    const { transcription, classes } = this.props;

    return (
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
    )
  }
}
