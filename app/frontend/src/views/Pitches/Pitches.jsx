import React from "react";

// @material-ui/core
import withStyles from "@material-ui/core/styles/withStyles";
import Icon from "@material-ui/core/Icon";
import Modal from '@material-ui/core/Modal';
import TextField from '@material-ui/core/TextField';

// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardIcon from "components/Card/CardIcon.jsx";
import CardFooter from "components/Card/CardFooter.jsx";
import Button from "components/CustomButtons/Button.jsx"
import PitchCard from "components/PitchCard/PitchCard.jsx"

import dashboardStyle from "assets/jss/material-dashboard-react/views/dashboardStyle.jsx";

const modalStyle = {
  width: '300px',
  backgroundColor: 'white',
  top: '50%',
  left: '50%',
  position: 'absolute',
  padding: '25px'
}

class Pitches extends React.Component {
  constructor(props){
    super(props);
    this.showModal = this.showModal.bind(this)
    this.closeModal = this.closeModal.bind(this)
    this.createPitch = this.createPitch.bind(this)
    this.handleTextInput = this.handleTextInput.bind(this)
    this.state = {
      showModal: false,
      newPitchName: '',
      pitches: []
    }
  }
  
  componentDidMount() {
    this.fetchPitches()
  }

  showModal() {
    this.setState({showModal: true})
  }

  closeModal() {
    this.setState({showModal: false})
  }

  handleTextInput(e) {
    this.setState({
      newPitchName: e.target.value
    })
  }

  fetchPitches(){
    fetch('http://localhost:5000/user/1/pitches').then((resp) => {
      if(!resp.ok){
        let dummyPitches = {
          pitches: [
          ]
        }
        return dummyPitches
      }
      return resp.json()
    }).then((json) => {
      this.setState({
        showModal: false,
        pitches: json.pitches
      })
    })
  }

  createPitch() {
    // TODO: Prevent ppl from not using a name like a dingus
    let pitchName = this.state.newPitchName
    fetch('http://localhost:5000/user/1/new_pitch', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({name: pitchName})
    }).then((resp) => {
      if(!resp.ok){
        throw Error("ruh roh")
      }
      this.fetchPitches()
    })
  }

  render() {
    const { classes } = this.props;
    let pitches = this.state.pitches
    let pitchCards = pitches.map((p, i) => 
      <GridItem key={i} xs={12} sm={6} md={3}>
        <PitchCard name={p.name} id={p.id}/>
      </GridItem>
    )

    return (
        <div>
            <GridContainer>
                {pitchCards}
                <GridItem xs={12} sm={6} md={3}>
                <Card>
                    <CardHeader color="success" stats icon>
                    <CardIcon color="success">
                        <Icon>create</Icon>
                    </CardIcon>
                    <p className={classes.cardCategory}>New Pitch</p>
                    <h4 className={classes.cardTitle}>
                        Create A Pitch
                    </h4>
                    </CardHeader>
                    <CardFooter stats>
                    <div className={classes.stats}>
                        <Button onClick={this.showModal}>Create Pitch</Button>
                    </div>
                    </CardFooter>
                </Card>
                </GridItem>
            </GridContainer>
            <Modal open={this.state.showModal} onClose={this.closeModal}> 
                <div style={modalStyle}>
                <h5 variant="h6" id="modal-title">
                    Create a Pitch
                </h5>
                <TextField
                id="pitchNameTextField"
                label="Pitch Name"
                onChange={this.handleTextInput}
                placeholder="Enter Your Pitch Name"
                className={classes.textField}
                margin="normal"
                variant="outlined"
                />
                <Button onClick={this.createPitch}>Create</Button>  
                </div>
            </Modal>
        </div>
    ); 
  }
}

export default withStyles(dashboardStyle)(Pitches);
