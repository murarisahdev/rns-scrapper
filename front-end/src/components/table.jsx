import React, { useState, useEffect } from 'react';
import { Table } from 'antd';

// Importing constant
import {APP} from '../constant/variable';

const columns = [
    {
        title: 'id',
        dataIndex: 'id',
        key: 'id',
    },
    {
        title: 'price',
        dataIndex: 'price',
        key: 'price',
    },
    {
        title: 'timestamp',
        dataIndex: 'timestamp',
        key: 'timestamp',
    },
];

const TableView = () => {
     const [data,setData]= useState([]);

    useEffect(() => {
        _loadData();
    }, [])


    const _loadData = () => {
        fetch(`${APP.BASE_URL}/gas-prices/`).then((res) => res.json()).then((data) => { setData(data); });
    }


    return (
        <div>
            <Table dataSource={data} columns={columns} />
        </div>
    );
};

export default TableView;
