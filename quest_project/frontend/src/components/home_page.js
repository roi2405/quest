import React, { Component } from "react";
import UserPage from "./user_page";
import QuestionPage from "./question_page";
import CreateUserPage from "./create_user_page";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                    <Routes>
                        <Route path='/user-1' element={<UserPage />}/>
                        <Route path='/create-user' element={<CreateUserPage />}/>
                        <Route path='/question-1' element={<QuestionPage />}/>
                        <Route path='/' element={<p> This is the Home Page </p>}/>
                    </Routes>
            </Router>
        )
    }
}
