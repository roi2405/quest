import React, { Component } from "react";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import { Link } from "react-router-dom";

export default class CreateUserPage extends Component
{
    constructor(props) 
    {
        super(props);
        this.state = 
        {
          name: "",
        };
    }

    on_user_name_change = (e) => {this.setState({name: e.target.value});}

    create_user_button_pressed = () => 
    {
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: this.state.name,
          }),
        };
        fetch("/api/create-user", requestOptions)
          .then((response) => response.json())
          .then((data) => console.log(this.state));
    }

      render() 
    {
        return (
          <Grid container spacing={1}>
            <Grid item xs={12} align="center">
              <Typography component="h4" variant="h4">
                Create A User
              </Typography>
            </Grid>
            <Grid item xs={12} align="center">
              <FormControl>
                <TextField
                  required={true}
                  onChange={this.on_user_name_change}
                  defaultValue={""}
                  inputProps={{
                    style: { textAlign: "center" },
                  }}
                />
              </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
              <Button
                color="primary"
                variant="contained"
                onClick={this.create_user_button_pressed}
              >
                Create A User
              </Button>
            </Grid>
            <Grid item xs={12} align="center">
              <Button color="secondary" variant="contained" to="/" component={Link}>
                Back
              </Button>
            </Grid>
          </Grid>
        );
    }
}