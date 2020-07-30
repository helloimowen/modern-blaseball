# Learnings 

I've learned a lot about the game of blaseball by rooting around in their API. This document serves as my captain's log. 

## Player stats 

The stars that you see next to a player's name is a composite score of 27 attributes. 

        "_id": "17397256-c28c-4cad-85f2-a21768c66e67",
        "anticapitalism": 0.3865984034527832,
        "baseThirst": 0.8163297863171528,
        "buoyancy": 0.6295030935858079,
        "chasiness": 0.3876884722913716,
        "coldness": 0.04077503022645801,
        "continuation": 0.9332406398132362,
        "divinity": 0.765859860942711,
        "groundFriction": 0.6234756539195374,
        "indulgence": 0.6302776113973703,
        "laserlikeness": 0.5813163393413376,
        "martyrdom": 0.7183643543823621,
        "moxie": 0.8930963701536112,
        "musclitude": 0.42446974479490573,
        "name": "Cory Ross",
        "omniscience": 0.40240204027262094,
        "overpowerment": 0.588492025671367,
        "patheticism": 0.8852546298408897,
        "ruthlessness": 0.034373471563752256,
        "shakespearianism": 0.4707237610843995,
        "suppression": 0.7581323899020682,
        "tenaciousness": 0.5321892387925751,
        "thwackability": 0.0337877991334099,
        "tragicness": 0,
        "unthwackability": 0.46406385877539,
        "watchfulness": 0.6211609170901324,
        "pressurization": 0.19961729034104736,
        "totalFingers": 10,
        "soul": 6


## The Bullpen and the Bench 

Pulling a team from the database endpoint reveals that there are ten extra players on every blaseball team - a bullpen and a bench. 


{
	"lineup": ["27c68d7f-5e40-4afa-8b6f-9df47b79e7dd", "63df8701-1871-4987-87d7-b55d4f1df2e9", "1f159bab-923a-4811-b6fa-02bfde50925a", "bf6a24d1-4e89-4790-a4ba-eeb2870cbf6f", "ea44bd36-65b4-4f3b-ac71-78d87a540b48", "e4034192-4dc6-4901-bb30-07fe3cf77b5e", "a1ed3396-114a-40bc-9ff0-54d7e1ad1718", "5ca7e854-dc00-4955-9235-d7fcd732ddcf", "75f9d874-5e69-438d-900d-a3fcb1d429b3"],
	"rotation": ["773712f6-d76d-4caa-8a9b-56fe1d1a5a68", "0bb35615-63f2-4492-80ec-b6b322dc5450", "0d5300f6-0966-430f-903f-a4c2338abf00", "f741dc01-2bae-4459-bfc0-f97536193eea", "e16c3f28-eecd-4571-be1a-606bbac36b2b"],
	"bullpen": ["0ecf6190-f869-421a-b339-29195d30d37c", "d81ce662-07b6-4a73-baa4-acbbb41f9dc5", "10ea5d50-ec88-40a0-ab53-c6e11cc1e479", "d8758c1b-afbb-43a5-b00b-6004d419e2c5", "f0594932-8ef7-4d70-9894-df4be64875d8", "dfe3bc1b-fca8-47eb-965f-6cf947c35447", "3db02423-92af-485f-b30f-78256721dcc6", "6192daab-3318-44b5-953f-14d68cdb2722"],
	"bench": ["5149c919-48fe-45c6-b7ee-bb8e5828a095", "63a31035-2e6d-4922-a3f9-fa6e659b54ad", "937c1a37-4b05-4dc5-a86d-d75226f8490a"],
	"_id": "878c1bf6-0d21-4659-bfee-916c8314d69c",
	"fullName": "Los Angeles Tacos",
	"location": "Los Angeles",
	"mainColor": "#64376e",
	"nickname": "Tacos",
	"secondaryColor": "#dbd26e",
	"shorthand": "LATA",
	"emoji": "0x1F32E",
	"slogan": "72° and Spicy"
}

## The two leagues (Good and Evil) and subleagues (chaotic and lawful) are actually subsubleagues of a larger league called Internet League Blaseball

GET https://blaseball.com/database/league?id=d8545021-e9fc-48a3-af74-48685950a183


`{"subleagues":["7d3a3dd6-9ea1-4535-9d91-bde875c85e80","93e58443-9617-44d4-8561-e254a1dbd450"],"_id":"d8545021-e9fc-48a3-af74-48685950a183","name":"Internet League Blaseball","tiebreakers":"72a618ed-c61c-4162-a455-3959a2d0e738"}`

also, I have no idea what "tiebreakers" signafies in this case.

## ids for analytics endpoints that the front end (seemingly) never calls 

Calling the /database/season endpoint reveals ids and paths that are not used by the frontend, from what I have seen. 

{"_id":"9dbb3119-7e0d-4fa7-bab9-caef1c19e03d","__v":0,"league":"d8545021-e9fc-48a3-af74-48685950a183","rules":"4ae9d46a-5408-460a-84fb-cbd8d03fff6c","schedule":"a50a6d24-b34f-435d-a1c9-b986f8f8d36e","seasonNumber":0,"standings":"03e5bb40-01cc-4f0b-9a2b-c0968a0a890d","stats":"8b0bb83b-ae1b-4b80-85a7-96eefc2d45cb","terminology":"b67e9bbb-1495-4e1b-b517-f1444b0a6c8b"} 


# notes 

The blaseball api is on the same subdomain as blaseball itself (naked domain - aka https://blaseball.com), so when an endpoint is invalid it redirects to the front page of blaseball. 



# What we still need to find 

1. Historical match data. The /database/standings endpoint returns total wins and losses

# TODO: Owen 