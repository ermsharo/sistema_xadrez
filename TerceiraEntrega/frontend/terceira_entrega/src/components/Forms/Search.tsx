import { DefaultRequest } from "../../services/requests";
import Table from "../../components/Table";
import React, { useState } from "react";
import {
  Select,
  MenuItem,
  InputLabel,
  SelectChangeEvent,
} from "@mui/material";
import styled from "styled-components";
import { HotelData , Players ,Judges} from "./selectData";

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
  match_name: string;
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
    match_name: `${obj.jogador_primario_nome} vs ${obj.jogador_primario_nome} - ${obj.campeonato}`,
  };
  return convertedObj;
}

const options = [
  { value: "option1", label: "Option 1" },
  { value: "option2", label: "Option 2" },
  { value: "option3", label: "Option 3" },
];

const StyledInputRow = styled(InputLabel)`
  width: 100%;

  display: flex;
  justify-content: space-between;
  gap: 2rem;
  flex-direction: column;
`;

const StyledFormControl = styled.div`
  padding: 1rem;
`;

const StyledInputLabel = styled(InputLabel)``;

function GamesView() {
  const { data, isLoading } = DefaultRequest<any>({
    url: `http://127.0.0.1:5000/programacao`,
  });

  const [selection1, setSelection1] = useState("");
  const [selection2, setSelection2] = useState("");
  const [selection3, setSelection3] = useState("");

  const handleSelection1Change = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setSelection1(event.target.value);
  };

  const handleSelection2Change = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setSelection2(event.target.value);
  };

  const handleSelection3Change = (event: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setSelection3(event.target.value);
  };

  const [age, setAge] = useState("todos");
  const handleChange = (event: SelectChangeEvent) => {
    setAge(event.target.value);
  };

  if (isLoading) {
    return <>loading</>;
  }

  if (data) {
    console.log("Data here -> ", data);

    // const convertedObj: Partida_Normalizada = convertObject(obj);
    const partidas_noramalizadas = data.map(convertObject);
    console.log("Here stay ->", partidas_noramalizadas);

    const columns = [
      {
        key: "match_name" as keyof (typeof data.count_by_country)[0],
        label: "jogo",
      },
      {
        key: "jogador_primario_nome" as keyof (typeof data.count_by_country)[0],
        label: "Primeiro jogador",
      },
      {
        key: "jogador_secundario_nome" as keyof (typeof data.count_by_country)[0],
        label: "Segundo jogador",
      },
      {
        key: "arbitro_nome" as keyof (typeof data.count_by_country)[0],
        label: "Arbitro",
      },
      {
        key: "vencedor" as keyof (typeof data.count_by_country)[0],
        label: "Vencedor",
      },
      {
        key: "data_inicio" as keyof (typeof data.count_by_country)[0],
        label: "Hotel",
      },
      {
        key: "salao_nome" as keyof (typeof data.count_by_country)[0],
        label: "Salao",
      },
      {
        key: "endereco" as keyof (typeof data.count_by_country)[0],
        label: "Endereco",
      },
      {
        key: "nacao" as keyof (typeof data.count_by_country)[0],
        label: "Pais",
      },
      {
        key: "data_inicio" as keyof (typeof data.count_by_country)[0],
        label: "Inicio",
      },
      {
        key: "data_fim" as keyof (typeof data.count_by_country)[0],
        label: "Fim",
      },
      {
        key: "numero_jogadas" as keyof (typeof data.count_by_country)[0],
        label: "numero de jogadas",
      },

      // Add more columns as needed
    ];

    partidas_noramalizadas.sort(
      (a: { numero_jogadas: number }, b: { numero_jogadas: number }) => {
        return a.numero_jogadas - b.numero_jogadas;
      }
    );

    return (
      <div>
        <div className="App">
          <h1>Jogos por parametros </h1>

          <StyledInputRow>
            <StyledFormControl>
              <InputLabel id="demo-simple-select-autowidth-label">
                Hotel
              </InputLabel>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                value={age}
                onChange={handleChange}
                fullWidth
                label="Age"
              >
                <MenuItem value="">{age}</MenuItem>
                {HotelData.map((item, index) => (
                  <MenuItem value={item.id}>{item.nome}</MenuItem>
                ))}
              </Select>
            </StyledFormControl>
            <StyledFormControl>
              <InputLabel id="demo-simple-select-autowidth-label">
               Jogador
              </InputLabel>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                value={age}
                onChange={handleChange}
                fullWidth
                label="Age"
              >
                <MenuItem value="">{age}</MenuItem>
                {Players.map((item, index) => (
                  <MenuItem value={item.id}>{item.nome}</MenuItem>
                ))}
              </Select>
            </StyledFormControl>

            <StyledFormControl>
              <InputLabel id="demo-simple-select-autowidth-label">
               Arbitros
              </InputLabel>
              <Select
                labelId="demo-simple-select-autowidth-label"
                id="demo-simple-select-autowidth"
                value={age}
                onChange={handleChange}
                fullWidth
                label="Age"
              >
                <MenuItem value="">{age}</MenuItem>
                {Judges.map((item, index) => (
                  <MenuItem value={item.id}>{item.nome}</MenuItem>
                ))}
              </Select>
            </StyledFormControl>

          </StyledInputRow>

          <Table
            data={partidas_noramalizadas}
            columns={columns}
            searchKey="name"
          />
        </div>
      </div>
    );
  }
}

export default GamesView;
