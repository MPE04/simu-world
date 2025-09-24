# Development steps


## Step 1 : initialisation


- [x] Create a first location
- [x] Create PNJ agent
- [x] PNJ comportment :
  - [x] All consume food at each step
  - [x] Some are producer and produce food
- [x] Run world
- [x] City food graph
- [x] Graph with Solara


## Step 2 : Consolidation

- [x] Mange more than 1 cities
- [x] Configuration done by json file
- [x] Dispatch PNJ between cities
- [x] PNJ linked to Cities (food for the moment)
- [x] Add logging information
- [x] improve dashboard view : 1 sheet per location


## Step 3 : increase static world capacity

- [x] Remove self.type
- [ ] Add city population : not only PNJ, but static number (high) by config file + random if nothing provided
- [ ] Add city ressources (metal, type of food…) by config file
- [ ] Add city production (manufactured things) by config file
- [ ] When nothing provide in config file, create default features with randomisation
- [ ] Create algo for production : link between population / ressource and population / production
- [ ] Update solara dashboard with graph for each ressources



