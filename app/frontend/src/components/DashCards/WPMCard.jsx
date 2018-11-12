import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class WPMCard extends Component {
    render() {
        const { classes, wpm } = this.props;

        let color = 'rose';

        if (typeof(wpm) === 'number') {
            color = wpm > 90 && wpm < 130 ? 'success' : 'danger';
        }

        return (
            <Card>
                <CardHeader color="success" stats icon>
                    <CardIcon color={color}>
                        <Icon>watch_later</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>Words per minute</p>
                    <h3 className={classes.cardTitle}>
                        {wpm}
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
