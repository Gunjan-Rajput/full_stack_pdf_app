import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UploadPage from './pages/UploadPage';
import QuestionPage from './pages/QuestionPage';

const App = () => {
    return (
        <Router>
            <Switch>
                <Route path="/upload" component={UploadPage} />
                <Route path="/ask" component={QuestionPage} />
            </Switch>
        </Router>
    );
};

export default App;
