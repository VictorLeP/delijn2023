import './App.css'
import Stelplaats, { IStelplaats } from './Stelplaats'

function App() {

  const [places, setPlaces] = useState([]);

  const test: Array<IStelplaats> = [{ id: 0, size: "klein", taken: true }, { id: 1, size: "normaal", taken: false }, { id: 2, size: "groot", taken: false }];

  return (
    <div style={{ display: "grid", gap: "20px" }}>
      {test.map((t, index) => <Stelplaats key={index} id={t.id} busses={t.busses} size={t.size} />)}
    </div>
  )
}

export default App
