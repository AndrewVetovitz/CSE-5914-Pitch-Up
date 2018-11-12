import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class PitchDurationCard extends Component {
    render() {
        const { classes, duration } = this.props;

        let color = 'rose';

        if (typeof(duration) === 'number') {
            color = duration > 15 && duration < 60 ? 'success' : 'danger';
        }

        return (
            <Card>
                <CardHeader color="success" stats icon>
                    <CardIcon color={color}>
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
        )
    }
}
