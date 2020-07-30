import unittest
import time
from modern_blaseball import blaseball_api

class TestBlaseballApi(unittest.TestCase):
    blaseball = blaseball_api()

    def setUp(self):
        # Let's not overload the blaseball api
        time.sleep(1)

    

    EXAMPLE_PLAYER = '17397256-c28c-4cad-85f2-a21768c66e67'
    
    EXAMPLE_PLAYERS = [
        "27c68d7f-5e40-4afa-8b6f-9df47b79e7dd",
        "63df8701-1871-4987-87d7-b55d4f1df2e9",
        "1f159bab-923a-4811-b6fa-02bfde50925a",
        "bf6a24d1-4e89-4790-a4ba-eeb2870cbf6f",
        "ea44bd36-65b4-4f3b-ac71-78d87a540b48",
        "e4034192-4dc6-4901-bb30-07fe3cf77b5e",
        "a1ed3396-114a-40bc-9ff0-54d7e1ad1718",
        "5ca7e854-dc00-4955-9235-d7fcd732ddcf",
        "75f9d874-5e69-438d-900d-a3fcb1d429b3",
        "773712f6-d76d-4caa-8a9b-56fe1d1a5a68",
        "0bb35615-63f2-4492-80ec-b6b322dc5450",
        "0d5300f6-0966-430f-903f-a4c2338abf00",
        "f741dc01-2bae-4459-bfc0-f97536193eea",
        "e16c3f28-eecd-4571-be1a-606bbac36b2b",
        "0ecf6190-f869-421a-b339-29195d30d37c",
        "d81ce662-07b6-4a73-baa4-acbbb41f9dc5",
        "10ea5d50-ec88-40a0-ab53-c6e11cc1e479",
        "d8758c1b-afbb-43a5-b00b-6004d419e2c5",
        "f0594932-8ef7-4d70-9894-df4be64875d8",
        "dfe3bc1b-fca8-47eb-965f-6cf947c35447",
        "3db02423-92af-485f-b30f-78256721dcc6",
        "6192daab-3318-44b5-953f-14d68cdb2722",
        "5149c919-48fe-45c6-b7ee-bb8e5828a095",
        "63a31035-2e6d-4922-a3f9-fa6e659b54ad",
        "937c1a37-4b05-4dc5-a86d-d75226f8490a"]
    
    EXAMPLE_TEAM = "878c1bf6-0d21-4659-bfee-916c8314d69c"

    EXAMPLE_LEAGUE = "d8545021-e9fc-48a3-af74-48685950a183"

    EXAMPLE_SUBLEAGUE = "7d3a3dd6-9ea1-4535-9d91-bde875c85e80"

    EXAMPLE_GAME = "dc767612-eb77-417b-8d2f-c21eb4dab868"

    EXAMPLE_SEASON = "0"

    EXAMPLE_BONUS_ID = "cbb567c0-d770-4d22-92f6-ff16ebb94758"

    EXAMPLE_DECREEE_ID = "b090fdfc-7d9d-414b-a4a5-bbc698028c15"

    EXAMPLE_PLAYOFF_NUM = "0"

    
    def test_global_events(self):
        result = blaseball.failover_500(self.blaseball.get_global_events)

        self.assertEqual(result.status_code, 200)
    
    def test_all_divisions(self):
        result = blaseball.failover_500(self.blaseball.get_all_divisions)

        self.assertEqual(result.status_code, 200)
    
    def test_league(self):
        result = blaseball.failover_500(self.blaseball.get_league, args=self.EXAMPLE_LEAGUE)

        self.assertEqual(result.status_code, 200)

    def test_sub_league(self):
        result = blaseball.failover_500(self.blaseball.get_sub_league, args=self.EXAMPLE_SUBLEAGUE)

        self.assertEqual(result.status_code, 200)
    
    def test_game(self):
        result = blaseball.failover_500(self.blaseball.get_game, args=self.EXAMPLE_GAME)

        self.assertEqual(result.status_code, 200)

    def test_offseason_setup(self):
        result = blaseball.failover_500(self.blaseball.get_offseason_setup)

        self.assertEqual(result.status_code, 200)
            
    def test_offseason_recap(self):
        result = blaseball.failover_500(self.blaseball.get_offseason_recap, args=self.EXAMPLE_SEASON)

        self.assertEqual(result.status_code, 200)
            
    def test_offseason_bonus_results(self):
        result = blaseball.failover_500(self.blaseball.get_offseason_bonus_results, args=self.EXAMPLE_BONUS_ID)

        self.assertEqual(result.status_code, 200)
            
    def test_offseason_decree_results(self):
        result = blaseball.failover_500(self.blaseball.get_offseason_decree_results, args=self.EXAMPLE_DECREEE_ID)

        self.assertEqual(result.status_code, 200)
            
    def test_playoff_details(self):
        result = blaseball.failover_500(self.blaseball.get_playoff_details, args=self.EXAMPLE_PLAYOFF_NUM)

        self.assertEqual(result.status_code, 200)
    
    def test_team(self):
        result = blaseball.failover_500(self.blaseball.get_team, args=self.EXAMPLE_TEAM)

        self.assertEqual(result.status_code, 200)
    
    def test_all_teams(self):
        result = blaseball.failover_500(self.blaseball.get_all_teams)

        self.assertEqual(result.status_code, 200)

    def test_one_player(self):
        result = blaseball.failover_500(self.blaseball.get_player_stats, args=self.EXAMPLE_PLAYER)

        self.assertEqual(result.status_code, 200)

    def test_many_players(self):
        result = blaseball.failover_500(self.blaseball.get_player_stats, args=self.EXAMPLE_PLAYERS)

        self.assertEqual(result.status_code, 200)
    def test_season(self):
        result = blaseball.failover_500(self.blaseball.get_season, args=self.EXAMPLE_SEASON)

        self.assertEqual(result.status_code, 200)

 
 

if __name__ == '__main__':
    unittest.main()
