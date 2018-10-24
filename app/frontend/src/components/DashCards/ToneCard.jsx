import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";

export default class ToneCard extends Component {
  render() {
    const { tone, classes } = this.props;

    const tone_sentence = [];

    if (tone !== null && tone['sentences_tone'] !== undefined) {
        tone['sentences_tone'].forEach((sent, index) => {
            if(sent['tones'].length === 0){
                tone_sentence.push(<span key={index}>{sent['text'] + ' '}</span>);
            } else {
                switch(sent['tones'][0]['tone_name']){
                    case 'Anger': {
                        tone_sentence.push(<span style={{color: 'red'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Fear': {
                        tone_sentence.push(<span style={{color: 'green'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Joy': {
                        tone_sentence.push(<span style={{color: 'yellow'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Sadness': {
                        tone_sentence.push(<span style={{color: 'orange'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Analytical': {
                        tone_sentence.push(<span style={{color: 'blue'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Confident': {
                        tone_sentence.push(<span style={{color: 'purple'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    case 'Tentative': {
                        tone_sentence.push(<span style={{color: 'blue'}} key={index}>{sent['text'] + ' '}</span>);
                        break;
                    }
                    default: {
                        tone_sentence.push(<span key={index}>{sent['text'] + ' '}</span>);
                        console.log('Unknown');
                    }
                }
            }

        });
    }

    return (
        <Card>
            <CardHeader color="warning">
                <h4 className={classes.cardTitleWhite}>Tone Analysis</h4>
                <p className={classes.cardCategoryWhite}>
                    Tone Anaylsis of pitch
                </p>
            </CardHeader>
            <CardBody>
                <p>
                    {tone_sentence}
                </p>
            </CardBody>
        </Card>
    )
  }
}
