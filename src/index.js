import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import Tree from './tree';
import registerServiceWorker from './registerServiceWorker';
import 'react-sortable-tree/style.css';
import 'jsoneditor/dist/jsoneditor.min.css';
import './index.css';

ReactDOM.render(<Tree />, document.getElementById('root'));
registerServiceWorker();
