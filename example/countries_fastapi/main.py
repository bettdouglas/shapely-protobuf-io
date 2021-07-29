from typing import List
import geopandas as gpd
from fastapi import FastAPI
from geojson_pydantic.geometries import Geometry
from geojson_pydantic.features import Feature
from pydantic import BaseModel
from shapely.geometry.geo import shape
import json
import shapely


class Country(BaseModel):
    name: str
    code: str
    type: str
    geometry: Feature


app = FastAPI(
    title="Natural Earth Countries",
    description="This is a list of endpoints which you can use to access natural earth data.",
    version="0.0.1",
    docs_url='/',
)

gdf = gpd.read_file('data/ne_110m_admin_0_countries.zip')
gdf['name'] = gdf['ADMIN'].apply(lambda x: x.lower())

@app.get('/countries/all')
def get_all_countries() -> List[Country]:
    return rows_to_countries(gdf)


@app.get('/countries/search/{name}')
def search_countries(name: str):
    name = name.lower()
    subset = gdf.loc[gdf["name"].str.contains(name)]
    return rows_to_countries(subset)

@app.get('/countries/within-boundary')
def countries_intersecting(boundary: Geometry):
    bounds = shape(boundary)
    subset = gdf.loc[gdf.intersects(bounds)]
    return rows_to_countries(subset)


def row_to_country(row):
    return Country(
        name=row["ADMIN"],
        type=row["TYPE"],
        geometry=Feature(geometry=row['geometry']),
        code=row["ADM0_A3"],
    )


def rows_to_countries(gdf):
    return [row_to_country(row) for _, row in gdf.iterrows()]