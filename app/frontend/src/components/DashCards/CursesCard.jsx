import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class StopWordsCard extends Component {
    render() {
        const { classes, explitives } = this.props;

        let color = 'rose';

        if (typeof(explitives) === 'number') {
            color = explitives === 0 ? 'success' : 'danger';
        }

        return (
            <Card>
                <CardHeader color="danger" stats icon>
                    <CardIcon color={color}>
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
        )
    }
}
