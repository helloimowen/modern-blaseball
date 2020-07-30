import requests 
import json 
import time

class blaseball_api():
    
    ##############################################################################
    # # # # # # # # # # # # # # # # INTERNAL METHODS # # # # # # # # # # # # # # #
    ##############################################################################
    
    def __init__(self):
        self.URL_BASE = 'https://blaseball.com'
        pass

    ##############################################################################
    # # # # # # # # # # # # # # # # ENDPOINTS  # # # # # # # # # # # # # # # # # #
    ##############################################################################


    def get_global_events(self):
        # https://blaseball.com/database/globalEvents
        return requests.get(self.URL_BASE + '/database/globalEvents')
    
    def get_all_divisions(self):
        # https://blaseball.com/database/allDivisions
        return requests.get(self.URL_BASE + '/database/allDivisions')

    def get_league(self, league_id):
        # https://blaseball.com/database/league?id=d8545021-e9fc-48a3-af74-48685950a183
        return requests.get(self.URL_BASE + '/database/league', 
                            params={'id':[league_id]})


    def get_sub_league(self, sub_league_ids):
        # https://blaseball.com/database/subleague?id=7d3a3dd6-9ea1-4535-9d91-bde875c85e80
        return requests.get(self.URL_BASE + '/database/subleague', 
                            params={'id':[sub_league_ids]})

    def get_game(self, game_id):
        # https://blaseball.com/database/gameById/dc767612-eb77-417b-8d2f-c21eb4dab868
        return requests.get(self.URL_BASE + '/database/gameById/' + game_id)

    def get_offseason_setup(self):
        # https://blaseball.com/database/offseasonSetup
        return requests.get(self.URL_BASE + '/database/offseasonSetup')

    def get_offseason_recap(self, season_num):
        # https://blaseball.com/database/offseasonRecap?season=0
        return requests.get(self.URL_BASE + '/database/offseasonRecap', 
                            params={'season':[season_num]})

    def get_offseason_bonus_results(self, bonus_id):
        # https://blaseball.com/database/bonusResults?ids=cbb567c0-d770-4d22-92f6-ff16ebb94758
        return requests.get(self.URL_BASE + '/database/bonusResults', 
                    params={'ids':[bonus_id]})

    def get_offseason_decree_results(self, decree_ids):
        # https://blaseball.com/database/decreeResults?ids=b090fdfc-7d9d-414b-a4a5-bbc698028c15
        return requests.get(self.URL_BASE + '/database/decreeResults', 
                    params={'ids':[decree_ids]})

    def get_playoff_details(self, playoff_num):
        # https://blaseball.com/database/playoffs?number=0
        return requests.get(self.URL_BASE + '/database/playoffs', 
                    params={'number':[playoff_num]})

    def get_team(self, team_id):
        # https://blaseball.com/database/team?id=878c1bf6-0d21-4659-bfee-916c8314d69c
        return requests.get(self.URL_BASE + '/database/team',
            params={'number':[team_id]})

    def get_all_teams(self):
        # https://blaseball.com/database/allTeams
        return requests.get(self.URL_BASE + '/database/allTeams')

    def get_player_stats(self, player_list): 
        if len(player_list[0]) > 1:
            return requests.get(self.URL_BASE + '/database/players', 
                                params={'ids':[','.join(player_list)]})
        else: 
            return requests.get(self.URL_BASE + '/database/players', 
                                params={'ids':[player_list]})

    def get_season(self, season_num):
        # https://blaseball.com/database/season?number=0
        return requests.get(self.URL_BASE + '/database/season', 
                            params={'number':[season_num]})
    
    def get_simulation_data(self):
        # Starting point 
        # Where did it go? 
        pass
    

    ##############################################################################
    # # # # # # # # # # # # # # # # # HELPERS  # # # # # # # # # # # # # # # # # #
    ##############################################################################
    
    def manage_batch(self, endpoint_func, list_of_payloads, sleepy_time=1): 
        results = []
        
        for payload in list_of_payloads:
            results.append(endpoint_func(payload))
            time.sleep(sleepy_time)
        return results
    
    def structure(self, func, args=None):
        if args:
            results = self.func(args)
        else:
            results = self.func()
        return json.loads(results.text)

    def failover_500(self, func, args=None, max_tries=3, sleepy_time=1):
        tries = 0
        while tries < max_tries:
            if args:
                result = func(args)
            else:
                result = func()

            if result.status_code != 500: 
                break
            time.sleep(sleepy_time)
            tries += 1
        return result 