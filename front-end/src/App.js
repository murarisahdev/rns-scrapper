import React from 'react';
import { Tabs } from 'antd';
import TableView from './components/table';

const { TabPane } = Tabs;

function App() {
  const _handleChange = (key) => {
    console.log(key);
  };

  return (
    <div style={{ marginLeft: 20 }}>
      <Tabs defaultActiveKey="1" onChange={_handleChange}>
        <TabPane tab="Table" key="1">
         <TableView/>
        </TabPane>
      </Tabs>
    </div>
  );
}

export default App;
