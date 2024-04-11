import React,{useEffect, useState} from "react";
import { LineChart } from '@mui/x-charts/LineChart';


// Importing constant
import {APP} from '../constant/variable';

const Chart = () => {
    const [data, setData]=useState([]);

    useEffect(()=>{
        _loadData();
    },[])

    const _extractTimeFromString =(dateTimeString)=> {
        const dateTime = new Date(dateTimeString);
        const hour = dateTime.getHours().toString().padStart(2, '0');
        const minute = dateTime.getMinutes().toString().padStart(2, '0');
        const timeString = `${hour}.${minute}`;
        return timeString;
    }

    
    const _loadData = () => {
        fetch(`${APP.BASE_URL}/gas-prices/`).then((res) => res.json()).then((data) => { setData(data); });
    }
    return (
        <LineChart
        xAxis={[{ data:  data.map((value)=> _extractTimeFromString(value.timestamp)) }]}
        series={[
            {
                data: data.map((value)=> value.price),
            },
        ]}
        width={600}
        height={600}
    />
    )
}

export default Chart;