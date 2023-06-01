import { useState } from "react";
import Header from "./components/Header";
import BuscarPartida from "./components/Forms/BuscarPartida";



import Home from "./pages/home/index";

function App() {
  const [Stage, setStage] = useState(0);

  return (
    <div>
<Header/>
<BuscarPartida/>

    </div>
  );
}

export default App;
