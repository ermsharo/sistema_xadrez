import React from 'react';
import { ResponsiveContainer, BarChart, XAxis, YAxis, Bar, Tooltip } from 'recharts';

// interface BarData {
//   name: string;
//   value: number;
// }

interface BarPlotProps {
  data: any[];
}

const BarPlot: React.FC<BarPlotProps> = ({ data }) => {
  
console.log("Bar plot data", data)
  
  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="value" fill="#8884d8" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default BarPlot;
