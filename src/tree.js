import React, {Component} from 'react';
import SortableTree from 'react-sortable-tree';
import 'react-sortable-tree/style.css';

export default class Tree extends Component {

  constructor(props){
    super(props);
    this.state = {
      treeData: [{title: 'Tencent',children:[{title: 'ecs_regular'}]}]
      // treeData: thedata
    };

  }


  render(){
    // return <h1>Hello, world</h1>;
    return (
      <div style={{height:400}}>
        <SortableTree
          treeData = {this.state.treeData}
          onChange = {treeData => this.setState({treeData})}
        />
      </div>
    )
  }
}

