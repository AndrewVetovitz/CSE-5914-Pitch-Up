import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class StopWordsCard extends Component {
    render() {
        const { classes, stopWords } = this.props;

        let color = 'rose';

        if (typeof(stopWords) === 'number') {
            color = stopWords < 5 ? 'success' : 'danger';
        }

        return (
            <Card>
                <CardHeader color="warning" stats icon>
                    <CardIcon color={color}>
                        <Icon>content_copy</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>Total Stop Words</p>
                    <h3 className={classes.cardTitle}>
                        {stopWords}
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
