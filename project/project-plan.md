# Project Plan

## Title
<!-- Give your project a short title. -->
Impact of Electric Car adoption on air pollution.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
* How has the adoption of electric vehicles in Washington State, particularly in Seattle, influenced air quality over time?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
* Air pollution is an important problem in big cities. In this project we analyze the relation between electric car adoption and air quality in Washington State and in particular in it's major cities.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Electric Vehicle Population Size History By County
* Metadata URL: [EV Population](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Size-History-By-County/3d5d-sdqb/about_data)
* Data URL: [Download EV Population](https://data.wa.gov/resource/3d5d-sdqb.csv?$limit=50000)
* Data Type: CSV
* License: [Open Database](https://opendatacommons.org/licenses/odbl/1-0/)

Washington State Open Data Portal. Free public data published by Washington state agencies and partners.

### Datasource2: Air Quality System (AQS) Data
* Metadata URL: [Air Data Description](https://aqs.epa.gov/aqsweb/airdata/FileFormats.html#_introduction)
* Data URL: for each year and each pollutant a different zip file has to be downloaded from [Air Data](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
* Data Type: zip folder containing CSV file.
* License: [Public Domain](https://opendatacommons.org/licenses/pddl/1-0/)

The Air Quality System (AQS) contains ambient air pollution data collected by the Environmental Protection Agency (EPA), state, local, and tribal air pollution control agencies from over thousands of monitors.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Defined Project Plan [#1][i1]
2. Data Pipeline [#2][i2]
3. Data Report [#3][i3]
4. Automated Testing [#4][i4]
5. Continuous Integration [#5][i5]
6. Analysis Report [#6][i6]

[i1]: https://github.com/korn3lie/made-project/issues/1
[i2]: https://github.com/korn3lie/made-project/issues/2
[i3]: https://github.com/korn3lie/made-project/issues/3
[i4]: https://github.com/korn3lie/made-project/issues/4
[i5]: https://github.com/korn3lie/made-project/issues/5
[i6]: https://github.com/korn3lie/made-project/issues/6
