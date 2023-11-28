export type Busgrootte = "klein" | "normaal" | "groot";

export interface IStelplaats {
    size: Busgrootte;
    id: number;
    busses: Array<Busgrootte>;
}

export default function Stelplaats({ size, id, busses }: IStelplaats) {

    const base = 100;

    const sizeToStyle = (size: Busgrootte) => {
        let modifier = 1;
        switch (size) {
            case "normaal":
                modifier = 2;
                break;
            case "groot":
                modifier = 4;
                break;
            default:
                break;
        }
        return `${base * modifier}px`;
    }

    const background = "#999999";


    return <div style={{ display: "grid", placeItems: "center", width: sizeToStyle(size), backgroundColor: background, height: `${base}px`, position: "relative" }}>
        <span style={{ position: "absolute", top: "0", left: "0" }}>{id}</span>
        <div style={{ display: "flex" }}>
            {busses.map(b => <div style={{ display: "grid", placeItems: "center", width: sizeToStyle(b), backgroundColor: background, height: `${base}px`, position: "relative" }}></div>)}
            {/* <img src="./Group 3.svg" style={{ objectFit: "contain", position: "relative" }}></img> */}
        </div>
    </div>
}