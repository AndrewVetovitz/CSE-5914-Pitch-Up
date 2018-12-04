import React, { Component } from 'react'
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Icon from "@material-ui/core/Icon";

export default class ContainsNameCard extends Component {
    render() {
        const { classes, company, score } = this.props;
        
        let title = '';

        if(company === '' || company === null){
            title = 'No companies compared to speech';
        } else {
            title = 'Company Similarity Score for ' + company; 
        }

        let content = '';
        let color = 'rose';
        const threshold = 3;

        if (typeof score === 'number' && company !== '') {
            content = score;
            color = score < threshold ? 'danger' : 'success';
        }

        return (
            <Card>
                <CardHeader color="success" stats icon>
                    <CardIcon color={color}>
                        <Icon>watch_later</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>{title}</p>
                    <h3 className={classes.cardTitle}>
                        {content}
                    </h3>
                </CardHeader>
                <CardFooter stats>
                    <div className={classes.stats}></div>
                </CardFooter>
            </Card>
        )
    }
}
