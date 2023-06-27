import BarPlot from "../../components/BarChart";
import { DefaultRequest } from "../../services/requests";
import Table from "../../components/Table";

interface Partida {
  jogador_primario: number;
  jogador_secundario: number;
  jogador_primario_nome: string;
  jogador_secundario_nome: string;
  arbitro: number;
  arbitro_nome: string;
  pecas_pretas: number;
  pecas_brancas: number;
  data_inicio: string;
  data_fim: string;
  vencedor: string;
  chave_campeonato: number;
  campeonato: string;
  chave_salao: number;
  salao: {
    id: number;
    capacidade: number;
    radio: string;
    televisao: string;
    video: string;
    internet: string;
    inicio_uso: string;
    fim_uso: string;
    nome: string;
    chave_hospedagem: number;
    hospedagem: {
      id: number;
      nome: string;
      cod_postal: number;
      endereco: string;
      nacao_id: number;
      nacao: string;
    };
  };
  numero_jogadas: number;
}

interface Partida_Normalizada {
  jogador_primario_nome: string;
  jogador_secundario_nome: string;
  arbitro_nome: string;
  data_inicio: string;
  data_fim: string;
  vencedor: string;
  campeonato: string;
  salao_nome: string;
  nome_hotel: string;
  cod_postal: number;
  endereco: string;
  nacao: string;
  numero_jogadas: number;
}

function convertObject(obj: Partida): Partida_Normalizada {
  const convertedObj: Partida_Normalizada = {
    jogador_primario_nome: obj.jogador_primario_nome,
    jogador_secundario_nome: obj.jogador_secundario_nome,
    arbitro_nome: obj.arbitro_nome,
    data_inicio: obj.data_inicio,
    data_fim: obj.data_fim,
    vencedor: obj.vencedor,
    campeonato: obj.campeonato,
    salao_nome: obj.salao.nome,
    nome_hotel: obj.salao.hospedagem.nome,
    cod_postal: obj.salao.hospedagem.cod_postal,
    endereco: obj.salao.hospedagem.endereco,
    nacao: obj.salao.hospedagem.nacao,
    numero_jogadas: obj.numero_jogadas,
  };
  return convertedObj;
}

function GamesByRounds() {
  const { data, isLoading } = DefaultRequest<any>({
    url: `http://127.0.0.1:5000/programacao`,
  });

  if (isLoading) {
    return <>loading</>;
  }

  if (data) {
    console.log("Data here -> ", data);


    // const convertedObj: Partida_Normalizada = convertObject(obj);
    const modifiedObj = data.map(convertObject);
    console.log("Here stay ->",modifiedObj);

    return (
      <div>
        <div className="App">
          <h1>Jogadores por pais</h1>
          {/* <BarPlot data={data.count_by_country} />

          <Table
            data={data.count_by_country}
            columns={columns}
            searchKey="name"
          /> */}
        </div>
      </div>
    );
  }
}

export default GamesByRounds;
