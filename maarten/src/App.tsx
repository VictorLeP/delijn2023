import './App.css'
import Stelplaats, { Busgrootte } from './Stelplaats'

function App() {

  const test: Array<Busgrootte> = ["klein", "normaal", "groot"];

  return (
    <div style={{ display: "grid", gap: "20px" }}>
      {test.map((t, index) => <Stelplaats key={index} size={t} />)}
    </div>
  )
}

export default App
