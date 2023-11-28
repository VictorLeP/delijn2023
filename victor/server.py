
from typing import Union

from fastapi import FastAPI

from victor import scheduling
from victor.classes import Bus, Garage, Stelplaats
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/allocate_buses")
async def allocate_buses():
    j = get_json()
    s = scheduling.Scheduler()
    t = s.allocate_bus_schedule(j)

    return {
        "stelplaats": j["stelplaats"],
        "parking":  s.stelplaatsen["De Lijn Arsenaal"].unallocated_buses,
        "garage": s.stelplaatsen["De Lijn Arsenaal"].garage.garage_allocations,
    }

@app.get("/json")
def read_json():
    return get_json()



def get_json():
    return {
	"stelplaats": "De Lijn Arsenaal",
	"parking": [
		{"bus": "3000","type": "MINI"},
		{"bus": "3001","type": "MINI"},
		{"bus": "3002","type": "MINI"},
		{"bus": "3003","type": "MINI"},
		{"bus": "3004","type": "MINI"},
		{"bus": "3005","type": "MINI"},
		{"bus": "3006","type": "MINI"},
		{"bus": "3007","type": "MINI"},
		{"bus": "3008","type": "MINI"},
		{"bus": "3009","type": "MINI"},
		{"bus": "3010","type": "MINI"},
		{"bus": "3011","type": "MINI"},
		{"bus": "3012","type": "MINI"},
		{"bus": "2000","type": "NORMAAL"},
		{"bus": "2001","type": "NORMAAL"},
		{"bus": "2002","type": "NORMAAL"},
		{"bus": "2003","type": "NORMAAL"},
		{"bus": "2004","type": "NORMAAL"},
		{"bus": "2005","type": "NORMAAL"},
		{"bus": "1000","type": "GROOT"},
		{"bus": "1001","type": "GROOT"},
		{"bus": "1002","type": "GROOT"}
	],
	"garage": {
		"groot": [],
		"medium": [],
		"klein": []
	}
}