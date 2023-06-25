import { useState } from "react";
import BarPlot from "../../components/BarChart";
import {DefaultRequest} from "../../services/requests";

function GamesByCountry() {



  const gdata = [
    { name: 'Category 1', value: 10 },
    { name: 'Category 2', value: 20 },
    { name: 'Category 3', value: 15 },
    { name: 'Category 4', value: 5 },
  ];

  const { data, isLoading } = DefaultRequest<any>({
    url: `http://127.0.0.1:5000/players_by_country`,
  });


  const refData = [
    { name: 'Category 1', value: 10 },
    { name: 'Category 2', value: 20 },
    { name: 'Category 3', value: 15 },
    { name: 'Category 4', value: 5 },
  ];
  if (isLoading) {
    return <>loading</>;
  }

  if (data) {

    console.log("Data", data.count_by_country)
    return (
  <div>
    <div className="App">
      <h1>Jogadores por pais</h1>
      <BarPlot data={data.count_by_country} />
    </div>

  </div>
    );
  }


}

export default GamesByCountry;
