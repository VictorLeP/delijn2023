export type Busgrootte = "klein" | "normaal" | "groot";

export interface IStelplaats {
    size: Busgrootte;
}

export default function Stelplaats({ size }: IStelplaats) {

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


    return <div style={{ display: "block", height: sizeToStyle(size), backgroundColor: "red", width: `${base}px` }}></div>
}