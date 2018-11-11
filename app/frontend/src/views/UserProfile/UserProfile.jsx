import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
import InputLabel from "@material-ui/core/InputLabel";
// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import CustomInput from "components/CustomInput/CustomInput.jsx";
import Button from "components/CustomButtons/Button.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";
import CardFooter from "components/Card/CardFooter.jsx";

const styles = {
    cardCategoryWhite: {
        color: "rgba(255,255,255,.62)",
        margin: "0",
        fontSize: "14px",
        marginTop: "0",
        marginBottom: "0"
    },
    cardTitleWhite: {
        color: "#FFFFFF",
        marginTop: "0px",
        minHeight: "auto",
        fontWeight: "300",
        fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
        marginBottom: "3px",
        textDecoration: "none"
    }
};

class UserProfile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            company: '',
            username: '',
            email: '',
            name: '',
            state: '',
            city: '',
            country: '',
            postal: '',
            bio: ''
        }
    }

    componentDidMount() {
        fetch('http://localhost:5000/user/1').then((resp) => resp.json())
            .then((res_json) => {
                this.setState({
                    ...res_json
                });
            });
    }

    updateUser() {
        fetch('http://localhost:5000/user/update', {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({id: 1, ...this.state})
          }).then((resp) => {
            if(!resp.ok){
              throw Error("ruh roh")
            }

            return resp.text();
          });
    }

    change(event, state) {
        if (state === 'f_name') {
            const l_name = this.state.name.split(' ')[1] || '';
            event.target.value = event.target.value + ' ' + l_name;
            state = 'name';
        }

        if (state === 'l_name') {
            const f_name = this.state.name.split(' ')[0] || '';
            event.target.value = f_name + ' ' + event.target.value;
            state = 'name';
        }

        this.setState({[state]: event.target.value});
    }

    render() {
        const { classes } = this.props;

        const { company, username, email, name, state, city, country, postal, bio } = this.state;

        const f_name = name.split(' ')[0] || '';
        const l_name = name.split(' ')[1] || '';

        return (
            <div>
                <GridContainer>
                    <GridItem xs={12} sm={12} md={12}>
                        <Card>
                            <CardHeader color="primary">
                                <h4 className={classes.cardTitleWhite}>Edit Profile</h4>
                                <p className={classes.cardCategoryWhite}>Complete your profile</p>
                            </CardHeader>
                            <CardBody>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={5}>
                                        <CustomInput
                                            labelText="Company"
                                            id="company"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "company"),
                                                value: company
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={3}>
                                        <CustomInput
                                            labelText="Username"
                                            id="username"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "username"),
                                                value: username
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Email address"
                                            id="email-address"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "email"),
                                                value: email
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={6}>
                                        <CustomInput
                                            labelText="First Name"
                                            id="first-name"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "f_name"),
                                                value: f_name
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={6}>
                                        <CustomInput
                                            labelText="Last Name"
                                            id="last-name"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "l_name"),
                                                value: l_name
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="City"
                                            id="city"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "city"),
                                                value: city
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Country"
                                            id="country"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "country"),
                                                value: country
                                            }}
                                        />
                                    </GridItem>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="Postal Code"
                                            id="postal-code"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "postal"),
                                                value: postal
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={4}>
                                        <CustomInput
                                            labelText="State"
                                            id="state"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "state"),
                                                value: state
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                                <GridContainer>
                                    <GridItem xs={12} sm={12} md={12}>
                                        <InputLabel style={{ color: "#AAAAAA" }}>About me</InputLabel>
                                        <CustomInput
                                            id="about-me"
                                            formControlProps={{
                                                fullWidth: true
                                            }}
                                            inputProps={{
                                                onChange: (event) => this.change(event, "bio"),
                                                multiline: true,
                                                rows: 5,
                                                value: bio
                                            }}
                                        />
                                    </GridItem>
                                </GridContainer>
                            </CardBody>
                            <CardFooter>
                                <Button onClick={() => this.updateUser()} color="primary">Update Profile</Button>
                            </CardFooter>
                        </Card>
                    </GridItem>
                </GridContainer>
            </div>
        );
    }
}

export default withStyles(styles)(UserProfile);
