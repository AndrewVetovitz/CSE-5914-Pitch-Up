import React from "react";
import PropTypes from "prop-types";
import {withRouter} from 'react-router-dom'

// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Mic from "@material-ui/icons/Mic";
// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Table from "components/Table/Table.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Button from "components/CustomButtons/Button.jsx"

import {
  dailySalesChart,
  emailsSubscriptionChart,
  completedTasksChart
} from "variables/charts";

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

class Pitch extends React.Component {
  state = {
    value: 0
  };
  goToStudio() {
    this.props.history.push('/recording')
  }
  handleChange = (event, value) => {
    this.setState({ value });
  };

  handleChangeIndex = index => {
    this.setState({ value: index });
  };
  render() {
    const { classes } = this.props;
    return (
      <div>
        <GridContainer>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="warning" stats icon>
                <CardIcon color="warning">
                  <Icon>content_copy</Icon>
                </CardIcon>
                <p className={classes.cardCategory}>Knowledge Base</p>
                <h3 className={classes.cardTitle}>
                  2/5 <small>Docs</small>
                </h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                    <Button>Upload Document</Button>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
          <GridItem xs={12} sm={6} md={3}>
            <Card>
              <CardHeader color="success" stats icon>
                <CardIcon color="success">
                  <Mic />
                </CardIcon>
                <p className={classes.cardCategory}>Recording Studio</p>
                <h3 className={classes.cardTitle}>Record Pitch</h3>
              </CardHeader>
              <CardFooter stats>
                <div className={classes.stats}>
                    <Button onClick={this.goToStudio.bind(this)}>Record Pitch Attempt</Button>
                </div>
              </CardFooter>
            </Card>
          </GridItem>
        </GridContainer>
        <GridContainer>
          <GridItem xs={12} sm={12} md={6}>
            <Card>
              <CardHeader color="warning">
                <h4 className={classes.cardTitleWhite}>Pitch Attempts</h4>
                <p className={classes.cardCategoryWhite}>
                  All Pitch Attempts on Record
                </p>
              </CardHeader>
              <CardBody>
                <Table
                  tableHeaderColor="warning"
                  tableHead={["Attempt #", "Date", "Duration", "Results"]}
                  tableData={[
                    ["1", "9/25/2018 2:30pm", "45s", "View Results"],
                    ["2", "9/25/2018 3:00pm", "50s", "View Results"],
                    ["3", "9/25/2018 3:05pm", "85s", "View Results"],
                    ["4", "9/26/2018 3:10pm", "87s", "View Results"]
                  ]}
                />
              </CardBody>
            </Card>
          </GridItem>
        </GridContainer>
      </div>
    );
  }
}

Pitch.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withRouter(withStyles(dashboardStyle)(Pitch));
