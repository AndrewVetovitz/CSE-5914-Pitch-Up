import React from "react";
import PropTypes from "prop-types";
import { withRouter } from 'react-router-dom'

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

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

class Pitch extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleClick = this.handleClick.bind(this);
        this.filesInput = React.createRef();
    }

    state = {
        value: 0,
        pitch_tries: [],
        topics: [],
        uploadInProgress: false
    };

    componentDidMount() {
        this.mounted = true;

        this.fetchPitchTries().then((json) => {
            let pitchTries = json.pitches.map((pitchTry) =>
                [
                    '' + pitchTry.id,
                    "Yesterday",
                    '' + pitchTry.duration + 's',
                    <Button onClick={() => this.handleClick(pitchTry.id)}>View Results</Button>,
                    <Button onClick={() => this.delete(pitchTry.id)}>Delete</Button>
                ]
            );

            if (this.mounted) {
                this.setState({
                    pitch_tries: pitchTries
                });
            }
        });

        this.fetchDocuments().then(json => {
            if (json && json['pitch'] && json['pitch']['content_analysis'] && json['pitch']['content_analysis']['related_concepts']) {
                const concepts = json['pitch']['content_analysis']['related_concepts'];

                let conceptArray;

                try {
                    conceptArray = JSON.parse(concepts);
                } catch (err) {
                    conceptArray = concepts;
                }

                const temp = []

                if (conceptArray.length > 0) {
                    for (let i = 0; i < conceptArray.length && i < 3; i++) {
                        temp.push(conceptArray[i]);
                        temp.push(<br key={i} />);
                    }

                    if (this.mounted) {
                        this.setState({
                            topics: temp
                        });
                    }
                }
            }
        });
    }

    componentWillUnmount() {
        this.mounted = false;
    }

    handleClick = id => {
        this.props.history.push('/pitch_analysis#' + id);
    }

    delete = id => {
        fetch('http://localhost:5000/pitch_try/delete/' + this.getPitchId() + '/' + id)
            .then(resp => resp.ok)
            .then(() => {
                this.setState({
                    pitch_tries: this.state.pitch_tries.filter(item => {
                        return Number(item[0]) !== id;
                    })
                });
            });
    }

    fetchDocuments() {
        return fetch('http://localhost:5000/pitch/' + this.getPitchId()).then((resp) => resp.json());
    }

    fetchPitchTries() {
        return fetch('http://localhost:5000/pitch/' + this.getPitchId() + '/pitch_tries').then((resp) => resp.json());
    }

    goToStudio() {
        let pitch_id = this.getPitchId()
        this.props.history.push('/recording#' + pitch_id)
    };

    handleChange = (event, value) => {
        this.setState({ value });
    };

    getPitchId() {
        let hashProps = this.props.location.hash.split('#')
        let pitchId = 13371337

        if (hashProps.length > 1) {
            pitchId = hashProps[1]
        }

        return pitchId
    }

    handleSubmit(event) {
        event.preventDefault();
        var pitch_id = this.getPitchId();

        const data = new FormData();

        for (const file of this.filesInput.current.files) {
            let ext = file.name.split(".").pop()
            if(ext !== "pdf"){
                alert("Failed To Upload " + file.name + " it's not a PDF")
            }
            data.append('files[]', file, file.name);
        }
        this.setState({uploadInProgress: true})
        return fetch('http://localhost:5000/pitch/' + pitch_id + '/upload', {
            method: 'POST',
            body: data,
            mode: 'no-cors'
        }).then((resp) => {
            this.filesInput.current.value = ''
            this.setState({uploadInProgress: false})
            // if(!resp.ok){
            //     alert("Document Upload Failed")
            // }
            // if(resp.status === 200){
            //     alert("Successful Document Upload!")
            // }
        })
    }

    handleChangeIndex = index => {
        this.setState({ value: index });
    };

    render() {
        const { classes } = this.props;
        return (
            <div>
                <GridContainer>
                    <GridItem xs={12} sm={6} md={6} lg={6}>
                        <Card>
                            <CardHeader color="success" stats icon>
                                <CardIcon color="success">
                                    <Icon>content_copy</Icon>
                                </CardIcon>
                                <p className={classes.cardCategory}>Knowledge Base</p>
                                <h3 className={classes.cardTitle} >
                                    {this.state.uploadInProgress ? "Uploading..." : "Upload Documents"}
                                </h3>
                            </CardHeader>
                            <CardFooter stats>
                                <form onSubmit={this.handleSubmit}>
                                    <GridContainer>
                                        <GridItem sm={6}>
                                            <div className={classes.fileUploadDiv}>
                                                <label>
                                                    <input type="file" ref={this.filesInput} multiple required name="files" accept="application/pdf" />
                                                </label>
                                            </div>
                                        </GridItem>
                                        <GridItem sm={6}>
                                            <Button type="submit">Upload Files</Button>
                                        </GridItem>
                                    </GridContainer>
                                </form>
                            </CardFooter>
                        </Card>
                    </GridItem>
                    <GridItem xs={12} sm={6} md={6} lg={6}>
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
                    <GridItem xs={12} sm={12} md={12}>
                        <Card>
                            <CardHeader color="success">
                                <h4 className={classes.cardTitleWhite}>Pitch Concepts</h4>
                                <p className={classes.cardCategoryWhite}>
                                    Related topics from documents
                                </p>
                            </CardHeader>
                            <CardBody>
                                {this.state.topics}
                            </CardBody>
                        </Card>
                    </GridItem>
                </GridContainer>

                <GridContainer>
                    <GridItem xs={12} sm={12} md={12}>
                        <Card>
                            <CardHeader color="success">
                                <h4 className={classes.cardTitleWhite}>Pitch Attempts</h4>
                                <p className={classes.cardCategoryWhite}>
                                    All Pitch Attempts on Record
                                </p>
                            </CardHeader>
                            <CardBody>
                                <Table
                                    tableHeaderColor="warning"
                                    tableHead={["Attempt #", "Date", "Duration", "Results", "Delete"]}
                                    tableData={this.state.pitch_tries}
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
