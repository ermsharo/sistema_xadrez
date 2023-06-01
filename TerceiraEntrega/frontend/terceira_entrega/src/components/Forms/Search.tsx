import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Locais from "./Locais";
import Hotel from "./Hotel";

function Bar() {
  return (
    <Box
      sx={{
        height: 24,
      }}
    />
  );
}

export default function Search() {
  return (
    <Box component="form" noValidate autoComplete="off">
      <div>
        <Bar />
        <TextField fullWidth id="outlined" label="Jogador" />
        <Bar />
        <TextField fullWidth id="outlined" label="Arbitro" />
        <Bar />
        <TextField
          fullWidth
          id="outlined"
          label="Local"
          defaultValue="Hello World"
        />
        <Bar />
        <TextField
          fullWidth
          id="outlined"
          label="Required"
          defaultValue="Hello World"
        />
        <Bar />
        <Locais />
        <Bar />
        <Hotel />
      </div>
    </Box>
  );
}
