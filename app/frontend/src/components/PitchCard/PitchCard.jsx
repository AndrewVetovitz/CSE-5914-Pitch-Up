import React from "react";
import {withRouter} from 'react-router-dom'

// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";

// core components
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Button from "components/CustomButtons/Button.jsx"

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";


class PitchCard extends React.Component {
    viewPitch() {
        this.props.history.push('/pitch')
    }

    render() {
        const { classes } = this.props;
        return (
            <Card>
                <CardHeader color="danger" stats icon>
                    <CardIcon color="danger">
                    <Icon>favorite</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>Elevator Pitch</p>
                    <h4 className={classes.cardTitle}>
                    Kitten Mittenz
                    </h4>
                </CardHeader>
                <CardFooter stats>
                    <Button onClick={this.viewPitch.bind(this)}>View Pitch</Button>
                </CardFooter>
            </Card>
        );
    } 
}

export default withRouter(withStyles(dashboardStyle)(PitchCard));
