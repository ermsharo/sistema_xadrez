import BarPlot from "../../components/BarChart";
import { DefaultRequest } from "../../services/requests";
import Table from "../../components/Table";

function GamesByCountry() {

  const { data, isLoading } = DefaultRequest<any>({
    url: `http://127.0.0.1:5000/players_by_country`,
  });

  if (isLoading) {
    return <>loading</>;
  }

  if (data) {
    console.log("Data", data.count_by_country);

    const columns = [
      { key: "name" as keyof (typeof data.count_by_country[0]), label: "Pais" },
      {
        key: "value" as keyof (typeof data.count_by_country[0]),
        label: "Quantidade",
      },

      // Add more columns as needed
    ];
    return (
      <div>
        <div className="App">
          <h1>Jogadores por pais</h1>
        
          <BarPlot data={data.count_by_country} />

          <Table
            data={data.count_by_country}
            columns={columns}
            searchKey="name"
          />
        </div>
      </div>
    );
  }
}

export default GamesByCountry;
