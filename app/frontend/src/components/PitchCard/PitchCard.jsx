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
    constructor(props) {
        super(props);
        this.viewPitch = this.viewPitch.bind(this);
        this.deletePitch = this.props.delete.bind(this);
    }
    
    viewPitch(id) {
        this.props.history.push('/pitch#' + id)
    }

    render() {
        const { classes, name, id } = this.props;
        return (
            <Card>
                <CardHeader color="danger" stats icon>
                    <CardIcon color="danger">
                    <Icon>favorite</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>Elevator Pitch</p>
                    <h4 className={classes.cardTitle}>
                    {name}
                    </h4>
                </CardHeader>
                <CardFooter stats>
                    <Button onClick={() => {this.viewPitch(id)}}>View Pitch</Button>
                    <Button onClick={() => {this.deletePitch(id)}}>Delete</Button>
                </CardFooter>
            </Card>
        );
    } 
}

export default withRouter(withStyles(dashboardStyle)(PitchCard));
