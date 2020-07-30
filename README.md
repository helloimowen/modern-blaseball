
# this is NOT an endorsement of the music of the band "modern baseball" I am listening to them now and they are not very good. 



## A blaseball API interface. 

### Install via pip:

pip install modernblaseball


### Basic use: 


`from modernblaseball.modern_blaseball import blaseball_api`

`blaseball = blaseball_api()`

`result = blaseball.get_global_events()`

#### or: 

`pyobj = structure(blaseball.get_global_events)`

#### blaseball endpoints will often return a 500 when under load, so you can add failover logic as well: 

`blaseball.failover_500(self.blaseball.get_player_stats, args=self.EXAMPLE_PLAYER)`

#### todo: make all utilities more modular. 
`

### tests: 

`python -m unittest`