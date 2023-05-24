import { useState } from "react";

import "xp.css/dist/XP.css";

import GameByCountry from "./pages/games-by-county";
import GameNumbers from "./pages/games-number-moviments";
import GameView from "./pages/games-view";
import GameRounds from "./pages/rounds-for-game";

import "./App.css"

function App() {
  const [Stage, setStage] = useState(0);

  const pageInstance = [
    <GameView />,
    <GameRounds />,
    <GameNumbers />,
    <GameByCountry />,
  ];

  return (
    <div>
      <div className="window" id="window">
        <div className="title-bar">
          <div className="title-bar-text">Sistema do jogo de xadrez</div>
          <div className="title-bar-controls">
            <button aria-label="Minimize"></button>
            <button aria-label="Maximize"></button>
            <button aria-label="Close"></button>
          </div>
        </div>
        <div className="window-body">
          <menu role="tablist">
            <button aria-selected="true" aria-controls="Jogos" onClick={()=>{setStage(0)}}>
              Jogos
            </button>
            <button aria-controls="jogos por jogadas" onClick={()=>{setStage(1)}}>Jogos por jogadas</button>
            <button aria-controls="Jogos por nação" onClick={()=>{setStage(2)}}>Jogos por nação</button>
          </menu>
      


    
          {pageInstance[Stage]}

        </div>
      </div>
    </div>
  );
}

export default App;
