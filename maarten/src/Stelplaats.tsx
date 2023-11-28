export type Busgrootte = "klein" | "normaal" | "groot";

export interface IStelplaats {
    size: Busgrootte;
    id: number;
    taken: boolean;
}

export default function Stelplaats({ size, id, taken }: IStelplaats) {

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

    const background = taken ? "#FFDD00" : "#999999";


    return <div style={{ display: "grid", placeItems: "center", width: sizeToStyle(size), backgroundColor: background, height: `${base}px`, position: "relative" }}>
        <span style={{ position: "absolute", top: "0", left: "0" }}>{id}</span>
        {/* <img src="./Group 3.svg" style={{ objectFit: "contain", position: "relative" }}></img> */}
    </div>
}